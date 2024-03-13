import math
import hashlib

# Convert intercepted message and hash from hex to bytes
M = bytes.fromhex('1D84125D200EA0077810B94082B432205E2B050641C7BE158D431B05070B064DB09617BEAA26D3CA3764B7B06100C7059241009DA8500B196511B48D0661A4DCE19A6ADAC68D381CE0343ED1D106705078D1BD0C6B69C778A0AA')
hash_intercepted = bytes.fromhex('0F6F9D8D428D86939C930BC846C1205E3579F5BBBCA9F3A51B86DF7A0DE9509C')

# Define the key length in bytes
key_length = 14

# Concatenate key and message
KM = b'\x00' * key_length + M

# Calculate the padding length
padding_len = 64 - ((key_length + len(M) + 8) % 64)
if padding_len < 0:
    padding_len += 64

# Construct the padding as a byte string
padding = b'\x80' + b'\x00' * (padding_len - 1)

# Add the length of the message (in bits) as a 64-bit big-endian integer
message_len_bits = (key_length + len(M) + padding_len) * 8
padding += message_len_bits.to_bytes(8, byteorder='big')

# Compute the hash of K || M || P || M_2
M2 = bytes.fromhex('D5B8D9080136C91E547277910B1913B4896387CCA6D894795DC600545BDA97CBD0D2155ABE2A64DC00335D936DE7D04D0329C22302802CE6EC0259368ED99B46050809806CAD0751306B000D60604283A0B0E47AEB9E')
KMPM2 = KM + padding + M2
hash_value = hashlib.sha256(KMPM2).hexdigest()

print(f"Padding: {padding.hex()}")
print(f"SHA256(K || M || P || M_2): {hash_value}")
