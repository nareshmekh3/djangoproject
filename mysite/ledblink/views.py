
import serial
#arduino = serial.Serial('/dev/ttyACM0',9600)

def led(request):
        result=''
        if 'door-open' in request.POST:
            #arduino.write('1')
	    result='door open'
	    return render(request,'index.html',{'result':result})
            #return render(request,'led.html',{'result':result})
        elif 'door-close' in request.POST:
            #arduino.write('2')
	    result='door close'
            return render(request,'index.html',{'result':result})
            #return render(request,'led.html',{'result':result})



