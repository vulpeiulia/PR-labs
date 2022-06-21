import utils
import consts
import logging
import requests
import threading
from flask import Flask, request
from domain.DiningRoom import DiningRoom

logging.basicConfig(filename='dining.log', level=logging.DEBUG, format='%(asctime)s: %(message)s', datefmt="%m/%d/%Y %I:%M:%S %p")
logger = logging.getLogger(__name__)




def simulation():
    restaurants = utils.get_restaurants()


    for r in restaurants:
        app = Flask(r['name'])
        dining = DiningRoom(r)

        requests.post(f'http://{consts.FO_HOST}:{consts.FO_PORT}/register', json=r)


        @app.route('/menu', methods=['GET'])
        def menu(app_dr=dining):
            return app_dr.get_menu()

        @app.route('/order', methods=['POST'])
        def order(app_dr=dining):
            data = request.get_json()
            return app_dr.order(data)

        @app.route('/order/<order_id>', methods=['GET'])
        def get_order(order_id, app_dr=dining):
            return app_dr.get_order(order_id)

        
        @app.route('/restaurant_data', methods=['GET'])
        def get_restaurant_data(app_dr=dining):
            # generating orders 
            threading.Thread(target=app_dr.start_dining_work).start()
            return app_dr.get_restaurant_data()

        
        @app.route('/rating', methods=['POST'])
        def rating(app_dr=dining):
            data = request.get_json()
            return app_dr.update_rating(data)

        threading.Thread(target=abc): app.run(host=consts.HOST, port=dining.config['dining_port'], debug=False, use_reloader=False, threaded=True), name=f'{dining.name}'.start()


def main():
    open("dining.log", "w").close()

    simulation()

    while True:
        pass


if __name__ == '__main__':
    main()