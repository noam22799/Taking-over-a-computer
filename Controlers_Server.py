# import moudels
import socket
from pynput import keyboard
from pynput.mouse import Button, Controller,Listener
import threading

def main():
  
    # Create Socket
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
        server_socket.bind(("127.0.0.1",8830))
        server_socket.listen(1)
        client_socket,address = server_socket.accept()
        
        # Press a key on the keyboard
        def on_press(key):
                try:
                    k = key.char
                except AttributeError:
                    k = key.name
                client_socket.send(f"PRESS|{k}".encode())
        
        # Release a key on the keyboard
        def on_release(key):
                try:
                    k = key.char
                except AttributeError:
                    k = key.name
                client_socket.send(f"RELEASE|{k}".encode())
        
        # Press any button on the mouse
        def press_mouse(x, y, button, pressed):
            if pressed:
                client_socket.send(f"PRESSM|{button}".encode())
            else:
                client_socket.send(f"RELEASEM|{button}".encode())
        
        # Moving the mouse
        def on_move(x, y):
            client_socket.send(f"MOVE|{x},{y}".encode())

         # Start listeners
        listener_keyboard = keyboard.Listener(on_press=on_press, on_release=on_release)
        listener_mouse = Listener(on_click=press_mouse, on_move=on_move)

        listener_keyboard.start()
        listener_mouse.start()

        # Keep main alive
        listener_keyboard.join()
        listener_mouse.join()

if __name__=="__main__":
     main()