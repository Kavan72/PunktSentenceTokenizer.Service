import grpc

from concurrent import futures
from grpc_services.sentence import SentenceService
from protos.gen_py import sentence_pb2_grpc as sentence_service


def get_server(host, port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sentence_service.add_SentenceServicer_to_server(SentenceService(), server)
    server.add_insecure_port(f'{host}:{port}')
    return server
