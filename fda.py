import requests
import logging
from utils import call_api


def get():
    api_url = 'https://api.fda.gov'
    base_url = api_url + '/device/510k.json'
    count = 0
    my_params = {"params":
                     {"limit": 100, "skip": 0},
                 "base_url": base_url}

    response = requests.get(url=base_url, params=my_params["params"])

    while response.status_code == 200:
        response = call_api(my_params)
        my_params['params']['skip'] += 100
        count += 1
        logging.debug(f'On {count} iteration of the loop, est. {my_params["params"]["limit"] * count} records fetched.')


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
    get()
