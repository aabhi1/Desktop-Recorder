# Copyright 2021 Agraj Abhishek. All Rights Reserved.
#
# Licensed under the MIT License, (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://github.com/aabhi1/Desktop-Recorder/blob/main/LICENSE
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import os, cv2, sys
import tkinter as tk
from tkinter import Menu, messagebox
from PIL import ImageTk, Image
from pathlib import Path
import datetime
import tkinter.font as font
from tkinter.ttk import *
import pyautogui
import numpy as np

class MainApp(tk.Tk):

    def byusb(self):
        if self.U == 0:
            k1 = 0
            self.U = 1

            dtnow = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            output = "output/"+dtnow+".avi"

            a = datetime.datetime.now()
            cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            ret, img = cap.read()
    #        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            #get info from img
            height, width, channels = img.shape
            # Define the codec and create VideoWriter object
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output, fourcc, 12, (width, height))
            cv2.namedWindow("Live - Press 'q' to Exit", cv2.WINDOW_NORMAL)

            # Resize this window
            cv2.resizeWindow("Live - Press 'q' to Exit", 480, 270)
            imgEar = img
            while True:
                ret, image = cap.read()
                if ret:
                    k1 +=1
                    b = datetime.datetime.now()
                    cv2.imshow("Live - Press 'q' to Exit", image)
                    out.write(image)
                    if k1 > 400:
                        dtnow = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                        output = "output/"+dtnow+".avi"
                        out = cv2.VideoWriter(output, fourcc, 12, (width, height))
                        a = datetime.datetime.now()
                        k1 = 0

                if cv2.waitKey(1) == ord('q'):
                    self.U = 0
                    break
        else:
            messagebox.showerror("Error","Please exit other mode !")

    def byusbintelligent(self):
        if self.U == 0:
            self.U = 1
            k2 = 0
            dtnow = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            output = "output/"+dtnow+".avi"

            a = datetime.datetime.now()
            cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            ret, img = cap.read()
            height, width, channels = img.shape
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(output, fourcc, 12, (width, height))
            cv2.namedWindow("Live - Press 'q' to Exit", cv2.WINDOW_NORMAL)

            # Resize this window
            cv2.resizeWindow("Live - Press 'q' to Exit", 480, 270)
            imgEar = img
            while True:
                ret, image = cap.read()
                if ret:
                    imgLatest = image
                    diff = (imgEar - imgLatest)
                    gray_image = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
                    x=np.where( gray_image > 50 )
                    b = datetime.datetime.now()
                    cv2.imshow("Live - Press 'q' to Exit", image)

                    if x[0].any():
                        k2 += 1
                        out.write(image)
                        if k2 > 400:
                            dtnow = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                            output = "output/"+dtnow+".avi"
                            out = cv2.VideoWriter(output, fourcc, 12, (width, height))
                            a = datetime.datetime.now()
                            k2 = 0
                    imgEar = imgLatest

                    if cv2.waitKey(1) == ord('q'):
                        self.U = 0
                        break
        else:
            messagebox.showerror("Error","Please exit other mode !")


    def recorder(self):
        k3 = 0
        dtnow = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        output = "output/"+dtnow+".avi"

        a = datetime.datetime.now()

        img = pyautogui.screenshot()
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        #get info from img
        height, width, channels = img.shape
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output, fourcc, 12, (width, height))
        cv2.namedWindow("Live - Press 'q' to Exit", cv2.WINDOW_NORMAL)

        # Resize this window
        cv2.resizeWindow("Live - Press 'q' to Exit", 480, 270)
        while True:
            k3 += 1
            img = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            out.write(image)
            # Optional: Display the recording screen
            cv2.imshow("Live - Press 'q' to Exit", image)

            # Stop recording when we press 'q'
            if cv2.waitKey(1) == ord('q'):
                break
            b = datetime.datetime.now()
            if k3 > 400:
                dtnow = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                output = "output/"+dtnow+".avi"
                out = cv2.VideoWriter(output, fourcc, 12, (width, height))
                a = datetime.datetime.now()
                k3 =0

        out.release()
        cv2.destroyAllWindows()

    def intelligentMode(self):
        k4 = 0
        dtnow = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        output = "output/"+dtnow+".avi"

        a = datetime.datetime.now()

        img = pyautogui.screenshot()
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        #get info from img
        height, width, channels = img.shape
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output, fourcc, 12, (width, height))
        cv2.namedWindow("Live - Press 'q' to Exit", cv2.WINDOW_NORMAL)

        # Resize this window
        cv2.resizeWindow("Live - Press 'q' to Exit", 480, 270)
        imgEar = img
        while True:
            img = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            imgLatest = image
            diff = (imgEar - imgLatest)
            gray_image = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            x=np.where( gray_image > 50 )
            b = datetime.datetime.now()
            cv2.imshow("Live - Press 'q' to Exit", image)
            if x[0].any():
                k4 += 1
                out.write(image)
                if k4 > 400:
                    dtnow = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
                    output = "output/"+dtnow+".avi"
                    out = cv2.VideoWriter(output, fourcc, 12, (width, height))
                    a = datetime.datetime.now()
                    k4 = 0
            imgEar = image

            if cv2.waitKey(1) == ord('q'):
                break



        out.release()
        cv2.destroyAllWindows()

    def __init__(self):
        tk.Tk.__init__(self)
        self.configure(background="black")
        self.x = self.y = 0
        self.geometry("154x150")
        self.resizable(0,0)


        if getattr(sys, 'frozen', False):
            application_path = sys._MEIPASS
        elif __file__:
            application_path = os.path.dirname(__file__)

        iconFile = 'logo.ico'
        logoFile = 'logo.png'

        self.iconbitmap(default=os.path.join(application_path, iconFile))
        img = ImageTk.PhotoImage(Image.open(os.path.join(application_path, logoFile)))

        self.swapV = []
        self.afile = []
        self.pdfafile = []
        self.U = 0
        temp_dir = "output"
        Path(temp_dir).mkdir(parents=True, exist_ok=True)
        self.title("Recorder")

        myFont = font.Font(weight="bold")
        menubar = Menu(self)
        self.filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Screen", menu=self.filemenu)

        self.filemenu.add_command(label="Normal Mode", command=self.recorder,
                                  activebackground='#e4642c')

        self.filemenu.add_command(label="Smart Mode", command=self.intelligentMode,
                                  activebackground='#e4642c')
        self.usbmenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="USB", menu=self.usbmenu)
        self.config(menu=menubar)
        self.usbmenu.add_command(label="Normal Mode", command=self.byusb,
                                  activebackground='#e4642c')

        self.usbmenu.add_command(label="Smart Mode", command=self.byusbintelligent,
                                  activebackground='#e4642c')

        self.filemenu.add_separator()

        self.filemenu.add_command(label="Exit", command=self.quit, activebackground='#e4642c')
        self.config(menu=menubar)

        self.helpmenu = Menu(menubar, tearoff=0)
        self.helpmenu.add_command(label="Help", command=lambda: self.fimageUpload(self.afile),
                                  activebackground='#e4642c')
        menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.config(menu=menubar)

        # tk.Button(self, text='Upload Image', command=lambda:self.fimageUpload(afile), bg='#183c5c', fg='#ffffff',
        #               font=('Arial', 12, 'bold'), width="15").grid(row=4, column=0,  pady=4, padx=6)

        img = ImageTk.PhotoImage(Image.open(os.path.join(application_path, logoFile)).resize((150, 150)))
        logo = tk.Label(self, image=img)
        logo.image = img
        logo.grid(row=0, column=0)
        #tk.Label(self, image=img, width="300").grid(row=4, column=1,  pady=4, padx=6)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
