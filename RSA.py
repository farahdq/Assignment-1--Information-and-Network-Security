# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 22:19:15 2022

@author: ASUS
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time

secret_message = b'AJFIPWND'

start_time = time.time()
### First, make a key and save it
key = RSA.generate(2048)
with open( 'mykey.pem', 'wb' ) as f:
    f.write( key.exportKey( 'PEM' ))
 
### Then use key to encrypt and save our message
public_crypter = PKCS1_OAEP.new( key )
enc_data = public_crypter.encrypt(secret_message)
with open( 'encrypted.txt', 'wb' ) as f:
    f.write( enc_data )

### And later on load and decode
with open( 'mykey.pem', 'r' ) as f:
    key = RSA.importKey( f.read() )

with open( 'encrypted.txt', 'rb' ) as f:
    encrypted_data = f.read()
    

public_crypter =  PKCS1_OAEP.new( key )
decrypted_data = public_crypter.decrypt( encrypted_data )

end_time = time.time()
print(end_time - start_time)

