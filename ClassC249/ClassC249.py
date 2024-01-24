import hashlib

PB_current_hash = '573de6af99199bdc7ae9534891d512afbc2b1473f2f6a5784e0c078d67a60bf9'
str = 'Alice sends James 5 Eth amount'

result = hashlib.sha256(str.encode())
CB_previous_hash = result.hexdigest()
print(CB_previous_hash)

if PB_current_hash == CB_previous_hash:
	print('Hash is verifed.')

else:
	print('Hash is not verified.')

#773f73363352cb8ef2225be45987992f82cacad37a2db
