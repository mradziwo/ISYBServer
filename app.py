from flask import Flask, request
import serial
from serial.tools import list_ports
app = Flask(__name__)

class Connections():
    ISWYBsetialDescriptor=None
    ISWYBserial=None
    PowerSerialDescriptor=None
    PowerSerial=None

    def connectISWYB(self):
        try:
            self.ISWYBserial=serial.serial(ISWYBsetialDescriptor)
            return(True)
        except:
            self.ISWYBserial=None
            return(False)
        pass

    def connectPower(self):
        try:
            self.PowerSerial=serial.serial(PowerSerialDescriptor)
            return(True)
        except:
            self.PowerSerial=None
            return(False)
        pass
    
    def writeISWYB(self, payload):
        if self.ISWYBserial==None:
            slelf.connectISWYB()
            if self.ISWYBserial is None:
                return(False)
        try:
            self.ISWYBserial.write(payload)
            return(True)
        except:
            self.ISWYBserial.close()
            self.ISWYBserial=None
            return(False)

    def writePower(self, payload):     
        if self.PowerSerial==None:
            slelf.connectPower()
            if self.ISWYBserial is None:
                return(False)
        try:
            self.PowerSerial.write(payload)
            return(True)
        except:
            self.PowerSerial.close()
            self.PowerSerial=None   
            return(False)

    def readPower(self, n):     
        if self.PowerSerial==None:
            slelf.connectPower()
        try:
            payload=self.PowerSerial.read(n)
            return(True,payload)
        except:
            self.PowerSerial.close()
            self.PowerSerial=None   
            return(False, b'')

@app.route('/availableSerialPorts')
def availableSerialPorts():
    asp=list_ports.comports()
    reply=""
    for serialPort in asp:
        reply=reply+str(serialPort)+" VID: "+str(serialPort.vid)+" PID: "+str(serialPort.pid)+"<br>"
    return(reply)
         

@app.route('/')
def status():
    return ('ISWYB '+ str(Connections.ISWYBserial) + '<br> Power'+str(Connections.PowerSerial))

@app.route('/version')
def return_version():
    return('0.0.2')

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
