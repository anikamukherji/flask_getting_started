from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/name', methods=["GET"])
def name():
    """
    Returns name dictionary to call as JSON

    :return: json dictionary with key "name"
    :rtype: dict
    """
    data = {
            'name': 'Anika',
            }
    return jsonify(data), 200

@app.route('/hello/<name>', methods=["GET"])
def hello(name):
    """
    Returns greeting with given name

    :return: json dictionary with key "message"
    :rtype: dict
    """
    data = {
            "message": "Hello there, {}".format(name)
            }
    return jsonify(data), 200

@app.route("/distance", methods=["POST"])
def distance():
    """
    Returns cartesian difference between two points
    Provided a dict containing 2 points, "a" and "b"

    :return: json dictionary with key "distance"
    :rtype: dict
    """
    r = request.get_json() # parses the POST request body as JSON
    point_a = r["a"]
    point_b = r["b"]
    dist = dist_helper(point_a[0], point_a[1], point_b[0], point_b[1])
    d = {"distance": dist}
    return jsonify(d), 200


def dist_helper(x1, y1, x2, y2):
    """
    Returns cartesian difference between two points

    :param x1: x value of point a
    :type x1: int
    :param y1: y value of point a
    :type y1: int
    :param x2: x value of point b
    :type x2: int
    :param y2: y value of point b
    :type y2: int

    :return: distance between points
    :rtype: float
    """
    from math import sqrt
    s = (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1)
    return sqrt(s)

if __name__ == "__main__":
    app.run()
