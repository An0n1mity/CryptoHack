import telnetlib
import json
import string
from Crypto.Util import number
import base64

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

def rot13(encoded):
    rot13 = bytes.maketrans(b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
   b"NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm")
    return encoded.translate(rot13)

def base16(encoded):
    bytes = []
    for i in range(2, len(encoded), 2):
        bytes.append(chr(int(encoded[i:i+2],16)))
    return "".join(bytes)

while(1):

    received = json_recv()
    print(received)
    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    if received["type"] == "base64":
        decoded = base64.b64decode(received["encoded"]).decode()
    if received["type"] == "hex":
        decoded = bytearray.fromhex(received["encoded"]).decode()
    if received["type"] == "rot13":
        decoded = rot13(received["encoded"])
    if received["type"] == "bigint":
        decoded = base16(received["encoded"])#arrive en str
    if received["type"] == "utf-8":
        decoded = "".join(chr(b) for b in received["encoded"])

    to_send = {
        "decoded": decoded
    }
    json_send(to_send)

    #json_recv()
