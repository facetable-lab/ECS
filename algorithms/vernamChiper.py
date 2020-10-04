import random

alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
messageIn = input()
key = []
i = 0
messageEnc = []
#generate key
while i < len(messageIn):
    key.append(random.randrange(0, 26))
    i += 1


def encodeMessage(messageIn, key):
    encodedMsg = ''
    counter = 0
    messageIn = messageIn.lower()
    for letter in messageIn:
        if alphabet.find(letter) != -1:
            let = alphabet.find(letter)
            encodedMsg = encodedMsg + alphabet[let + key[counter]]
        else:
            encodedMsg += letter
        counter += 1
    return encodedMsg

def decodeMessage(messageEnc, key):
    decodedMsg = ''
    counter = 0
    # messageEnc.lower()
    for letter in messageEnc:
        if alphabet.find(letter) != -1:
            let = alphabet.find(letter)
            decodedMsg = decodedMsg + alphabet[let - key[counter]]
        else:
            decodedMsg += letter
        counter += 1
    return decodedMsg


print(key)
encodedMsg = encodeMessage(messageIn, key)
print('Encoded message: ', encodedMsg)
print('Decoded message: ', decodeMessage(encodedMsg, key))