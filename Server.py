# -*- coding: utf-8 -*-
import SocketServer
import json
import datetime
from string import digits


"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""

loggedinlist = ''

class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """
    def __init__(self):
        self.client_name = 0

    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request

        # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096)
            
            # TODO: Add handling of received payload from client
            if self.connection.data["Request"] == "login":
                time = datetime.datetime.now()
                username = 'Server'
                
                if self_client_name != 0:
                    response = 'Error'
                    content = 'You are already logged in'
                elif self.connection.data["Content"] in loggedinlist:
                    response = 'Error'
                    content = 'Username taken'
                else:
                    un = self.connection.data["Content"]
                    if un.isalnum():
                        loggedinn.append(self.connection.data["content"])
                        response = 'Info'
                        content = 'Loggin successful'
                        self.client_name = str(self.connection.data["content"])
                        # Send history
                    else:
                        response = 'Error'
                        content = 'Username must be one ord containing only letters and numbers'

            elif self.connection.data["Request"] == "logout":
                time = datetime.datetime.now()
                username = 'Server'
                if self.client_name == 0:
                    response = 'Error'
                    content = 'You are not logged in'
                else:
                    response = 'Info'
                    content = 'You are now logged out'
                    loggedinlist.remove(self.client_name)
                    self.client_name = 0

            elif self.connection.data["Request"] == "msg":
                time = datetime.datetime.now()
                if self.client_name == 0:
                    username = 'Server'
                    response = 'Error'
                    content = 'You are not logged in'
                else:
                    username = self.client_name
                    response = 'Message'
                    content = self.connection.data["Content"]
                    # History = History + str(username) + ': ' + str(self.connection.data["content"]) + '\n'


            elif self.connection.data["Request"] == "names":
                time = datetime.datetime.now()
                username = 'Server'
                if self.client_name == 0:
                    response = 'Error'
                    content = 'You are not logged in'
                else:
                    response = 'Info'
                    content = 'The names logged in are: ' + str(loggedinlist)

            elif self.connection.data["Request"] == "help":
                time = datetime.datetime.now()
                username = 'Server'
                response = 'Info'
                content = 'Send help'

            else:
                time = datetime.datetime.now()
                username = 'Server'
                response = 'Error'
                content = 'Request is invalid'
            
            out = jsonconv(time, username, response, content)
                

    def jsonconv(self, time, username, response, content):
        
        temp = {'Timestamp': time, 'Sender': username, 'Response': response, 'Content': content}
        output = json.dumps(temp,indent=4, separators=(',', ': '))
        
        return output


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations are necessary
    """
    allow_reuse_address = True

if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations are necessary
    """
    HOST, PORT = 'localhost', 9998
    print 'Server running...'

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
