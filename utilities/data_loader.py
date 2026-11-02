import json


def read_test_data():
    with open("test_data/login_details.json") as f:
        test_data=json.load(f)
        return test_data
