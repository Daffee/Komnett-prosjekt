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

        adress = ('localhost', 9997)
        self.connection.connect(adress)

        self.running = True


        # TODO: Finish init process with necessary code
        self.run()

    def run(self):
        # Initiate the connection to the server
        while self.running:

            output = Client.interface(self)

            self.connection.send(output)
            running = False


    def disconnect(self):

        # TODO: Handle disconnection
        self.connection.close()
        running = False
        print("Du er nå logget av")
        pass

    def receive_message(self, message):
        self.connection.recv(4098)
        # TODO: Handle incoming message
        pass

    def send_payload(self, data):
        # TODO: Handle sending of a payload
        pass
        
    # More methods may be needed!

    def msg(self):
        pass

    def send_help(self):
        pass

    def login(self):
        pass

    def jsonconv(self, content, request):


        temp = {'Request': request, 'Content': content}
        output = json.dumps({'Request': request, 'Content': content}, indent=4, separators=(',', ': '))
        return output
        pass

    def stringconv(self, json):

        output = ""
        
    def interface(self):
        
        brukerinput=input("Hva vil du gjøre?")
        if brukerinput == "help":
            output=Client.jsonconv(self, None, "help")
        elif brukerinput == "name":
            output=Client.jsonconv(self, None, "name")
        elif brukerinput == "login":
            brukerinput = input("Ditt brukernavn?")
            output=Client.jsonconv(self, brukerinput, "login")
        elif brukerinput == "msg":
            brukerinput = input("Hva er din beskjed?")
            output = Client.jsonconv(self, brukerinput, "msg")
        else:
            print("Dette er ikke en lovelig kommando")
            output = None
        
        return output




if __name__ == '__main__':

    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9997)
