import requests
from flask import Flask, render_template, request
from flask_restful import Api, Resource

from resources import Image

app = Flask(__name__, template_folder="templates")

# API section begins here
api = Api(app)
api.add_resource(Image, "/image")

if __name__ == "__main__":
    app.run(port="5002", debug=True)