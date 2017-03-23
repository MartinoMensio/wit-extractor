import requests

class Extractor:
    def __init__(self, token):
        self.token = token
        self.headers = {'Authorization':'Bearer {0}'.format(token)}

    def parse(self, sentence):
        params = {'q':sentence}
        response = requests.get("https://api.wit.ai/message", params = params, headers = self.headers).json()
        # TODO check for errors

        intent = response["entities"]["intent"][0];
        del response["entities"]["intent"]
        entities = response["entities"]

        return intent, entities

def foo():
    print("hi")
