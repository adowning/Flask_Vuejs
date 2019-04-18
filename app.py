import os
from flask import render_template,request
from flask import Flask, jsonify
from flask_cors import CORS


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


# sanity check route
@app.route('/', methods=['GET'])
def index():
    # return jsonify('pong!')
    return render_template('index.html')
    
@app.route('/result', methods=['POST','GET'])
def res():
    # if request.method == 'POST':
    #     result = request.t
    #     return render_template("result.html",result = result)
    if request.method == 'GET':
        return render_template("result.html")


if __name__ == '__main__': 
	app.run(debug=True, host='127.0.0.1')


# app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))