import sys
import hashlib

try:
    arg = sys.argv[1]
except IndexError:
    raise SystemExit(f"First command line argument is the file to be hashed")

try:
    arg2 = sys.argv[2]
except IndexError:
    raise SystemExit(f"Second command line argument is the existing has value")

print(f"The second command line argument is {arg}")

print(f"The third command line argument is {arg2}")


# Python program to find SHA256 hash string of a file
sha256_hash = hashlib.sha256()
with open(arg,"rb") as f:
    # Read and update hash string value in blocks of 4K
    for byte_block in iter(lambda: f.read(4096),b""):
        sha256_hash.update(byte_block)
    print(sha256_hash.hexdigest())

hash1 = sha256_hash.hexdigest()


with open(arg2, 'r') as f2:
    data = f2.read().replace('\n', '')


hash2 = data

print(data)



if hash1 == hash2:
    print("\nCongratulations, both hashes are equal!")
else:
    print("\nNope! Somebody has tampered with this file")


