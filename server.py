"""
The server program that receives an image from a POST request.
It saves the image locally and detects the face using opencv
"""

from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def index():
    return 'This is the index page. Change this soon'


@app.route('/image', methods=['POST'])
def detect_face():
    print(request.form)
    return 'OK'


app.run(debug=True)
