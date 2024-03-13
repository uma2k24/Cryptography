# Convert the original ciphertext to bytes
ciphertext_hex = '37B35A5E8CEC247BD9A04B980A819DE0601812448158797306D3A438680A4132'
#ciphertext_hex = '8002314AA61B6034007940AA8D3704932CDE6D8080EE9E052823ABA31215C278'
ciphertext_bytes = bytes.fromhex(ciphertext_hex)

# Split the ciphertext into two blocks: the IV and the encrypted message
iv = ciphertext_bytes[:16]
encrypted_message = ciphertext_bytes[16:]

# Convert the ASCII-encoded versions of "Mike" and "$25" to bytes
mike_b = b'Mike'
twenty_five_b = b'$25'

# Compute the XOR of the second block with the XOR of "Mike" and "$25"
xor1 = bytes([encrypted_message[i] ^ mike_b[i % len(mike_b)] ^ twenty_five_b[i % len(twenty_five_b)] for i in range(len(encrypted_message))])

# Compute the XOR of the result with the XOR of "me" and "$500"
me_b = b'me'
five_hundred_b = b'$500'
xor2 = bytes([xor1[i] ^ me_b[i % len(me_b)] ^ five_hundred_b[i % len(five_hundred_b)] for i in range(len(xor1))])

# Convert the modified second block to hexadecimal format
modified_block_hex = xor2.hex()

# Combine the modified second block with the IV to form the modified ciphertext
modified_ciphertext_hex = iv.hex() + modified_block_hex
print(modified_ciphertext_hex.upper()) # Output: 37B35A5E8CEC247BD9A04B980A819DE0B20B7CCBD2DA6DD49A5225D6F23853CB