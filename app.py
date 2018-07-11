import csv
from pathlib import Path

from flask import Flask, render_template, jsonify
import netaddr

from clustipy import clustipy

app = Flask(__name__)


@app.route('/clusters')
def clusters():
    networks = []
    with Path('tests/test_address.csv').open() as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            networks.append(netaddr.IPNetwork(row[0].split('/')[0]))
    result = clustipy.clustering(networks, 25)
    return jsonify(networks=[str(r) for r in result])


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
