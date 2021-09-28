import RPi.GPIO as gpio
import smtplib, ssl
from time import sleep as sl

gpio.setmode(gpio.BCM)
gpio.setup(21, gpio.IN)

prev=0
state=0

pwd="SenderPWD"

context=ssl.create_default_context()

def send_state(state):
    msg='open.' if state==0 else 'closed.'
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login("sender@gmail.com", pwd)
    server.sendmail("sender@gmail.com", "receiver@hotmail.com", "The door is "+msg)

def detect():
    global  prev, state
    while True:
        state=gpio.input(21)
        if state==0 and state!=prev:
                send_state(state)
                prev=state
        if state==1 and state!=prev:
                send_state(state)
                prev=state
