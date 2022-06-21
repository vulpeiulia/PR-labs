import utils
import consts
import logging
import threading
from flask import Flask, request
from domain.kitchen import Kitchen

logging.basicConfig(filename='kitchen.log', level=logging.DEBUG, format='%(asctime)s: %(message)s', datefmt="%m/%d/%Y %I:%M:%S %p")
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')



def simulation():
    for i in range(1, 10):
        print(i)
        app = Flask(f'Kitchen - {i}')
        dr_port = int(f'{i}')
        kt_port = int(f'{i}')

        kitchen_data = utils.fetch_kitchen_data_from_dr(dr_port)
        kitchen = Kitchen(kt_port, dr_port, i, kitchen_data['cooks'], kitchen_data['ovens'], kitchen_data['stoves'], kitchen_data['menu'])

        @app.route('/order', methods=['POST'])
        def order(kt=kitchen):
            data = request.get_json()
            logger.info(f'Kitchen-{kt.id_} NEW ORDER "{data["order_id"]}" | priority: {data["priority"]} | items: {data["items"]}\n')
            return k.receive_new_order(data)

        threading.Thread(target=lambda: app.run(host=consts.HOST, port=kitchen.port, debug=False, use_reloader=False, threaded=True), name=f'FLASK-K{i}', daemon=True).start()

        # kitchen simulation
        threading.Thread(target=kitchen.start_kitchen, daemon=True).start()


def main():
    open("kitchen.log", "w").close()

    simulation()

    while True:
        pass


if __name__ == '__main__':
    main()