#Look! I made changes!
def enc(msg):
    c = []
    for char in msg:
        c.append(chr(ord(char)^0x69))
    return ''.join(c)


a = "hello world"
b = "testing"
print a,b
print enc(a), enc(b)
print enc(enc(a)), enc(enc(b))
