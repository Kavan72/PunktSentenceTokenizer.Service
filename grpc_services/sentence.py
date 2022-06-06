import nltk

from protos.gen_py import sentence_pb2_grpc as sentence_service
from protos.gen_py import sentence_service_pb2 as sentence_message


class SentenceService(sentence_service.SentenceServicer):
    def Split(self, request, context):
        metadata = dict(context.invocation_metadata())

        return sentence_message.SplitSentenceResult(
            sentences=[
                sentence_message.Sentence(sentence=sentence)
                for sentence in nltk.sent_tokenize(request.paragraph, sentence_message.Language.Name(request.language).lower())
            ]
        )


