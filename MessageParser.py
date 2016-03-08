import json

class MessageParser():
    def __init__(self):

        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            'message': self.parse_message,
            'history': self.parse_history,	
        }

    def parse(self, payload):
        payload = json.loads(payload)

        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            # Response not valid

    def parse_error(self, payload):
        error_msg = payload['content']
        #return eller print
    def parse_info(self, payload):
        info_msg = payload['content']
        #return eller print
    def parse_message(self, payload):
        msg = payload['content']
        #return eller print
    def parse_history(self, payload):
        history_list = payload['content']
        length = len(history_list)
        for i in range(0,length):
            msg = json.loads(history_list(i))
            #Return eller print
