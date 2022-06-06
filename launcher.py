import time
import nltk
import config

from server import get_server

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


def main(host, port):
    nltk.download('punkt')

    server = get_server(host, port)
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    main(config.SERVER_HOST, config.SERVER_PORT)
