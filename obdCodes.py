import bt
def connectOBD(targetName):
    bt.connect(targetName)
    bt.sendMsg('ATH0\r') #disable headers

def getSpeed(speed):
    response = bt.sendMsg('010d')
    responseProcessed = parseResponse(1)
    return int(responseProcessed, 16)

def getRPM(rpm):
    response = bt.sendMsg('010c\r')
    responseProcessed = parseResponse(2)
    responseNumber = int(responseProcessed, 16)
    return responseNumber/4 # rpm is divided by 4

def parseResponse(bytes, response):
    toReturn = response[6:6+(bytes*2)]
    return toReturn
