from flask import Flask
from flask import request
import os
import socket



app = Flask(__name__)

@app.route("/")
def hello():

    html = "<h3>Information about app</h3>" \
 		   "<h4>Updated line!!!</h4>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>IstanceID:</b> {instanceid}"
    return html.format(hostname=request.host, instanceid=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
