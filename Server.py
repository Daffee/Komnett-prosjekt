# -*- coding: utf-8 -*-
import SocketServer
import json
import datetime
from string import digits


"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""
History = []
loggedinlist = []

class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    def jsonconv(self, time, username, response, content):
        
        temp = {'timestamp': time, 'sender': username, 'response': response, 'content': content}
        output = json.dumps(temp,indent=4, separators=(',', ': '))
        
        return output
    
    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.client_name = 0
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request

        # Loop that listens for messages from the client
        while True:
            rec_str = json.loads(self.connection.recv(4096))
            
            # TODO: Add handling of received payload from client
            if rec_str["request"] == "login":
                time = datetime.datetime.now()
                username = 'Server'
                
                if self.client_name != 0:
                    response = 'error'
                    content = 'You are already logged in'
                elif rec_str["content"] in loggedinlist:
                    response = 'error'
                    content = 'Username taken'
                else:
                    un = rec_str["content"]
                    if un.isalnum():
                        loggedinlist.append(rec_str["content"])
                        response = 'info'
                        content = History
                        self.client_name = str(rec_str["content"])
                    else:
                        response = 'error'
                        content = 'Username must be one ord containing only letters and numbers'

            elif rec_str["request"] == "logout":
                time = datetime.datetime.now()
                username = 'Server'
                if self.client_name == 0:
                    response = 'error'
                    content = 'You are not logged in'
                else:
                    response = 'info'
                    content = 'You are now logged out'
                    loggedinlist.remove(self.client_name)
                    self.client_name = 0

            elif rec_str["request"] == "msg":
                time = datetime.datetime.now()
                if self.client_name == 0:
                    username = 'Server'
                    response = 'error'
                    content = 'You are not logged in'
                else:
                    username = self.client_name
                    response = 'message'
                    content = rec_str["content"]


            elif rec_str["request"] == "names":
                time = datetime.datetime.now()
                username = 'Server'
                if self.client_name == 0:
                    response = 'error'
                    content = 'You are not logged in'
                else:
                    response = 'info'
                    content = 'The names logged in are: ' + str(loggedinlist)

            elif rec_str["request"] == "help":
                time = datetime.datetime.now()
                username = 'Server'
                response = 'info'
                content = 'Supported commands: login, msg, names, logout, help'

            else:
                time = datetime.datetime.now()
                username = 'Server'
                response = 'error'
                content = 'Request is invalid'
            temptime = str(time)
            timeString = temptime[0:19]
            out = self.jsonconv(timeString, username, response, content)
            self.connection.send(out)
            if response == 'message':
                History.append(out)



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
