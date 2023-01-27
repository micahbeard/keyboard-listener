'''
Custom music shortcut: Create a program that listens for a keyboard input “;” and when this key is pressed 
a browser window is opened to a youtube video playing my favorite song “https://www.youtube.com/watch?v=SQNymNaTr-Y”
'''



from pynput.keyboard import Listener, Key
import webbrowser


def on_press(key):
        if hasattr(key, ';'):         
            webbrowser.open('https://www.youtube.com/watch?v=SQNymNaTr-Y')
    


with Listener(on_press=on_press) as listener: 
    listener.join() 