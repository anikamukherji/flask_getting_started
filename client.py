import requests

def call_apis():
    """
    Calls each api and returns a list of their requests

    :return: list of api requests
    :rtype: list
    """
    name_r = requests.get("http://vcm-3576.vm.duke.edu:5000/name")
    hello_r = requests.get("http://vcm-3576.vm.duke.edu:5000/hello/"
                           "{}".format("Anika"))
    points = {"a": [0, 1], "b": [4, 1]}
    dist_r = requests.post("http://vcm-3576.vm.duke.edu:5000/distance",
                           json=points)
    return [name_r, hello_r, dist_r]

def print_api_returns(rets):
    """
    Prints out the json attributes of a list of requests
    """
    for r in rets: print(r.json())

if __name__ == "__main__":
    rets = call_apis()
    print_api_returns(rets)
