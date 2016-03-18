# -*- coding: utf-8 -*-
import socket
import json
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser

class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        adress = ('localhost', 9998)
        self.connection.connect(adress)
        MessageReceiver.daemon.__init__
        self.running = True
        self.run()

    def run(self):
        # Initiate the connection to the server
        while self.running:
            Client.interface(self)

    def disconnect(self):

        # TODO: Handle disconnection
        self.connection.close()
        self.running = False
        print("Du er nå logget av")

    def receive_message(self, message):

        MessageParser.parse(message)


    def send_payload(self, data):

        self.connection.send(data)
        pass

    def msg(self, brukerinput):
        msg = Client.jsonconv(self, brukerinput, "msg")
        self.send_payload(msg)

    def send_help(self):
        self.send_payload(self.jsonconv('help',None ))

    def login(self, login, username):
        self.send_payload((self.jsonconv(login, username)))

    def jsonconv(self, request, content):

        temp = {'Request': request, 'Content': content}
        output = json.dumps({'Request': request, 'Content': content}, indent=4, separators=(',', ': '))
        return output

    def interface(self):
        
        brukerinput=raw_input("Hva vil du gjøre?")
        if brukerinput == "help":
            self.send_help()
        elif brukerinput == "name":
            pass
        elif brukerinput == "login":
            brukernavn = raw_input("Ditt brukernavn?")
            self.login(brukerinput, brukernavn)
        elif brukerinput == "msg":
            beskjed = raw_input("Hva er din beskjed?")
            self.msg(brukerinput, beskjed)

        elif brukerinput == "logout":
            self.disconnect()
            output = None
        else:
            print("Dette er ikke en lovelig kommando")
            output = None





if __name__ == '__main__':

    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)
