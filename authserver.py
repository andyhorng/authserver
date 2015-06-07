from flask import Flask, request, redirect
from dailycred import DailyCred
import yaml

app = Flask(__name__)

config = yaml.load(open('./config.yaml'))
dailycred = DailyCred(config['dailycred']['client_id'],
                      config['dailycred']['secret'])

LOGIN_URL = config['wifidog']['login_url']
GATEWAY_URL = config['wifidog']['gateway_url']
LANDING_PAGE_URL = config['wifidog']['landing_page_url']


@app.route('/ping/')
def ping():
    return 'Pong'


@app.route('/login/')
def login():
    # redirect to dailycred
    return redirect(LOGIN_URL)


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
    return redirect(LANDING_PAGE_URL)

if __name__ == '__main__':
    app.run(debug=config['debug'], port=9666, host='0.0.0.0')
