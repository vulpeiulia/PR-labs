import consts
import logging
import threading
from flask import Flask
from domain.Client import Client

logging.basicConfig(filename='client_service.log', level=logging.DEBUG, format='%(asctime)s: %(threadName)s: %(message)s', datefmt="%m/%d/%Y %I:%M:%S %p")
logger = logging.getLogger(__name__)


def simulation():
    app = Flask('Client-Service')
    threading.Thread(target=lambda: app.run(host=consts.HOST, port=consts.CS_PORT, debug=False, use_reloader=False, threaded=True), name=f'FLASK-MAIN', daemon=True).start()

    for i in range():
        client = Client(i)
        threading.Thread(target=client.generate_order, daemon=True, name=f'Client-{i}').start()


def main():
    open("client_service.log", "w").close()

    simulation()

    while True:
        pass


if __name__ == '__main__':
    main()