from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/name', methods=["GET"])
def name():
    """
    Returns name dictionary to call as JSON
    """
    data = {
            'name': 'Anika',
            }
    return jsonify(data), 200

@app.route('/hello/<name>', methods=["GET"])
def hello(name):
    """
    Returns greeting with given name
    """
    data = {
            "message": "Hello there, {}".format(name)
            }
    return jsonify(data), 200

@app.route("/distance", methods=["POST"])
def distance():
    """
    Returns cartesian difference between two points
    """
    from math import sqrt
    r = request.get_json() # parses the POST request body as JSON
    point_a = r["a"]
    point_b = r["b"]
    y_dist_squared = (point_a[1] - point_b[1])(point_a[1] - point_b[1])
    x_dist_squared = (point_a[0] - point_b[0])(point_a[0] - point_b[0])
    d = sqrt(y_dist_squared + x_dist_squared)
    return d, 200

if __name__ == "__main__":
    app.run()
