# Наиль Зайнетдинов, 6-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)

track = post_new_order(data.order_type).json()['track']
def get_order_from_track():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + str(track))

def test_order_from_track():
    response = get_order_from_track()
    assert response.status_code == 200
