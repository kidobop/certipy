import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

class Generate_Certificates:
    def __init__(self,master):
        self.master=master
        self.master.title("Certipy")
        self.master.geometry("1200x800")
        self.master.config(bg="#272727")

        self.button_frame=tk.Frame(self.master,bg="#272727")
        self.button_frame.pack(side=tk.TOP,fill=tk.X,padx=20,pady=15)

        self.upload_button=tk.Button(self.button_frame,text="Upload Image",relief="flat",bg="#4CAF50",fg="white",font=("Helvetica",12,"bold"),padx=15,pady=10,activebackground="#45a049")
        self.upload_button.pack(side=tk.LEFT,padx=10)

        self.clear_button=tk.Button(self.button_frame,text="Clear Image",state=tk.DISABLED,relief="flat",bg="#4CAF50",fg="white",font=("Helvetica",12,"bold"),padx=15,pady=10,activebackground="#45a049")
        self.clear_button.pack(side=tk.LEFT,padx=10)

        self.canvas=tk.Canvas(self.master,bg="#292929")
        self.canvas.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)



def main():
    root=tk.Tk()
    app=Generate_Certificates(root)
    root.mainloop()

if __name__=="__main__":
    main()