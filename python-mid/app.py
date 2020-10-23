from typing import List, Dict
import requests
from flask import Flask, render_template, request, session, redirect, url_for
import json
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

app = Flask(__name__)
"""
@app.route('/<path:text>')
def home(text):
    if text.startswith('v1'):
        HOST_IP = os.environ.get('HOST_IP')
        POD_IP = os.environ.get('POD_IP')
        HOSTNAME = os.environ.get('HOSTNAME')
        return "I'm from Python Application" + '            ' + "My HostName is {}".format(HOSTNAME) + '          ' + "My POD IP is {}".format(POD_IP) + '            ' + "My Host IP Is {}".format(HOST_IP)
    elif text.startswith('v2'):
        HOST_IP = os.environ.get('HOST_IP')
        POD_IP = os.environ.get('POD_IP')
        HOSTNAME = os.environ.get('HOSTNAME')
        return "I'm from Python Application" + '            ' + "My HostName is {}".format(HOSTNAME) + '          ' + "My POD IP is {}".format(POD_IP) + '            ' + "My Host IP Is {}".format(HOST_IP)
    else:
        HOST_IP = os.environ.get('HOST_IP')
        POD_IP = os.environ.get('POD_IP')
        HOSTNAME = os.environ.get('HOSTNAME')
        return "Not right cotext, Provide either v1 or v2" + '           ' "My HostName is {}".format(HOSTNAME) + '            ' + "My POD IP is {}".format(POD_IP) + '              ' + "My Host IP Is {}".format(HOST_IP)

"""
@app.route('/')
def hello():
    PYBACKEND = os.environ.get("PY_BACKEND")
    return requests.get(PYBACKEND).content

@app.route('/<path:text>')
def web(text):
    if text.startswith('pyapp'):
        HOST_IP = os.environ.get('HOST_IP')
        POD_IP = os.environ.get('POD_IP')
        HOSTNAME = os.environ.get('HOSTNAME')
        return "I'm from Python Middleware Application" + '            ' + "My HostName is {}".format(HOSTNAME) + '          ' + "My POD IP is {}".format(POD_IP) + '            ' + "My Host IP Is {}".format(HOST_IP)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
