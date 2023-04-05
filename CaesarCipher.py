#Caesar Cipher- Encryption/Decryption

message = input('Enter the message to be encrypted or decrypted: ')
shift = int(input('Enter the offset value: ')) #determines which will be the displacement of the characters to be used in the encryption
mode = input('Choose E to encrypt or D to decrypt the message: ')
# Valid character set in algorithm
CARACTERES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'#alphabet 
#Store the encrypted (or decrypted) text
convert = ''
message = message.upper()
for caractere in message:
  if caractere in CARACTERES:              
    num = CARACTERES.find(caractere)
    if mode == 'E':
      num = num + shift
    elif mode == 'D':
      num = num - shift
  if num >= len(CARACTERES):
    num = num - len(CARACTERES)
  elif num < 0:
    num = num + len(CARACTERES)
    convert= convert + CARACTERES[num] 
  else:
    convert = convert + caractere
if mode == 'E':
  print('Encrypt message ', convert)
if mode == 'D':
  print('Decrypt message ', convert)