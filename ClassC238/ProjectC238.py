import hashlib

#Initializing string.
text = 'TestText'
textOne = 'TestTextOne'
textTwo = 'TestTextTwo'

#Enconding string using encode.
#Sending it to SHA256.
result = hashlib.sha3_256(text.encode())
resultOne = hashlib.sha3_256(textOne.encode())
resultTwo = hashlib.sha3_256(textTwo.encode())

#Printing SHA256 value.
print('SHA256 Value Zero is: ', result.hexdigest())
print('SHA256 Value One is: ', result.hexdigest())
print('SHA256 Value Two is: ', result.hexdigest())