'''
Created on 31 mar 2013

@author: balp
'''

class DummyLib:
    def __init__(self):
        pass
    def tdTurnOn(self, id):
        pass
    def tdTurnOff(self, id):
        pass

class TelldusCore(object):
    def __init__(self):
        self.lib = DummyLib()
        