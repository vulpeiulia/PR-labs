import consts
import logging
import threading
import coloredlogs
from flask import Flask, request

logging.basicConfig(filename='ordering.log', level=logging.DEBUG, format='%(asctime)s:  %(message)s', datefmt="%m/%d/%Y %I:%M:%S %p")
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')


def simulate():
    app = Flask('Ordering')
    manager = OrderManager()


    @app.route('/menu', methods=['GET'])
    def get_menu():
        return manager.get_menu()

    @app.route('/order', methods=['POST'])
    def order():
        data = request.get_json()
        return manager.make_order(data)

    @app.route('/rating', methods=['POST'])
    def rating():
        data = request.get_json()
        return manager.rating(data)

    threading.Thread(target=lambda: app.run(host=consts.HOST, port=consts.FO_PORT,  use_reloader=False, threaded=True), daemon=True).start()


def main():
    open("ordering.log", "w").close()

    simulate()

    while True:
        pass


if __name__ == '__main__':
    main()