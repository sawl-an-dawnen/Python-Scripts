hexNumbers = {
    '0' : 0, '1' : 1,'2' : 2,'3' : 3,'4' : 4,'5' : 5,'6' : 6,'7' : 7,'8' : 8,'9' : 9,
    'A' : 10,'B' : 11,'C' : 12,'D' : 13,'E' : 14,'F' : 15
}

def hexToDec(hexNum):
    '''''
    i = 0
    while i < len(hexNum):
        print(hexNum[i])
        i += 1
    '''
    dec = ''
    i = 0
    while i < len(hexNum):
        if hexNum[i] not in hexNumbers:
            return "INVALID INPUT"
        dec = dec + str(hexNumbers[hexNum[i]])
        i += 1
    return dec

print(hexToDec('1AB3D'))
print(hexToDec('91546A'))

def hexToDec_Rec(hexNum):
    return str(hexToDec_Rec(hexNum[0:len(hexNum)-1])) + str(hexNumbers[hexNum[len(hexNum)-1]]) if hexNum != '' else ''

print(hexToDec_Rec('91546A'))
print(hexToDec_Rec('1AB3D'))


