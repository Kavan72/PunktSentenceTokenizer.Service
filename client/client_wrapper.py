import grpc
import sys
from functools import partial


class ServiceClient:
    def __init__(self, service_module, stub_name, host, port, timeout=5):
        channel = grpc.insecure_channel(f'{host}:{port}')
        try:
            grpc.channel_ready_future(channel).result(timeout=timeout)
        except grpc.FutureTimeoutError:
            sys.exit('Error connecting to server')
        self.stub = getattr(service_module, stub_name)(channel)
        self.timeout = timeout

    def __getattr__(self, attr):
        return partial(self._wrapped_call, self.stub, attr)

    def _wrapped_call(self, *args, **kwargs):
        try:
            return getattr(args[0], args[1])(
                args[2], **kwargs, timeout=self.timeout
            )
        except grpc.RpcError as e:
            raise print('Call {0} failed with {1}'.format(
                args[1], e.code())
            )

