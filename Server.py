# -*- coding: utf-8 -*-
import SocketServer
import json
import datetime


"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""

History = ''
loggedinlist = ''

class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Everytime a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """
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
            if self.connection.data["request"] == "login":
                time = datetime.datetime.now()
                username = 'Server'
                
                if self_client_name != 0:
                    respons = 'Error'
                    content = 'You are already logged in'
                elif self.connection.data["content"] in loggedinlist:
                    respons = 'Error'
                    content = 'Username taken'
                else:
                    loggedinn.append(self.connection.data["content"])
                    respons = 'Info'
                    content = 'Loggin successful'
                    self.client_name = str(self.connection.data["content"])

            elif self.connection.data["request"] == "logout":
                time = datetime.datetime.now()
                username = 'Server'
                    if self.client_name == 0:
                        respons = 'Error'
                        content = 'You are not logged in'
                    else:
                        response = 'Info'
                        content = 'You are now logged out'
                        loggedinlist.remove(self.client_name)
                        self.client_name = 0

            elif self.connection.data["request"] == "msg":
                time = datetime.datetime.now()
                if self.client_name == 0:
                    username = 'Server'
                    respons = 'Error'
                    content = 'You are not logged in'
                else:
                    username = self.client_name
                    respons = 'Message'
                    content = self.connection.data["content"]
                    History = History + str(username) + ': ' + str(self.connection.data["content"]) + '\n'


            elif self.connection.data["request"] == "names":
                time = datetime.datetime.now()
                username = 'Server'
                if self.client_name == 0:
                    respons = 'Error'
                    content = 'You are not logged in'
                else:
                    respons = 'Info'
                    content = 'The names logged in are: ' + str(loggedinlist)

            elif self.connection.data["request"] == "help":
                time = datetime.datetime.now()
                username = 'Server'
                respons = 'Info'
                content = 'Send help'

            else:
                time = datetime.datetime.now()
                username = 'Server'
                respons = 'Error'
                content = 'Request is invalid'
            
            out = tojson(time, username, respons, content)

    
    
    def tojson(time, username, respons, content):
        output = '{\n "timestamp":<' + str(time) + '>,\n "sender":<' + str(username) + '>,\n "respons":<' + str(respons) + '>,\n "content":<' + str(content) + '>,\n }'
        return output
    def fromjson(input):




# Time:
# import datetime
# time = datetime.datetime.now()


# import time
# ts = time.time()
# import datetime
# st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
# st = 2012-12-15 01:21:05



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
