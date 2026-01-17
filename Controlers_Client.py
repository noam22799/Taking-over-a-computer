# import moudels
import socket
from pynput.keyboard import Controller, Key
from pynput.mouse import Button, Controller as MouseController

# Create Keyboard and Mouse controllers
keyboard = Controller()
mouse = MouseController()

def main():
    
    # Create Socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(("127.0.0.1", 8830))
        print("Connected to server")

        while True:
            data = client_socket.recv(1024)
            if not data:
                break

            try:
                action, key_value = data.decode().split('|')
            except ValueError:
                continue  

            # Keyboard actions
            if action == 'PRESS':
                try:
                    key_obj = getattr(Key, key_value)
                except AttributeError:
                    key_obj = key_value
                keyboard.press(key_obj)

            elif action == 'RELEASE':
                try:
                    key_obj = getattr(Key, key_value)
                except AttributeError:
                    key_obj = key_value
                keyboard.release(key_obj)

            # Mouse actions
            elif action == 'PRESSM':
                button_obj = getattr(Button, key_value.split('.')[-1])
                mouse.press(button_obj)

            elif action == 'RELEASEM':
                button_obj = getattr(Button, key_value.split('.')[-1])
                mouse.release(button_obj)

            elif action == 'MOVE':
                x, y = map(int, key_value.strip("()").split(","))
                mouse.move(x, y)

if __name__ == "__main__":
    main()