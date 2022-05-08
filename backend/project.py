import base64
import datetime
import json
import uuid
import logging
import os

from flask import Flask 

from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

APP_PORT = os.environ.get("APP_PORT", 5000)


@app.route("/")
def index():
    return dict(os.environ)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
