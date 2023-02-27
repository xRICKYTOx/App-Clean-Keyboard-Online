"""Clean for Keyboard this user"""


from tkinter import Tk, Button, PhotoImage, Label, messagebox

import keyboard

import urllib.request

import sys

from urllib.error import URLError

windows = Tk()

url1 = 'https://i.imgur.com/9JAfPhz.png'
url2 = 'https://i.imgur.com/nW4OSIO.png'
url3 = 'https://i.imgur.com/HREytYT.png'

with urllib.request.urlopen(url1) as url_response1:
    deactivate = url_response1.read()
with urllib.request.urlopen(url2) as url_response2:
    activate = url_response2.read()
with urllib.request.urlopen(url3) as url_response3:
    logo = url_response3.read()


class CleanKeyboard():
    def __init__(
        self
    ):
        # Visual
        windows.geometry(
            "300x50+850+450"
        )
        windows.config(
            background='white'
        )
        windows.resizable(
            False,
            False
        )
        windows.title(
            'Clean Keyboard'
        )
        icon = PhotoImage(
            data=logo
        )
        windows.iconphoto(
            False,
            icon
        )

        # Txt

        txt = Label(
            windows,
            text="Blocked Keyboard",
            font=(
                'Arial', 15
            ),
            background='white',
            foreground='black'
        )

        txt.place(
            x=35,
            y=10
        )

        # Button

        img = PhotoImage(
            data=deactivate
        )

        self.button = Button(
            windows,
            image=img,
            background="white",
            border=0,
            activebackground='white',
            command=lambda: [
                {
                    self.activate_button()
                }
            ],
            cursor='hand2'
        )

        self.button.place(
            x=220,
            y=1
        )

        windows.mainloop()

    def desactivate_button(self):
        img = PhotoImage(
            data=deactivate
        )
        self.button.config(
            image=img,
            command=lambda: [
                {
                    self.activate_button()
                }
            ]
        )

        keyboard.unhook_all()

        windows.mainloop()


    def activate_button(self):
        img = PhotoImage(
            data=activate
        )
        self.button.configure(
            image=img,
            command=lambda: [
                {
                    self.desactivate_button()
                }
            ]
        )

        # Blocked Keyboard
        keyboard.block_key('esc')
        keyboard.block_key('F1')
        keyboard.block_key('F2')
        keyboard.block_key('F3')
        keyboard.block_key('F4')
        keyboard.block_key('F5')
        keyboard.block_key('F6')
        keyboard.block_key('F7')
        keyboard.block_key('F8')
        keyboard.block_key('F9')
        keyboard.block_key('F10')
        keyboard.block_key('F11')
        keyboard.block_key('F12')
        keyboard.block_key('delete')
        keyboard.block_key('home')
        keyboard.block_key('end')
        keyboard.block_key(33)
        keyboard.block_key(34)
        keyboard.block_key(91)
        keyboard.block_key(255)
        keyboard.block_key(173)
        keyboard.block_key(174)
        keyboard.block_key(175)
        keyboard.block_key(177)
        keyboard.block_key(179)
        keyboard.block_key(176)
        keyboard.block_key('`')
        keyboard.block_key('1')
        keyboard.block_key('2')
        keyboard.block_key('3')
        keyboard.block_key('4')
        keyboard.block_key('5')
        keyboard.block_key('6')
        keyboard.block_key('7')
        keyboard.block_key('8')
        keyboard.block_key('9')
        keyboard.block_key('0')
        keyboard.block_key('-')
        keyboard.block_key('=')
        keyboard.block_key(8)
        keyboard.block_key(192)
        keyboard.block_key('tab')
        keyboard.block_key('q')
        keyboard.block_key('w')
        keyboard.block_key('e')
        keyboard.block_key('r')
        keyboard.block_key('t')
        keyboard.block_key('y')
        keyboard.block_key('u')
        keyboard.block_key('i')
        keyboard.block_key('o')
        keyboard.block_key('p')
        keyboard.block_key('[')
        keyboard.block_key(']')
        keyboard.block_key(220)
        keyboard.block_key('capslock')
        keyboard.block_key('a')
        keyboard.block_key('s')
        keyboard.block_key('d')
        keyboard.block_key('f')
        keyboard.block_key('g')
        keyboard.block_key('h')
        keyboard.block_key('j')
        keyboard.block_key('k')
        keyboard.block_key(255)
        keyboard.block_key('l')
        keyboard.block_key('+')
        keyboard.block_key("\\")
        keyboard.block_key(';')
        keyboard.block_key('space')
        keyboard.block_key('backspace')
        keyboard.block_key('enter')
        keyboard.block_key(222)
        keyboard.block_key(20)
        keyboard.block_key('shift')
        keyboard.block_key('z')
        keyboard.block_key('x')
        keyboard.block_key('c')
        keyboard.block_key('v')
        keyboard.block_key('b')
        keyboard.block_key('n')
        keyboard.block_key('m')
        keyboard.block_key(',')
        keyboard.block_key('.')
        keyboard.block_key('/')
        keyboard.block_key('ctrl')
        keyboard.block_key('alt')
        keyboard.block_key(32)
        keyboard.block_key(37)
        keyboard.block_key(38)
        keyboard.block_key(39)
        keyboard.block_key(40)
        keyboard.block_key('numlock')
        keyboard.block_key(144)
        keyboard.block_key('/')
        keyboard.block_key('*')
        keyboard.block_key(111)
        keyboard.block_key('-')
        keyboard.block_key(109)
        keyboard.block_key(103)
        keyboard.block_key(104)
        keyboard.block_key(105)
        keyboard.block_key(102)
        keyboard.block_key(101)
        keyboard.block_key(100)
        keyboard.block_key(99)
        keyboard.block_key(98)
        keyboard.block_key(97)
        keyboard.block_key(96)
        keyboard.block_key(110)
        keyboard.block_key(13)
        keyboard.block_key(107)

        windows.mainloop()


def check_internet():
    """Check Connection at Wifi"""
    try:
        urllib.request.urlopen('https://www.google.com')
        CleanKeyboard()
        return True
    except URLError as e:
        return False


if not check_internet():
    windows.withdraw()
    messagebox.showerror(
        'Error', 'Internet connection is required to install the application.'
    )
    sys.exit()
