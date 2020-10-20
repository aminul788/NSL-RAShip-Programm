'''
    Date  : 20/10/2020
    Day   : Tuesday
    Author: Md. Aminul Islam
    Topic : Logic Gates
'''

### this is super class LogicGate
class LogicGate:
    
    def __init__(self, n):
        self.label = n
        self.output = None
    
    def getLabel(self):
        return self.label
    
    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output



### BinaryGate a subclass of LogicGate
class BinaryGate(LogicGate):
    
    def __init__(self, n):
        super(BinaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None
    
    # def getPinA(self):
    #     return int(input("Enter Pin A input for gate " + self.getLabel() + "--> "))

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"--> "))
        else:
            return self.pinA.getFrom().getOutput()
    
    # def getPinB(self):
    #     return int(input("Enter Pin B input for gate " + self.getLabel() + "--> "))

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + "--> "))
        else:
            return self.pinB.getFrom().getOutput()
    
    def setNextPin(self, source):
        if self.pinA  == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                # raise RuntimeError ("Error: NO EMPTY PINS")
                print("Cannot Connect: NO EMPTY PINS on this gate")



### UnaryGate a subclass of LogicGate
class UnaryGate(LogicGate):

    def __init__(self, n):
        LogicGate.__init__(self, n)

        self.pin = None
    
    # def getPin(self):
    #     return int(input("Enter Pin input for gate " + self.getLabel() + "-->"))

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate " + self.getLabel() + "--> "))
        else:
            return self.pin.getFrom().getOutput()
    
    def setNextPin(self, source):
        if self.pin  == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")
    



### AndGate a subclass of BinaryGate
class AndGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 1 and b == 1:
            return 1
        else:
            return 0

### OrGate a subclass of BinaryGate
class OrGate(BinaryGate):

    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()

        if a == 0 and b == 0:
            return 0
        else:
            return 1

### NotGate a subclass of UnaryGate
class NotGate(UnaryGate):

    def __init__(self, n):
        UnaryGate.__init__(self,n)
    
    def performGateLogic(self):
        a = self.getPin()

        if a == 0:
            return 1
        else:
            return 0


### NandGate a subclass of AndGate
class NandGate(AndGate):
    
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1

### NorGate a subclass of OrGate
class NorGate(OrGate):
    
    def performGateLogic(self):
        if super().performGateLogic() == 1:
            return 0
        else:
            return 1


### Connector class (HAS-A Relationship)
class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
    
        tgate.setNextPin(self)
    
    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate
    


def main():

    g1 = AndGate("G1")
    g2 = AndGate("G2")
    g3 = OrGate("G3")
    g4 = NotGate("G4")
    g5 = NandGate("G5")
    c1 = Connector(g1,g3)
    c2 = Connector(g2,g3)
    c3 = Connector(g3,g4)
    c4 = Connector(g4,g5)
    print(g5.getOutput())

    # g5 = NandGate("G5")
    # print(g5.getOutput())

main()