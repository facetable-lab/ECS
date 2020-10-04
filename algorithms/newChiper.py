alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

text = input('Enter you text for encrypt: ')
key = input('Enter key: ')


def keyToText(text, key):
    keyFinaly = ''
    counter = 0
    massLetters = keyToMassive(key)
    while counter <= len(text):
        keyFinaly += massLetters[counter]
        counter += 1
        if counter >= len(massLetters):
            counter = 0
        if len(keyFinaly) == len(text):
            break

    return keyFinaly


def keyToMassive(key):
    mass = []
    for letter in key:
        mass += letter
    return mass


def getNumbersOfText(text):
    numbersText = []
    for letter in text:
        numbersText.append(alphabet.find(letter) + 1)
    return numbersText


def getNumbersOfKey(key):
    numbersKey = []
    for letter in key:
        numbersKey.append(alphabet.find(letter) + 1)
    return numbersKey


def encodeMsg(text, key):
    text.lower()
    a = keyToText(text, key)
    c = getNumbersOfText(text)
    d = getNumbersOfKey(a)
    sum = []
    encodeMessage = ''
    for i in range(len(text)):
        sum.append(c[i] + d[i])
    for i in range(len(text)):
        encodeMessage = encodeMessage + alphabet[sum[i] - 1]
    print(c)
    print(d)
    return encodeMessage


def decodeMsg(encText, key):
    encText.lower()
    a = keyToText(encodeMsg(text, key), key)
    c = getNumbersOfText(encodeMsg(text, key))
    d = getNumbersOfKey(a)
    deSum = []
    decodeMessage = ''
    counter = 0
    for i in range(len(encText)):
        deSum.append(c[i] - d[i])
    for i in encText:
        if alphabet.find(i) != -1:
            decodeMessage = decodeMessage + alphabet[deSum[counter] - 1]
        else:
            decodeMessage += i
        counter += 1

    print(c)
    print(d)
    return decodeMessage


end = encodeMsg(text, key)
dec = decodeMsg(text, key)
print('Encoded msg: ', end)
print('Decoded msg: ', dec)
