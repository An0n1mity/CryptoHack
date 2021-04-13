def cesear_cipher(string, shift):
    return  ''.join([chr(((ord(l)-ord('A')+shift)%26)+ord('A')) for l in string])

def veginere_cipher(string, key):
    return ''.join([chr((ord(string[l])-ord('A')+(ord(key[l%len(key)])-ord('A')))%26+ord('A')) for l in range(0, len(string))])

def one_pad(string, key, decode=False):
    #xor the ascii representation
    if decode:
        ascii_list = [int(string[x:x+2], 16) for x in range(0, len(string), 2)]
        return ''.join([chr(ascii_list[l] ^ ord(key[l%len(key)])) for l in range(0, len(ascii_list))])
    return ''.join('{:02x}'.format(x) for x in [ord(string[l]) ^ ord(key[l%len(key)])for l in range(0, len(string))])

