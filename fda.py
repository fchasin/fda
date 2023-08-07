import requests
import json
import csv
import time
import logging

def get():
    api_url = 'https://api.fda.gov'
    base_url = api_url + '/device/510k.json'
    count = 0
    my_params = {"params":
                     {"limit": 100,"skip": 0},
                 "base_url": base_url}

    response = requests.get(url=base_url, params=my_params["params"])

    while (response.status_code == 200):
        response = call_api(my_params)
        my_params['params']['skip'] += 100
        count += 1
        logging.debug(f'On {count} iteration of the loop, est. {my_params["params"]["limit"] * count} records fetched.')

def call_api(params):
    response = requests.get(url=params['base_url'], params=params['params'])
    if response.status_code == 200:
        # df = pd.read_json(text)
        time.sleep(0.1)
        array = response.json()
        text = json.dumps(array)
        dataset = json.loads(text)
        apps = dataset['results']
        for app in apps:
            if 'registration_number' in app['openfda']:
                app['openfda'].pop('registration_number')
            if 'fei_number' in app['openfda']:
                app['openfda'].pop('fei_number')
            # unpack
            for field in app['openfda']:
                app[field + 'open_fda_field'] = app['openfda'][field]
            app.pop('openfda')
        if params['params']['skip'] == 0:
            write_first(apps)
        else:
            write_next(apps)
    else:
        print("Error: Unable to fetch adverse events.")
        return None

    return response

def write_first(apps):
    csvFile = open("filename.csv", 'w')
    csvWriter = csv.writer(csvFile)
    # write header
    keys = apps[0].keys()
    csvWriter.writerow(keys)

    # write data
    write(apps, csvWriter)
    csvFile.close()

def write_next(apps):
    csvFile = open("filename.csv", 'a')
    csvWriter = csv.writer(csvFile)
    write(apps, csvWriter)
    csvFile.close()

def write(apps, csvWriter):
    for line in apps:
        csvWriter.writerow(line.values())

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.DEBUG)
    get()
