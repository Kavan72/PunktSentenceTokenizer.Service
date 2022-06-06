import os

import sentence_pb2_grpc as sentence_service
import sentence_service_pb2 as sentence_message

from client_wrapper import ServiceClient

SERVER_HOST: str = os.getenv("SERVER_HOST", "0.0.0.0")
SERVER_PORT: int = int(os.getenv("SERVER_PORT", "4569"))


def run():
    sentence = ServiceClient(sentence_service, 'SentenceStub', SERVER_HOST, SERVER_PORT)

    paragraph = """
    Sometimes we come across some forgetful persons in our surroundings. And some geniuses are also forgetful to some extent. We know that Newton 
    boiled his pocket watch instead of an egg. Once Einstein was traveling without a ticket in a train. When the checker demanded the ticket, he was 
    frantically searching for the missing ticket. However, when the checker could recognize him, he assured that the scientist would not have to search 
    for it. Einstein still went on searching and remarked that he was searching to find out where he was going for he totally forgot about his destination.
    But the most striking incident centered around my father on my sister’s birthday. The dinner was ready but the guests were absent. Finally, father
    discovered that all the invitation letters were lying in his drawer. The incident has become a family legend. 
    """

    # Insert example metadata
    metadata = [('ip', '127.0.0.1')]
    response = sentence.Split(
        sentence_message.SplitSentenceRequest(
            paragraph=paragraph,
            language=sentence_message.Language.ENGLISH
        ),
        metadata=metadata
    )

    print(response)


if __name__ == '__main__':
    run()
