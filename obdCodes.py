import bt
def connectOBD(targetName):
    bt.connect(targetName)
    bt.sendMsg('ATH0\r') #disable headers

def getSpeed():
    response = bt.sendMsg('010d\r')
    bt.sock.recv(32)
    print('\t response', response)
    responseProcessed = parseResponse(1, response)
    print(' \t responseProcessed ', responseProcessed)
    return int(responseProcessed, 16)

def getRPM():
    response = bt.sendMsg('010c\r')
    bt.sock.recv(32);
    print('\t response', response)
    responseProcessed = parseResponse(2, response)
    print(' \t responseProcessed ', responseProcessed)
    responseNumber = int(responseProcessed, 16)
    return responseNumber/4 # rpm is divided by 4

def parseResponse(noBytes, response):
    toReturn = response[4:4+(noBytes*2)]
    return toReturn
