<p align="center">
  <img width="250" height="250" src="https://media.tenor.com/images/2c3668f83f251c47fe4319ed58961898/tenor.gif">
</p>
<h1 align="center">Ratify</h1><p align="center">
<b>Ratify</b> is <b>Remote Access Tool</b> Used to Control Desktop Remotely
</p>   

<p align=center>  
<a href=https://github.com/JayTechPH<img src="https://img.shields.io/badge/Author-JayTechPH-red.svg?style=for-the-badge&label=Author" /></a>

<img src="https://img.shields.io/badge/Version-1.0-brightgreen?style=for-the-badge" >
<img src="https://img.shields.io/github/stars/JayTechPH/Ratify?style=for-the-badge">  
<img src="https://img.shields.io/github/followers/JayTechPH?label=Followers&style=for-the-badge">
</p>   

* **If you like the tool and for my personal motivation so as to develop other tools please leave a +1 star** 

This Python script serves as a remote control utility for performing various tasks on a Windows machine. It provides functionality for keylogging, displaying warnings, file uploading, and audio/video streaming. The script can be executed with command-line arguments to control its behavior.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install and run the provided code, follow the steps below:

1. Clone the repository to your local machine:
   ```bash
   $ git clone https://github.com/JayTechPH/Ratify.git
   ```

2. Navigate to the project directory:
   ```bash
   $ cd Ratify
   ```

3. Install the required dependencies. Make sure you have `pyautogui` and `customtkinter` installed:
   ```bash
   $ pip install pynput
   $ pip install vidstream
   ```

4. Run the Python script:
   ```bash
   $ python ratify.py
   ```

Make sure you have the necessary permissions and requirements to run the code successfully.

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

Options for CMD:
--------
    warning                             Show a warning message.
    logger                              Start a keylogger to record keystrokes. if want to run in background "logger false"
    copy                                Upload files to a specified server. required file select example "upload id.txt"
    sharescreen, camera, audio          Example "camera" or if want to set custom ip and port "camera 127.0.0.1 22"
    exit                                If want to exit the connection

## Contributing

We welcome contributions from the community. To contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test your changes.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for more details.

Feel free to reach out if you have any questions or feedback. Happy coding!

## Educational Purpose

Important: This script is intended for educational purposes only. It should be used responsibly and with the explicit consent of the target machine's owner. Unauthorized or malicious use of this script is strictly prohibited and may violate applicable laws and regulations.
