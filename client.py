import curses
import socket
import rsa
"""
LOGIN\n
USERNAME = "TheEngineerGuy"\n
PUBLIC = "<rsa-encryption-key>"\n
LOGIN_HASH = "hash(USERNAME + PUBLIC + PRIVATE + PASSPHRASE)"

LOGOUT\n
USERNAME = "TheEngineerGuy"\n
PUBLIC = "<rsa-encryption-key>"\n
LOGIN_HASH = "hash(USERNAME + PUBLIC + PRIVATE + PASSPHRASE)"

REQUEST\n
FOR = "plugin" | "json" | "message_history"

POST\n
CONTENT = object_data\n
CONTENT_TYPE = "raw" | "json\n
CONTENT_SIZE = sizeof(CONTENT)
"""


ip_addr = "192.168.122.255"
port = 2800
runserver = True
clients = []

node = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
node.bind((ip_addr, port))

def ParsePacket(data, address):
    target = data.split("\n")
    
    match target[0]:
        case "LOGIN":
            pass

        case "LOGOUT":
            pass

        case "REQUEST":
            pass

        case "POST":
            pass

while runserver:
    response = ParsePacket(node.recvfrom(2048))