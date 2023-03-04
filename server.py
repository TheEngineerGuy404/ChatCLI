import socket
import rsa
from hashlib import sha256
import sqlite3

"""
LOGIN\n
USERNAME="TheEngineerGuy"\n
PUBLIC="<rsa-encryption-key>"\n
LOGIN_HASH="hash" <optional>
SMTP="<smtp-address>" <optional>

LOGOUT\n
USERNAME="TheEngineerGuy"\n
PUBLIC="<rsa-encryption-key>"\n
LOGIN_HASH="hash(USERNAME + PUBLIC + PRIVATE + PASSPHRASE)"

REQUEST\n
FOR="plugin" | "json" | "message_history"
CONTENT_ID="<object-name/source>"

POST\n
CONTENT=object_data\n
CONTENT_TYPE="raw" | "json"

KEEPALIVE\n
PING=<ping-in-ms>

SCAN\n
"""
"""
SCAN_RESPONSE\n
"""

ip_addr = "192.168.1.84"
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
    user_id INTEGER NOT NULL,
    message TEXT NOT NULL,
    message_signature TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES user_info(user_id)
)
""")
               

node = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
node.bind((ip_addr, port))

def ParsePacket(data, address):
    target = data.split("\n")
    
    match target[0]:
        case "LOGIN":
            username = target[1][10:-1].replace("\"", "")
            key = target[2][7:-1].replace("\"", "")
            login_hash = target[3][11:-1].replace("\"", "")
            smtp = target[4][5:-1].replace("\"", "")

            cursor.execute("""
            SELECT * FROM user_info WHERE username = ? AND key = ? AND login_hash = ? AND smtp = ?
            """, (username, key, login_hash, smtp))
            res = cursor.fetchall()
            if res is None:
                return
            print(f"[SYSTEM]:[LOGIN] User '{username}' logged in with IP : '{address[0]}'")

        case "LOGOUT":
            username = target[1][10:-1].replace("\"", "")
            key = target[2][7:-1].replace("\"", "")
            login_hash = target[3][11:-1].replace("\"", "")
            smtp = target[4][5:-1].replace("\"", "")

            cursor.execute("""
            SELECT * FROM user_info WHERE username = ? AND key = ? AND login_hash = ? AND smtp = ?
            """, (username, key, login_hash, smtp))
            res = cursor.fetchall()
            if res is None:
                return
            print(f"[SYSTEM]:[LOGIN] User '{username}' logged out")

        case "REQUEST":
            pass

        case "POST":
            pass

while runserver:
    data, addr = node.recvfrom(4096)
    response = ParsePacket(data, addr)