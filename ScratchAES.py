import time
C2I=dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',range(26)))
I2C=dict(zip(range(26),'ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
#INPUTS
start_time = time.time()
filename=input('Enter the plaintext to be encrypted: ')

with open(filename, 'r') as file:
    original = file.read()

plaintext=original.upper()

key=13

#ROT13 CIPHER / ceasar cipher
ciphertext=[]
for word in plaintext.split(' '):
	ciphertext.append(''.join([I2C[(C2I[i]+key)%26] for i in word]))
ciphertext=' '.join(ciphertext)

with open('outfile.txt', 'w') as file:
    file.write(ciphertext)
    
#OUTPUTS
print('\n\n\t\tPlaintext:  ',plaintext)
print('\n\n\t\tCiphertext: ',ciphertext)
end_time = time.time()
print(end_time - start_time)