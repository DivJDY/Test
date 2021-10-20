from flask import Flask,jsonify

app = Flask(__name__)

# @app.route('/json', methods=['POST', 'GET'])
# def test_json():
#     return '{"code": 1, "message": "Hello, World!" }'


# st=[
#     {"code": 1, "message": "Hello, World!" },

#     {"id":2,"name":"Divya"}
# ]

file="/home/aspldev2/Desktop/POstman_Collection/file.json"

# @app.route('/json', methods=['POST', 'GET'])
# def test_json():
#     return jsonify(st)

# @app.route('/', methods=['GET'])
# def son():
#     return jsonify(st)




@app.route('/json', methods=['POST', 'GET'])
def test_json():
    return jsonify(file)


if __name__=='__main__':
    app.run(debug=True)