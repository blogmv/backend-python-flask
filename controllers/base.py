__author__ = 'fernando'

class Controller(object):
    __slots__ = ["request"]
    def __init__(self, request):
        self.request = request
    def process_request(self):
        raise NotImplemented()