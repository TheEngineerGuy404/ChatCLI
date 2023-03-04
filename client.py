import socket
import rsa
from hashlib import sha256
import curses
import curses.textpad
import json
import os
from pythonping import ping
import threading

first_execution = False

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
SUCCESS\n
IN="login" | "logout" | "request" | "post" | "keepalive"

FAILURE\n
IN="login" | "logout" | "request" | "post" | "keepalive"\n
REASON=<reason>

SCAN_RESULT\n
NAME=<server-name>\n
LOGIN_AMOUNT=<num-of-active-logins>
LOGIN_MAX=<max-num-of-active-logins>
"""


ip_addrs = ["192.168.1.84"]
port = 2800
runclient = True


screensize = os.get_terminal_size()
scr_width = screensize.columns
scr_height = screensize.lines

nav_vert  = 0
nav_horiz = 0

scr = curses.initscr()
servers = curses.newpad(255, int(scr_width/4))
curses.cbreak()
curses.noecho()
curses.curs_set(0)
scr.nodelay(1)
scr.keypad(True)

node = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def ServerPing(ip_addr):
    ping_res = ping(ip_addr, timeout=1, payload="ping")
    if ping_res.packet_loss > 2:
        return f"'{ip_addr}' is unresponsive/unreachable"
    node.sendto(ip_addr, "SCAN".encode("utf-8"))

    try:
        node.settimeout(3)
        data, _ = node.recvfrom(4096)
    except socket.TimeoutError:
        return f"'{ip_addr}' is unresponsive/unreachable"
    
    data = data.decode("utf-8").split("\n")
    if data[0] != "SCAN_RESULT":
        return f"'{ip_addr}' is unresponsive/unreachable"

     

while runclient:
    x = scr.getch()
    match x:
        # Arrow keys
        case 259: # Up arrow
            pass

        case 258: # Down arrow
            pass
        
        case 260: # Left arrow
            pass

        case 261: # Right arrow
            pass

        # Number keys
        case 48: # Numpad 0
            pass

        case 49: # Numpad 1
            pass

        case 50: # Numpad 2
            pass

        case 51: # Numpad 3
            pass

        case 52: # Numpad 4
            pass

        case 53: # Numpad 5
            pass

        case 54: # Numpad 6
            pass

        case 55: # Numpad 7
            pass

        case 56: # Numpad 8
            pass

        case 57: #Numpad 9
            pass
    
    scr.clear()
    for y in range(scr_height-1):
        scr.addch(y, int(scr_width / 3), "#")
    for y in range(scr_height-1):
        scr.addch(y, 0, "#")
    scr.refresh()

curses.curs_set(1)
curses.endwin()

"""
width = 96
line = 32

100000000000000000000000000000001
1 Cool Server         - 124.0ms 1

"""