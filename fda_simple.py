import csv

import logging
import json

def doit():
    count = 0
    with open('device-510k-0001-of-0001.json', encoding='utf-8') as inputfile:
        file = json.load(inputfile)
        apps = file['results']
        for app in apps:
            if 'registration_number' in app['openfda']:
                app['openfda'].pop('registration_number')
            if 'fei_number' in app['openfda']:
                app['openfda'].pop('fei_number')
            # unpack
            for field in app['openfda']:
                app[field + 'open_fda_field'] = app['openfda'][field]
            app.pop('openfda')
        write_first(apps)

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
    # get()
    doit()
