
from flask import Flask, request, jsonify

app = Flask(__name__)

# root
@app.route("/")
def index():
    """
    this is a root dir of my server
    :return: str
    """
    return "This is root!!!!"


# running web app in local machine
if __name__ == '__main__':
    app.run()