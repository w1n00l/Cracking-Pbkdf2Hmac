import base64
import hashlib
import sys

### edit this settings, based on your PBKDF2Hmac
hash_name = 'sha1'
iterations = '128000'
dklen = 160 / 8

hashfile = sys.argv[1]
outfile = sys.argv[2]

f = open(hashfile,'rb')
hashes = f.read().splitlines()
f.close()

o = open(outfile,'w')

for hash in hashes:
    b64e = hash
    b64d = base64.b64decode(b64e)
    secret = b64d[16:]
    salt = b64d[8:16]
    b64secret = str(base64.b64encode(secret),'utf-8')
    b64salt = str(base64.b64encode(salt),'utf-8')
    o.write(hash_name+':'+iterations+':'+b64salt+':'+b64secret+'\n')
