# basic server for the sandbox

from bottle import Bottle, run

# import sandbox modules
import FremontBridgeCount as FBC


def hello():
    return "Hello World!"

def setup_routing(app):
    app.route('/hello', 'GET', hello)

    # sandbox module routes
    app.route('/fremontBridge', 'GET', FBC.getFremontBridge)


# setup and run the app
myapp = Bottle()
myapp.config.load_config('bottleapp.config')
setup_routing(myapp)
run(myapp, host='localhost', port=8080)
