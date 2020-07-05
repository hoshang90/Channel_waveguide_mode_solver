#!/usr/bin/python3
# -*-coding:Utf-8 -*
import tkinter as tk
#from tkinter.ttk import *
class LaFrame(tk.Frame):
    def __init__(self,master,lbda,OR,Nmodes):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.configure_gui(lbda,OR,Nmodes)
        self.create_widgets()

    def _close(self):
        self.destroy()

    def configure_gui(self,lbda,OR,Nmodes):
        self.WL=lbda
        self.OPR=OR
        self.Nmodes=Nmodes
        return 1       
    
    def create_widgets(self):
        mfr=tk.LabelFrame(self.master,text="lbda ",bd=3,pady=4)
        mfr.pack(side=tk.LEFT,fill=tk.X,expand=1)
        #-----------------------------------
        ligne=0
        tk.Label(mfr,text='\u03BB (\u03BCm)').grid(row = ligne, column= 0)#,columnspan=3)
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.WL).grid(row=ligne, column=1, padx=5, pady=5)
        #-----------------------------------
        ligne=1
        tk.Label(mfr,text='OR (°/mm)').grid(row = ligne, column= 0)#,columnspan=3)
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.OPR).grid(row=ligne, column=1, padx=5, pady=5)
        #-----------------------------------
        ligne=2
        tk.Label(mfr,text='# of modes').grid(row = ligne, column= 0)#,columnspan=3)
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.Nmodes).grid(row=ligne, column=1, padx=5, pady=5)

        return mfr
#--------------------------------------------------------------
if __name__ == '__main__':
   root = tk.Tk()
   main_app =LaFrame(root,\
           tk.DoubleVar(),tk.DoubleVar(),tk.IntVar()
           )
   root.mainloop()




