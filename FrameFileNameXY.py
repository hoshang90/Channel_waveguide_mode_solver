#!/usr/bin/python3
# -*-coding:Utf-8 -*
import tkinter as tk
from tkinter import filedialog
import os
#from tkinter.ttk import *
class LaFrame(tk.Frame):
    def __init__(self,master,fname,x,y,Dir_label):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.configure_gui(fname,x,y,Dir_label)
        self.create_widgets()

    def _close(self):
        self.destroy()

    def configure_gui(self,fname,x,y,Dir_label):
        self.FileName=fname
        self.x_cut=x
        self.y_cut=y
        self.dir_label=Dir_label
        return 1       
    
    def create_widgets(self):
        mfr=tk.Frame(self.master,bd=3,pady=4)
        mfr.pack(side=tk.LEFT,fill=tk.X,expand=1)
        #-----------------------------------
        ligne=0
        tk.Label(mfr,textvariable=self.dir_label).grid(row = ligne, column=
                0,columnspan=8)
        ligne=1
        tk.Button(mfr,text='Save as', command=lambda:self.file_save_as()).grid(row = ligne, column= 0)#,columnspan=3)
        tk.Entry(mfr, width=12, borderwidth=5, textvariable=self.FileName).grid(row=ligne, column=1, padx=5, pady=5)

        #-----------------------------------
        ligne=2
        tk.Label(mfr,text='xcut  ').grid(row = ligne, column= 0)#,columnspan=3)
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.x_cut).grid(row=ligne, column=1, padx=5, pady=5)
        #-----------------------------------
        ligne=3
        tk.Label(mfr,text='ycut  ').grid(row = ligne, column= 0)#,columnspan=3)
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.y_cut).grid(row=ligne, column=1, padx=5, pady=5)
        return mfr
    def file_save_as(self):
        """Ask the user where to save the file and save it there. 
        Returns True if the file was saved, and False if the user
        cancelled the dialog.
        """
        self.save_as_path =tk.filedialog.askdirectory(initialdir=os.getcwd(),title="Select As")#,filetypes=("json", "*.json")
        if self.save_as_path:
            os.chdir(self.save_as_path)
            self.dir_label.set((os.getcwd()+"/"+self.FileName.get()).replace(os.sep, '/'))
        else:
            tk.messagebox.showinfo("Warning",'Please try again to save the file')
#--------------------------------------------------------------
if __name__ == '__main__':
   root = tk.Tk()
   main_app =LaFrame(root,\
           tk.StringVar(),tk.DoubleVar(),tk.DoubleVar(),tk.StringVar()
           )
   root.mainloop()




