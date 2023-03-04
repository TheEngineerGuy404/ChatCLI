import socket
import rsa
from hashlib import sha256
import sqlite3

"""
LOGIN\n
USERNAME = "TheEngineerGuy"\n
PUBLIC = "<rsa-encryption-key>"\n
LOGIN_HASH = "hash(USERNAME + PUBLIC + PASSPHRASE)"

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

db = sqlite3.connect("ChatCLI.db")
cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_info (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password_hash TEXT NOT NULL,
    public_key TEXT NOT NULL,
    email TEXT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS messages (
    message_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id FOREIGN KEY
        REFERENCES user_info(user_id)
    message TEXT NOT NULL
)
""")
               

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
"""
while runserver:
    data, addr = node.recvfrom(4096)
    response = ParsePacket(data, addr)
"""