from urllib import urlencode
from urllib2 import urlopen
import json


class DailyCred(object):

    def __init__(self, client_id, secret):
        self.client_id = client_id
        self.secret = secret

    def exchange_token(self, code):
        endpoint = 'https://www.dailycred.com/oauth/access_token'

        data = urlencode({
            "code": code,
            "client_secret": self.secret
            })
        response = urlopen(endpoint, data).read()
        response = json.loads(response)

        if 'worked' not in response or not response['worked']:
            return False

        return response['access_token']

    def get_me(self, token):
        user = DailyCredUser(token)

        if not user:
            return False

        return user.me()

    def get_auth_url(self):
        return ("https://www.dailycred.com/oauth/gateway?"
                "client_id={}".format(self.client_id))


class DailyCredUser(object):
    def __init__(self, token):
        self.token = token

    def me(self):
        endpoint = 'https://www.dailycred.com/graph/me.json'

        data = urlencode({
            'access_token': self.token
            })
        response = urlopen(endpoint, data).read()
        response = json.loads(response)

        if 'worked' in response and not response['worked']:
            return False

        return response

    def set(self, attr, value):
        endpoint = 'https://www.dailycred.com/attribute/set'

        data = urlencode({
            'access_token': self.token,
            'key': attr,
            'value': value
            })

        response = urlopen(endpoint, data).read()

        return json.loads(response)

    def add_tag(self, tag):
        pass

    def remove_tag(self, tag):
        pass

