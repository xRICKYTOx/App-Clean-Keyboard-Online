"""Install app it's moved int directory C://"""


from urllib.error import URLError

from tkinter import Tk, Label, ttk, Text, Scrollbar, END, PhotoImage, Toplevel, Entry, Button, filedialog

from tkinter import messagebox

import urllib.request

from urllib.error import URLError

from subprocess import Popen

import os

import time

import shutil

import sys


import win32api


windows = Tk()

user_pc = win32api.GetUserName()


def insert_information(info):
    """Insert info int information it's class"""

    # Configure ==> font ==> foreground
    info.tag_config(
        "title", font=('Arial', 20), foreground='red'
    )

    info.tag_config(
        'polices', font=('Arial', 13), foreground='blue'
    )

    info.tag_configure(
        'info_polices', font=('Arial', 11), foreground='black'
    )

    # Configure ==> insert information

    info.insert(
        END, "CLEAN KEYBOARD                    v1.0.0\n", "title"
    )

    info.insert(
        END, "\nPrivacy Policy", 'polices'
    )

    info.insert(
        END,
        "\n\nAt xRICKYTOx, we are committed to protecting your privacy and ensuring that your personal information is handled in a safe and responsible manner. This Privacy Policy outlines how we collect, use, disclose, and store your personal information,and your rights with respect to that information.\n\nInformation We Collect \n\nWe collect personal information from you when you use our website, products, or services. We may also collect non-personal information, such as your IP address and browser type, through the use of cookies and other tracking technologies.\n\nHow We Use Your Information \n\nWe may use your personal information to provide you with the products or services that you have requested, to communicate with you about our products or services, and to improve our offerings. We may also use your information for marketing purposes, such as to send you promotional emails or newsletters.\n\nHow We Share Your Information\n\nWe may share your personal information with third-party service providers who perform services on our behalf, such as payment processing, customer service, and marketing. We may also share your information with our affiliates, subsidiaries, or other third parties for their own marketing purposes. We will not sell your personal information to third parties for their marketing purposes without your consent.\n\nYour Rights\n\nYou have the right to access, correct, or delete your personal information at any time. You also have the right to object to the processing of your personal information, to restrict the processing of your personal information and to receive a copy of your personal information in a structured, machine-readable format. \n\nSecurity\n\nWe take the security of your personal information seriously and implement appropriate technical and organizational measures to protect it from unauthorized access, disclosure, alteration, or destruction. \n\nContact Us\n\nIf you have any questions or concerns about our Privacy Policy, please contact us at rikytoloser@gmail.com. We may update this Privacy Policy from time to time, and any changes will be posted on our website.\n\nCopyright\n\nCopyright Clean-Keyboard 2023-2024©", 'info_polices'
    )

    # Configure ==> desactive widget

    info.config(
        state='disable'
    )

    windows.mainloop()


class ExitAppSelect():
    def __init__(
        self
    ):
        # Images ==> Urls ==> With

        url1 = 'https://i.imgur.com/Cxa7WLA.png'
        url2 = 'https://i.imgur.com/IRc8Ahn.png'
        url3 = 'https://i.imgur.com/DWfahBn.png'

        with urllib.request.urlopen(url1) as url_response1:
            app_img = url_response1.read()
        with urllib.request.urlopen(url2) as url_response2:
            icon_img = url_response2.read()
        with urllib.request.urlopen(url3) as url_response3:
            img_app_install = url_response3.read()

        # View ==> withdraw ==> geometry ==> title ==> icon ==> resizable

        self.win = Toplevel()
        self.win.geometry(
            '550x420+625+325'
        )
        self.win.title(
            'Install Clean Keyboard'
        )
        icons = PhotoImage(
            data=icon_img
        )
        self.win.iconphoto(
            False,
            icons
        )
        self.win.resizable(
            False,
            False
        )
        # Panel ==> up ==> line int up

        panel_up = Label(
            self.win,
            background='#BABABA'
        )

        panel_up.place(
            width=550,
            height=65,
            x=0,
            y=0
        )

        line_panel = Label(
            self.win,
            background='#1A1818'
        )

        line_panel.place(
            width=550,
            height=1,
            x=0,
            y=65
        )

        # Log ==> img ==> label

        log_img = PhotoImage(
            data=app_img
        )

        log = Label(
            self.win,
            image=log_img,
            background='#BABABA'
        )

        log.place(
            x=490,
            y=7
        )

        # Install ==> Img ==> Label

        install_img = PhotoImage(
            data=img_app_install
        )

        la = Label(
            self.win,
            image=install_img
        )

        la.place(
            x=20,
            y=100
        )

        # Thanks you ==> introduction text

        thanks = Label(
            self.win,
            text='Thank you for \ninstalling the \nprogram.',
            foreground='#87ABDF',
            font=(
                'Arial', 38
            )
        )

        thanks.place(
            x=220,
            y=115
        )

        # Button ==> exit

        exit_bt = ttk.Button(
            self.win,
            text='Exit',
            command=lambda: [
                {
                    exit_program()
                }
            ]
        )

        exit_bt.place(
            x=455,
            y=383
        )

        self.win.mainloop()


def InstallApp(path):
    """Move arch int path install"""
    class InstallApp():
        def __init__(
            self
        ):
            # Images ==> Urls ==> With

            url1 = 'https://i.imgur.com/Cxa7WLA.png'
            url2 = 'https://i.imgur.com/IRc8Ahn.png'
            url3 = 'https://i.imgur.com/DWfahBn.png'

            with urllib.request.urlopen(url1) as url_response1:
                app_img = url_response1.read()
            with urllib.request.urlopen(url2) as url_response2:
                icon_img = url_response2.read()
            with urllib.request.urlopen(url3) as url_response3:
                img_app_install = url_response3.read()

            # Create folder ==> path select

            self.rut_path = path

            path_name = 'CleanKeyboard'

            path_complet = os.path.join(self.rut_path, path_name)

            if not os.path.exists(path_complet):
                print('True')
            else:
                messagebox.showerror(
                    'Error', 'The folder already exists in this path, please delete it.'
                )
                return SelectInstallPanel()

            # View ==> withdraw ==> geometry ==> title ==> icon ==> resizable

            windows.withdraw()
            self.win = Toplevel()
            self.win.geometry(
                '550x420+625+325'
            )
            self.win.title(
                'Install Clean Keyboard'
            )
            icon = PhotoImage(
                data=icon_img
            )
            self.win.iconphoto(
                False,
                icon
            )
            self.win.resizable(
                False,
                False
            )
            # Panel ==> up ==> line int up

            panel_up = Label(
                self.win,
                background='#BABABA'
            )

            panel_up.place(
                width=550,
                height=65,
                x=0,
                y=0
            )

            line_panel = Label(
                self.win,
                background='#1A1818'
            )

            line_panel.place(
                width=550,
                height=1,
                x=0,
                y=65
            )

            # Log ==> img ==> label

            log_img = PhotoImage(
                data=app_img
            )

            log = Label(
                self.win,
                image=log_img,
                background='#BABABA'
            )

            log.place(
                x=490,
                y=7
            )

            # Buttons ==> Return ==> Continue

            self.return_bt = ttk.Button(
                self.win,
                text='Return',
                cursor='hand2',
                command=lambda: [
                    {
                        self.win.destroy(),
                        SelectInstallPanel()
                    }
                ]
            )

            self.return_bt.place(
                x=20,
                y=383
            )

            continue_bt = ttk.Button(
                self.win,
                text='Install',
                cursor='hand2',
                state='normal',
                command=lambda: [
                    {
                        self.install()
                    }
                ]
            )

            continue_bt.place(
                x=455,
                y=383
            )

            # Install app ==> progress bar install and moved arch's

            styles_install = ttk.Style()
            styles_install.configure(
                'TProgressbar',
                troughcolor='green',
                background='#2b79c2',
                bordercolor='green',
            )

            self.progressbar = ttk.Progressbar(
                self.win,
                style="TProgressbar",
                orient='horizontal',
                length=510
            )

            self.progressbar.place(
                height=30,
                x=20,
                y=320
            )

            # Install ==> Img ==> Label

            install_img = PhotoImage(
                data=img_app_install
            )

            la = Label(
                self.win,
                image=install_img
            )

            la.place(
                x=180,
                y=90
            )

            self.win.mainloop()

        def install(self):
            """Instalación del programa"""
            self.return_bt.config(
                state='disable'
            )
            task = 11
            porcentaje = 0
            while porcentaje < task:
                time.sleep(0.5)
                self.progressbar['value'] += 11
                porcentaje += 1.1
                self.win.update_idletasks()
            if porcentaje > task:
                self.moved_int_path()

        def moved_int_path(self):
            """Move arch's int path select"""

            # Moved ==> folder int path select

            path_complet = f'{path}/CleanKeyboard'
            arch = 'CleanKeyboard'

            # Link ==> acceso directo
            desktop = f'C:/Users/{user_pc}/OneDrive/Escritorio'
            path_move_link = f'{path}/CleanKeyboard/DesktopLnk/CleanKeyboard.lnk'

            # Moved ==> panel apps

            panel_apps = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'
            path_move_link_int_apps = f"{path}/CleanKeyboard/PanelAppsLnk/CleanKeyboard.lnk"

            # Moved's
            shutil.move(arch, path_complet)
            shutil.move(path_move_link, desktop)
            shutil.move(path_move_link_int_apps, panel_apps)
            self.win.destroy()
            ExitAppSelect()

    InstallApp()


class SelectInstallPanel():
    """Install App in system for user"""

    def open_file_localization(self):

        self.folder_selected = filedialog.askdirectory()

        if not os.path.exists(self.folder_selected):
            self.continue_bt.config(
                state='disabled'
            )
            messagebox.showerror(
                'Error', 'Enter a readable path'
            )
            self.rut_not_modify.config(
                state='normal'
            )
            self.rut_not_modify.delete(
                0,
                END
            )
            self.desactive_entry()
        else:
            self.rut_not_modify.config(
                state='normal'
            )
            self.rut_not_modify.delete(
                0,
                END
            )

            self.path = f'{self.folder_selected}'

            if self.path == 'C:/':
                self.rut_not_modify.insert(
                    END,
                    'C:/CleanKeyboard'
                )
            else:
                self.rut_not_modify.insert(
                    END,
                    f'{self.path}/CleanKeyboard'
                )

            self.rut_not_modify.config(
                state='disabled',
                disabledbackground='#E8E8E8'
            )

            self.continue_bt.config(
                state='normal'
            )

    def desactive_entry(self):
        self.rut_not_modify.insert(
            END,
            'Select Path'
        )
        self.rut_not_modify.config(
            state='disabled',
            disabledbackground='#E8E8E8'
        )

    def return_installmain(self):
        self.win.destroy()
        windows.deiconify()

    def __init__(
        self
    ):
        # Images ==> Urls ==> With

        url1 = 'https://i.imgur.com/Cxa7WLA.png'
        url2 = 'https://i.imgur.com/v2BulXh.png'
        url3 = 'https://i.imgur.com/IRc8Ahn.png'

        with urllib.request.urlopen(url1) as url_response1:
            app_img = url_response1.read()
        with urllib.request.urlopen(url2) as url_response2:
            arch_img = url_response2.read()
        with urllib.request.urlopen(url3) as url_response3:
            icon_img = url_response3.read()

        # View ==> withdraw ==> geometry ==> title ==> icon ==> resizable

        windows.withdraw()
        self.win = Toplevel()
        self.win.geometry(
            '550x420+625+325'
        )
        self.win.title(
            'Install Clean Keyboard'
        )
        icon = PhotoImage(
            data=icon_img
        )
        self.win.iconphoto(
            False,
            icon
        )
        self.win.resizable(
            False,
            False
        )
        # Panel ==> up ==> line int up

        panel_up = Label(
            self.win,
            background='#BABABA'
        )

        panel_up.place(
            width=550,
            height=65,
            x=0,
            y=0
        )

        line_panel = Label(
            self.win,
            background='#1A1818'
        )

        line_panel.place(
            width=550,
            height=1,
            x=0,
            y=65
        )

        # Log ==> img ==> label

        log_img = PhotoImage(
            data=app_img
        )

        log = Label(
            self.win,
            image=log_img,
            background='#BABABA'
        )

        log.place(
            x=490,
            y=7
        )

        # Installing ==> rut not modify

        self.rut_not_modify = Entry(
            self.win,
            background='white',
            foreground='black',
            font=(
                'Arial', 13
            )
        )

        self.rut_not_modify.after(
            10, self.desactive_entry
        )

        self.rut_not_modify.place(
            width=468,
            height=33,
            x=20,
            y=100
        )

        # Files ==> img ==> button

        files_img = PhotoImage(
            data=arch_img
        )

        files = Button(
            self.win,
            image=files_img,
            border=0,
            cursor='hand2',
            command=lambda: [
                {
                    self.open_file_localization()
                }
            ]
        )

        files.place(
            x=500,
            y=99
        )

        # Buttons ==> Return ==> Continue
        return_bt = ttk.Button(
            self.win,
            text='Return',
            cursor='hand2',
            command=lambda: [
                {
                    self.return_installmain()
                }
            ]
        )

        return_bt.place(
            x=20,
            y=383
        )

        self.continue_bt = ttk.Button(
            self.win,
            text='Continue',
            cursor='hand2',
            command=lambda: [
                {
                    self.win.destroy(), InstallApp(path=self.path)
                }
            ],
            state='disabled'
        )

        self.continue_bt.place(
            x=455,
            y=383
        )

        self.win.mainloop()


def exit_program():
    """It's exit program or app"""
    Popen(
        [
            'taskkill',
            '/f',
            '/im',
            'CleanKeyboard.exe'
        ]
    )
    sys.exit()


class InstallMain():
    """It's users install app for system"""

    def __init__(
        self
    ):

        # Images ==> Urls ==> With
        url1 = 'https://i.imgur.com/Cxa7WLA.png'
        url2 = 'https://i.imgur.com/v2BulXh.png'
        url3 = 'https://i.imgur.com/IRc8Ahn.png'

        with urllib.request.urlopen(url1) as url_response1:
            app_img = url_response1.read()
        with urllib.request.urlopen(url2) as url_response2:
            arch_img = url_response2.read()
        with urllib.request.urlopen(url3) as url_response3:
            icon_img = url_response3.read()

        # View ==> geometry ==> title ==> icon img ==> icon ==> resizable

        windows.geometry(
            '550x420+625+325'
        )
        windows.title(
            'Install Clean Keyboard'
        )
        icon = PhotoImage(
            data=icon_img
        )
        windows.iconphoto(
            False,
            icon
        )
        windows.resizable(
            False,
            False
        )

        # Panel ==> up ==> line int up

        panel_up = Label(
            windows,
            background='#BABABA'
        )

        panel_up.place(
            width=550,
            height=65,
            x=0,
            y=0
        )

        line_panel = Label(
            windows,
            background='#1A1818'
        )

        line_panel.place(
            width=550,
            height=1,
            x=0,
            y=65
        )

        # Log ==> img ==> label

        log_img = PhotoImage(
            data=app_img
        )

        log = Label(
            windows,
            image=log_img,
            background='#BABABA'
        )

        log.place(
            x=490,
            y=7
        )

        # Button ==> cancel ==> continue

        cancel_bt = ttk.Button(
            windows,
            text='Cancel',
            cursor='hand2',
            command=lambda: [
                {
                    exit_program()
                }
            ]
        )

        cancel_bt.place(
            x=20,
            y=383
        )

        continue_bt = ttk.Button(
            windows,
            text='Continue',
            cursor='hand2',
            command=lambda: [
                {
                    SelectInstallPanel()
                }
            ]
        )

        continue_bt.place(
            x=455,
            y=383
        )

        # Information ==> text ==> scrollbar

        self.information_txt = Text(
            windows,
            background='white',
            foreground='black',
            font=(
                'Arial', 13
            ),
            state='normal'
        )

        information_scr = Scrollbar(
            windows,
            command=self.information_txt.yview,
            cursor='hand2',
        )

        information_scr.place(
            width=15,
            height=290,
            x=510,
            y=80
        )

        self.information_txt.place(
            width=490,
            height=290,
            x=20,
            y=80
        )

        self.information_txt.config(
            yscrollcommand=information_scr.set
        )
        self.information_txt.after(
            200, insert_information(info=self.information_txt)
        )

        windows.mainloop()


def check_internet():
    """Check Connection at Wifi"""
    try:
        urllib.request.urlopen('https://www.google.com')
        InstallMain()
        return True
    except URLError as e:
        return False


if not check_internet():
    windows.withdraw()
    messagebox.showerror(
        'Error', 'Internet connection is required to install the application.'
    )
    sys.exit()
