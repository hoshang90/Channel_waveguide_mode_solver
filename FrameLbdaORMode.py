#!/usr/bin/python3
# -*-coding:Utf-8 -*
import tkinter as tk
#from tkinter.ttk import *
class LaFrame(tk.Frame):
    def __init__(self,master,lbda,OR,Nmodes,TraceMode_var,TraceIntensity_var):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.configure_gui(lbda,OR,Nmodes,TraceMode_var,TraceIntensity_var)
        self.create_widgets()

    def _close(self):
        self.destroy()

    def configure_gui(self,lbda,OR,Nmodes, TraceMode_var, TraceIntensity_var):
        self.WL=lbda
        self.OPR=OR
        self.Nmodes=Nmodes
        self.TraceMode_var=TraceMode_var
        self.TraceIntensity_var=TraceIntensity_var
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
        #-----------------------------------
        ligne=3
        tk.Checkbutton(mfr,text="Trace Modes",variable=self.TraceMode_var).grid(row = ligne, column= 0)
        tk.Checkbutton(mfr,text="Trace Intensity",variable=self.TraceIntensity_var).grid(row = ligne, column=1)

        return mfr
#--------------------------------------------------------------
if __name__ == '__main__':
   root = tk.Tk()
   main_app =LaFrame(root,\
           tk.DoubleVar(),tk.DoubleVar(),tk.IntVar()
           ,tk.BooleanVar(), tk.BooleanVar())
   root.mainloop()




