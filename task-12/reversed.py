import string

def de_xor(x):
    return ''.join(chr(ord(h)^10) for h in x)

def de_shift(x):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    z = []
    for i in x:
        if i.isupper() is True:
            z.append(upper[(upper.index(i)-3)%26])
        elif i.islower() is True:
            z.append(lower[(lower.index(i)-3)%26])
        elif i.isdigit() is True:
            z.append(digits[(digits.index(i)-3)%10])
    return z
def decode(x):
    return bytearray.fromhex(x).decode()
    
p=(de_shift(de_xor(decode('667b6c7d63677f3c733c7f323c3c7b333e7b3c3c7f3e7b333e3232393c3d3268'))))
print(p)
str=""
for i in p:
    str+=i
print(str)
