import serial  #import serial library

arduinoSerialData  = serial.Serial('com3', 9600)

while (1==1):
    if (arduinoSerialData.inWaiting()>0):
        myData = arduinoSerialData.readline()
        print myData
