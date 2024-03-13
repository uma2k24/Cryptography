from Crypto.Cipher import AES
import hashlib

# Define the RSA private key
n = 59210790280148624739286652371
d = 49699248857891630688602112147

# Define the ciphertext
c = '19A9B282518E6675CFBAE13EAB8148FD4CFB383D6B83C9A1436F64662DE83ED26D8D9B310CC398344FF786773CE0E801'

# Convert the ciphertext from hexadecimal to bytes
c_bytes = bytes.fromhex(c)

# Decrypt the ciphertext using AES-CBC decryption
key = hashlib.sha256(str(pow(int(y.replace(" ", ""),  d, n)).encode('utf-8')).hexdigest().encode('utf-8')).digest()
cipher = AES.new(key, AES.MODE_CBC, b'0'*16)
m_bytes = cipher.decrypt(c_bytes)

# Convert the decrypted message from bytes to string
m = m_bytes.decode('utf-8')

# Convert the RSA encrypted message from hexadecimal to decimal
y = int('73B2E681F398E71B9BE55915'.replace(" ", ""), 16)

# Decrypt the RSA encrypted message to obtain x
x = pow(y, d, n)

print(x)
