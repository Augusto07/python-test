import requests


def get_request(endpoint):

    r = requests.get(endpoint)
    j = r.json()
    j = dict(j)
    return j



