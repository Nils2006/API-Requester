import json
import requests


def make_api_request(url, method, route, body):
    if method == "POST":
        response = requests.post(url + route, json=body)
    elif method == "GET":
        response = requests.get(url + route, params=body)
    # Add support for other request methods as needed

    # Print the response status code and content
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}\n")


def scan_json_file(filename):
    with open(filename, "r") as file:
        data = json.load(file)

    url = data["url"]
    requests = data["requests"]

    for request in requests:
        method = request["type"]
        route = request["route"]
        body = request["body"]

        make_api_request(url, method, route, body)


# Specify the path to your JSON file
json_file = "requests.json"

scan_json_file(json_file)
