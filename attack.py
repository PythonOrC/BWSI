import Crypto.Hash.SHA256 as SHA256

def encode(msg):
    h = SHA256.new(msg)
    return h.digest()

def check_hash(msg, hash):
    return encode(msg) == hash

def main():
    msg = b"0x10"
    hash = b"0x10"
    result = encode(msg)
    result2 = encode(hash)
    print(result)
    print(result2)

main()