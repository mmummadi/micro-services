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
    return "No Home Page for Python Application" + '           ' + "Access with context path either /goweb or /pyweb"

@app.route('/<path:text>')
def web(text):
    GOBACKEND = os.environ.get("GO_BACKEND")
    PYBACKEND = os.environ.get("PY_BACKEND")
    if text.startswith('goweb'):
        return requests.get(GOBACKEND).content
    elif text.startswith('pyweb'):
        return requests.get(PYBACKEND).content
    elif text.startswith('goapp'):
        return requests.get(GOBACKEND + "goapp").content
    elif text.startswith('pyapp'):
        return requests.get(PYBACKEND + "pyapp").content
    else:
        return "Not a Right Context, Access with context path either /goweb or /pyweb"


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
