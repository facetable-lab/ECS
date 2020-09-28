alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

text = input()
key = input()

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
    a = keyToText(text, key)
    b = keyToMassive(key)
    c = getNumbersOfText(text)
    d = getNumbersOfKey(a)
    print(a)
    print(b)
    print(c)
    print(d)
    
end = encodeMsg(text, key)
print(end)
