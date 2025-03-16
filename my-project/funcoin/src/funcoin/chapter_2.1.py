import hashlib

# Hash an image

file = open("/Users/mdrafsunsheikh/work/blockchain-development/my-project/funcoin/src/funcoin/metamask_logo.png", "rb")
hash = hashlib.sha256(file.read()).hexdigest()
file.close()

print(f"The hash of the file is: {hash}")
