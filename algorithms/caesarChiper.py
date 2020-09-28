alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

#This function encode the message
def encodeMessage(text, key):
    encodedMsg = ''
    for letter in text:
        if alphabet.find(letter) != -1:
            let = alphabet.find(letter)
            encodedMsg = encodedMsg + alphabet[let + key]
        else:
            encodedMsg += letter
    return encodedMsg

#This function decode the message mjqqt, rd sfrj nx irnywd
def decodeMessage(encMsg, key):
    decodedMsg = ''
    for letter in encMsg:
        if alphabet.find(letter) != -1:
            let = alphabet.find(letter)
            decodedMsg = decodedMsg + alphabet[let - key]
        else:
            decodedMsg += letter
    return decodedMsg


answer = int(input('Code/Decode (1 or 0): '))

if answer == 1:
    text = input('Input text for code: ')
    key = int(input('Enter key(2-26): '))
    msg = encodeMessage(text, key)
    print('Your coded message:', msg)
elif answer == 0:
    text = input('Input text for decode: ')
    key = int(input('Enter key(2-26): '))
    msg = decodeMessage(text, key)
    print('Your decoded message:', msg)
else:
    print('Incorrect answer')
