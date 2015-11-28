
import os, subprocess, yowsup #, logging
from wasend import YowsupSendStack
from wareceive import YowsupReceiveStack, MessageReceived
from yowsup.demos import sendclient

def credential():
     return "59167479531", "kgWT7zbZhFxGEl/fJoVGwn/Kzbw="

def Answer(risp, phone):
    print '**************************'
    print 'Phone: ' + phone
    print 'Message: ' + risp
    print '**************************'
    try:
        stack = YowsupSendStack(credential(), [([phone, risp])])
        stack.start()
    except:
        pass
    return

def UpdateFunc():
    Answer("Updating...")
    os.system("sudo apt-get -y update")
    Answer("System updated!")
    return

def RestartFunc():
    Answer("Restarting the system...")
    os.system("sudo reboot")
    return

def TempFunc():
    t=float(subprocess.check_output(["/opt/vc/bin/vcgencmd measure_temp | cut -c6-9"], shell=True)[:-1])
    ts=str(t)
    Answer("My temperature is "+ts+" grados C")
    return

while True:
    try:
        stack=YowsupReceiveStack(credential())
        stack.start()
    except MessageReceived as rcvd:
        received=rcvd.value.lower()
        print '++++++++++++++++++++++++++++++++++'
        print received
        print '++++++++++++++++++++++++++++++++++'
        phone = received[:11]
        message = received[11:]
        if received[:len("59112345678")]=="59168510583":
            received=received[len("39000000000"):]
            print '---------------------------------'
            print received
            print '---------------------------------'
            if received[:11]=="hola":
                print '======================='
                print 'entro en el hola'
                print '======================='
                Answer("Hola!!! este es un mensaje automatico", phone)
            elif received[:11]=="update": UpdateFunc()
            elif received[:11]=="restart" or received[:6]=="reboot": RestartFunc()
            elif "temperature" in received: TempFunc()
            else: Answer("Sorry, I cannot understand what you are asking for...")
        else: #message from wrong sender
            Answer('Error de conexion!!!', phone)
            with open("/home/ben/tmp/whatsapp.log","a") as mf: mf.write("Wrong sender: "+received[:len("390000000000")]+"\n")

