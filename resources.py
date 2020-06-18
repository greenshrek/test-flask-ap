import json
import base64
from collections import defaultdict

import requests
from flask import request
from flask_restful import Api, Resource

class Image(Resource):
    def __init__(self):
        self.text = ""

    def get(self):
        return "I am alive", 200

    def post(self):
        """
        Processes the image, picks and answer and sends it back
        """
        args = request.json
        print("args are--->",args["image_name"])
        imgdata = base64.b64decode(args["image_file"])
        filename = args["image_name"]
        with open(filename, 'wb') as f:
            f.write(imgdata)

        return args["image_file"], 200