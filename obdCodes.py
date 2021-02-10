import bt
def connectOBD(targetName):
    bt.connect(targetName)
    bt.sendMsg('ATH0\r') #disable headers

def getSpeed():
    response = sendOBDCode('010d\r',1)
    return response

def getRPM():
    response = sendOBDCode('010c\r',2)
    return response/4 # rpm is divided by 4

def sendOBDCode(code, noBytes):
    response = bt.sendMsg(code)
    bt.sock.recv(32) # trim bytes
    responseProcessed = parseResponse(noBytes, response)
    return int(responseProcessed, 16)

def parseResponse(noBytes, response):
    toReturn = response[4:4+(noBytes*2)]
    return toReturn
