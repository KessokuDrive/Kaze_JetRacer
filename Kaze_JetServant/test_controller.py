import asyncio
import time
import websockets
import threading
import sys
import os
LIB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, LIB)

from libs.uploader import *
from websockets.sync.client import connect
SERVER = "ws://127.0.0.1:8765"

def sendcommand(websocket,key):
    match key:
        case "w":
            send_ws(websocket,coord2cmd(0,0.2))
            print(f"Received: {websocket.recv()}")
        case "a":
            send_ws(websocket,coord2cmd(0.8,0))
            print(f"Received: {websocket.recv()}")
        case "d":
            send_ws(websocket,coord2cmd(-0.8,0))
            print(f"Received: {websocket.recv()}")
        case _:
            pass
    
import sys
import tty
import termios

def read_key():
    # Save the terminal settings
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        # Disable echo and enable canonical input (buffered)
        tty.setcbreak(fd)
        
        # Read a single key press
        ch = sys.stdin.read(1)
        
    finally:
        # Restore the terminal settings
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    
    return ch if ch in ('w', 'a', 's', 'd') else None

def main(data=None,close=False):
    print("Start Connect")
    with connect(SERVER) as websocket:    
        if(close):
            websocket.close()
        if(data!=None):
            key = read_key()
            if key is None:
                pass
            sendcommand(websocket, key)
            print("end\n")
        
try:
    while True:
        main(data=1)
except KeyboardInterrupt:
    main(close=True)