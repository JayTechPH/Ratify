# Ratify

![Project Logo](icon.ico)

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
   $ cd project
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

##Usage:
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
