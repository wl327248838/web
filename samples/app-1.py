from restunl.unetlab import UnlServer
from restunl.device import Router

LAB_NAME = 'test_1'

def app_1():
    unl = UnlServer('10.14.10.148')
    unl.login('admin', 'eve')
    print ("*** CONNECTED TO UNL")
    lab = unl.create_lab(LAB_NAME)
    print ("*** CREATED LAB")
    node_1 = lab.create_node(Router('R1'))
    print ("*** CREATED NODE")

if __name__ == '__main__':
    app_1()