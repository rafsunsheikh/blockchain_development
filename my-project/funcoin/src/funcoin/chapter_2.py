import hashlib 

input_bytes = b'hello world'

output = hashlib.sha256(input_bytes).hexdigest()

print(f"The hash of the word is: {output}")
