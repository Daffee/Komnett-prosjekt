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
        self.host = 'localhost'
        self.server_port=9998


        # TODO: Finish init process with necessary code
        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))
        
    def disconnect(self):
        # TODO: Handle disconnection
        self.connection.close()
        # print: something
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

    def jsonconv(self, string, request):

        temp = {}
        temp
        output = json.dump(temp,indent=4, separators=(',', ': '))
        return output
        pass

    def stringconv(self, json):

        output = ""




if __name__ == '__main__':
    
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)
