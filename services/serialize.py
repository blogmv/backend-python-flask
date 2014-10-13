try:
    import json
except ImportError:
    import simplejson as json


__author__ = 'fernando'

class JSONSerializable(object):
    def toJSON(self):
        raise NotImplementedError("Implement JSONSerializable.toJSON")


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, JSONSerializable):
            return obj.toJSON()
        return json.JSONEncoder.default(self, obj)

def serialize(result):
    if not result and not isinstance(result, list):
        return "", 404, {"Content-Type": "application/json"}
    return json.dumps(result, cls=JSONEncoder), 200, {"Content-Type": "application/json"}