#!/usr/bin/python3
# -*-coding:Utf-8 -*
import tkinter as tk
#from tkinter.ttk import *
class LaFrame(tk.Frame):
    def __init__(self,master,fname,x,y):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.configure_gui(fname,x,y)
        self.create_widgets()

    def _close(self):
        self.destroy()

    def configure_gui(self,fname,x,y):
        self.FileName=fname
        self.x_cut=x
        self.y_cut=y
        return 1       
    
    def create_widgets(self):
        mfr=tk.Frame(self.master,bd=3,pady=4)
        mfr.pack(side=tk.LEFT,fill=tk.X,expand=1)
        #-----------------------------------
        ligne=0
        tk.Label(mfr,text='Filename\n to save').grid(row = ligne, column= 0)#,columnspan=3)
        tk.Entry(mfr, width=12, borderwidth=5, textvariable=self.FileName).grid(row=ligne, column=1, padx=5, pady=5)
        #-----------------------------------
        ligne=1
        tk.Label(mfr,text='xcut  ').grid(row = ligne, column= 0)#,columnspan=3)
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.x_cut).grid(row=ligne, column=1, padx=5, pady=5)
        #-----------------------------------
        ligne=2
        tk.Label(mfr,text='ycut  ').grid(row = ligne, column= 0)#,columnspan=3)
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.y_cut).grid(row=ligne, column=1, padx=5, pady=5)
        return mfr
#--------------------------------------------------------------
if __name__ == '__main__':
   root = tk.Tk()
   main_app =LaFrame(root,\
           tk.StringVar(),tk.DoubleVar(),tk.DoubleVar()
           )
   root.mainloop()




