from protos.gen_py import sentence_pb2_grpc as sentence_service
from protos.gen_py import sentence_service_pb2 as sentence_messages


class SentenceService(sentence_service.SentenceServicer):
    def Split(self, request, context):
        metadata = dict(context.invocation_metadata())
        sentence = sentence_messages.Sentence(sentence=request.sentence)
        return sentence_messages.SplitSentenceResult(
            sentences=[sentence]
        )


