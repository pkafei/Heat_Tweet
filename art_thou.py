#!/bin/env python
# encoding: utf-8

"""
Webservice prototype for exposing cell data via
HTTP and JSON/JSONP
"""

DB = 'tstream'
CELLS_COLLECTION = 'tweet'

import json
import time
import math
import redis
import threading
import signal
import sys
from flask import Flask
from flask import request
from flask import abort
from flask import url_for

app = Flask(__name__)


@app.route('/tweets')
def tweets():

    url_for('static', filename='map.html')
    url_for('static', filename='jquery-1.7.2.min.js')
    url_for('static', filename='jquery.eventsource.js')
    url_for('static', filename='jquery-1.7.2.js')
    return Response(event_stream(),
        headers={'Content-Type':'text/event-stream'})


def runThread():
    st = Thread( target = tail_mongo_thread )
    st.start()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    app.before_first_request(runThread)
    app.run(debug=True, host='0.0.0.0')
