import Crypto.Hash.SHA256 as SHA256

def encode(msg):
    h = SHA256.new(msg)
    return h.digest()

def check_hash(msg, hash):
    return encode(msg) == hash
