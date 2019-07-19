from telnetlib import Telnet
from restunl.helper import *

class Device(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return type(self).__name__ + '(' + self.name + ')'

    def to_json(self):
        return self.__dict__


class Router(Device):
    defaults = {
        "type":"qemu","template":"vios","config":"Unconfigured","delay":0,"icon":"Router.png",
        "image":"vios-adventerprisek9-m-15.5.3M","name":"Core Router 1","left":"35%","top":"25%",
        "ram":"1024","console":"telnet","cpu":1,"ethernet":2,"uuid":"641a4800-1b19-427c-ae87-4a8ee90b7790"
    }

    def __init__(self, name):
        for key, value in Router.defaults.items():
            setattr(self, key, value)
        super(Router, self).__init__(name)
        self.url_ip, self.url_port = '', ''

    def set_url(self, url):
        self.url_ip, self.url_port = str(url).strip('telnet://').split(':')
        return None

    def send_config(self, config):
        session = Telnet(self.url_ip, self.url_port)
        send_and_wait(session, '\r\n')
        result = send_and_wait(session, config)
        session.close()
        return result