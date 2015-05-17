from flask import Flask, request, redirect
from dailycred import DailyCred
import yaml

app = Flask(__name__)

config = yaml.load(open('./config.yaml'))
dailycred = DailyCred(config['dailycred']['client_id'],
                      config['dailycred']['secret'])

GATEWAY_URL = config['wifidog']['gateway_url']


@app.route('/ping/')
def ping():
    return 'Pong'


@app.route('/login/')
def login():
    # redirect to dailycred
    return redirect(dailycred.get_auth_url())


@app.route('/success_login/')
def success_login():
    # get the access token
    token = dailycred.exchange_token(request.args.get('code'))

    if not token:
        return "Cannot exchange token"

    # return to the gateway with token
    return redirect(GATEWAY_URL +
                    "/wifidog/auth?token={}".format(token))


@app.route('/auth/')
def auth():
    stage = request.args.get('stage')
    if stage == 'login':
        user = dailycred.get_me(request.args.get('token'))
        if user:
            return "Auth: 1"
        return "Auth: 0"
    else:
        return ""


@app.route('/portal/')
def portal():
    return "Welcome"

if __name__ == '__main__':
    app.run(debug=config['debug'])
