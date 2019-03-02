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
    state = str(request.args.get('state')).lower()
    setting=None
    if state == "none":
        return('relay'+str(number)+ "   -state report   ")
    if (state=="off")|(state=="false")|(state=="clear")|(state=="reset")|(state=="0")|(state=="low"):
        setting=0
    elif (state=="on")|(state=="true")|(state=="set")|(state=="1")|(state=="high"):
        setting=1
    if setting!=None:
        return('relay- '+str(number)+ "   -   "+str(setting))
    else:
        return('relay- unknown command')

if __name__ == '__main__':
   app.run(debug = True, port=5000, host='0.0.0.0')

   from flask import request