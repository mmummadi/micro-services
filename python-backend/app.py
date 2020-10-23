from typing import List, Dict
import requests
from flask import Flask, render_template, request, session, redirect, url_for
import json
import os
from http.server import SimpleHTTPRequestHandler, HTTPServer

app = Flask(__name__)

@app.route('/')
def home():
    HOST_IP = os.environ.get('HOST_IP')
    POD_IP = os.environ.get('POD_IP')
    HOSTNAME = os.environ.get('HOSTNAME')
    return "I'm from Python Application" + '            ' + "My HostName is {}".format(HOSTNAME) + '          ' + "My POD IP is {}".format(POD_IP) + '            ' + "My Host IP Is {}".format(HOST_IP)

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
