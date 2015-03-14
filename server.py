# basic server for the sandbox

from bottle import Bottle, run
import FreemontBridgeCount as FBC


def hello():
    return "Hello World!"

def setup_routing(app):
    app.route('/hello', 'GET', hello)
    app.route('/freemontBridge', 'GET', FBC.getFreemontBridgeData)


myapp = Bottle()
setup_routing(myapp)
run(myapp, host='localhost', port=8080)
