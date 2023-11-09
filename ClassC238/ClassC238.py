import hashlib

#Initializing string.
text = 'TestTextOne'

#Enconding string using encode.
#Sending it to SHA256.
result = hashlib.sha3_256(text.encode())

#Printing SHA256 value.
print('SHA256 Value is: ', result.hexdigest())