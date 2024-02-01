from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/howdy', methods=['GET'])
def test_hello():
    return jsonify({'howdy': "Hello World!"})



if __name__ == "__main__":
    app.run(debug=True)