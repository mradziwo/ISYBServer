from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/version')
def return_version():
    return('0.0.1')

@app.route('/sel')
def select_relay():
    return('SelectRelay')

@app.route('/relay<int:number>')
def set_relay(number):
    state = request.args.get('state')
    return('relay- '+str(number)+ "   -   "+str(state))

if __name__ == '__main__':
   app.run(debug = True, port=5000, host='0.0.0.0')

   from flask import request