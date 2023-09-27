__author__ = "Pangilinan, Ar Jay"
__email__ = "jaytechph0@gmail.com"
__status__ = "planning"

import vidstream
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-streama", action="store_true")
args = parser.parse_args()

def stream():
    stream = vidstream.StreamingServer("127.0.0.1", 23)
    stream.start_server()
        
def streama():
    stream = vidstream.AudioReceiver("127.0.0.1", 23)
    stream.start_server()
    
    
if args.streama:
    streama()
if not args.streama:
    stream()
