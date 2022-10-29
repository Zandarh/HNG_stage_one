# import main Flask class, then jsoniy and requet object
from flask import Flask, request
from werkzeug.exceptions import MethodNotAllowed


# create the flask app
app = Flask(__name__)

@app.get("/")
def my_data():
    """Returns my data"""
    # checking if the http method is Get
    if request.method == "GET":
        my_dict = {
            "slackUsername": "zandarh",
            "backend": True,
            "age": 30,
            "bio": "I am an aspiring software engineer"
            }
        return (my_dict)
    else:
        raise MethodNotAllowed
