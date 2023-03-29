from flask import Flask, jsonify
from scrapy import cmdline
import json
from multiprocessing import Process
import os
import time
import datetime


app = Flask(__name__)

def scrape_data(jsonName):
    cmdline.execute(["scrapy", "crawl", "departments", "-o", jsonName])

@app.route('/', methods=['GET'])
def index():
    # Definimos nombre al archivo json
    date=datetime.datetime.now()
    dateYmd= date.date().strftime('%Y-%m-%d')
    hour= date.strftime('%H_%M_%S')
    jsonName=dateYmd+'__'+hour+'.json'

    # Ejecutar el scraping en un proceso hijo
    p = Process(target=scrape_data, args=(jsonName,))
    p.start()
    p.join()

    # esperear a que el archivo exista
    while not os.path.exists(jsonName):
        time.sleep(5)

    # Leer el archivo generado por el scraping
    with open(jsonName) as file:
        data = json.load(file)

    return jsonify(data)



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)