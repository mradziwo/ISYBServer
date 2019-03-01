from flask import Flask
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

@app.route('/relay<number>')
def set_relay(number):
    return('relay'+str(numner))

if __name__ == '__main__':
   app.run(debug = True, port=5000, host='0.0.0.0')