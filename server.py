# import main Flask class, then jsoniy and requet object
from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.exceptions import MethodNotAllowed


# create the flask app
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", strict_slashes=False)
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
        return jsonify(my_dict)
    else:
        raise MethodNotAllowed

if __name__ == "__main__":
        app.run(debug=True)