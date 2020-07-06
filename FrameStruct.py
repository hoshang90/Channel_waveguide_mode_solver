#!/usr/bin/python3
# -*-coding:Utf-8 -*
import tkinter as tk
#from tkinter.ttk import *
class LaFrame(tk.Frame):
    def __init__(self,master,nC_1,nC_2,nC_3,\
            nL1_1,nL1_2,nL1_3,\
            nL2_1,nL2_2,nL2_3,\
            nSub_1,nSub_2,nSub_3,\
            TL_1,TL_2,Tchan):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.configure_gui(
                nC_1,nC_2,nC_3,\
                nL1_1,nL1_2,nL1_3,\
                nL2_1,nL2_2,nL2_3,\
                nSub_1,nSub_2,nSub_3,\
                TL_1,TL_2,Tchan)
        self.create_widgets()

    def _close(self):
        self.destroy()

    def configure_gui(self,nC_1,nC_2,nC_3,\
            nL1_1,nL1_2,nL1_3,\
            nL2_1,nL2_2,nL2_3,\
            nSub_1,nSub_2,nSub_3,\
            TL_1,TL_2,Tchan):
        self.nC_1=nC_1;self.nC_2=nC_2;self.nC_3=nC_3
        self.nL1_1=nL1_1;self.nL1_2=nL1_2;self.nL1_3=nL1_3
        self.nL2_1=nL2_1;self.nL2_2=nL2_2;self.nL2_3=nL2_3
        self.nSub_1=nSub_1;self.nSub_2=nSub_2;self.nSub_3=nSub_3
        self.TL_1=TL_1;self.TL_2=TL_2;self.Tchan=Tchan
        return 1       
    
    def create_widgets(self):
        mfr=tk.LabelFrame(self.master,text="Channel Structure",bd=3,pady=4)
        mfr.pack(side=tk.LEFT,fill=tk.X,expand=1)
        #-----------------------------------
        col=0
        ligne=0
        tk.Label(mfr,text="Refractive indices").grid(row = ligne, column= 2)#,columnspan=3)
        tk.Label(mfr,text="Thickness").grid(row = ligne, column= 4)
        #-----------------------------------
        ligne+=1;col=0
        tk.Label(mfr,text="Cover").grid(row = ligne, column= col)
        col+=1
        tk.Entry(mfr, width=10, borderwidth=5, textvariable=self.nC_3).grid(row=ligne, column=col, padx=5, pady=5)
        tk.Entry(mfr, width=10, borderwidth=5, textvariable=self.nC_2).grid(row=ligne, column=col+1, padx=5, pady=5)
        tk.Entry(mfr, width=10, borderwidth=5, textvariable=self.nC_1).grid(row=ligne, column=col+2, padx=5, pady=5)
        #-----------------------------------
        ligne+=1;col=0
        tk.Label(mfr,text="Layer 2").grid(row = ligne, column= col)
        col+=1
        tk.Entry(mfr, width=10, borderwidth=5, textvariable=self.nL1_3).grid(row=ligne, column=col, padx=5, pady=5)
        tk.Entry(mfr, width=10, borderwidth=5, textvariable=self.nL1_2).grid(row=ligne, column=col+1, padx=5, pady=5)
        tk.Entry(mfr, width=10, borderwidth=5, textvariable=self.nL1_1).grid(row=ligne, column=col+2, padx=5, pady=5)
        tk.Entry(mfr, width=10, borderwidth=5, textvariable=self.TL_1).grid(row=ligne, column=col+3, padx=5, pady=5)
        #-----------------------------------
        ligne+=1;col=0
        tk.Label(mfr,text="Layer 1").grid(row = ligne, column= col)
        col+=1
        tk.Entry(mfr, width=10, borderwidth=5, textvariable=self.nL2_3).grid(row=ligne, column=col, padx=5, pady=5)
        tk.Entry(mfr, width=10, borderwidth=5, textvariable=self.nL2_2).grid(row=ligne, column=col+1, padx=5, pady=5)
        tk.Entry(mfr, width=10, borderwidth=5, textvariable=self.nL2_1).grid(row=ligne, column=col+2, padx=5, pady=5)
        tk.Entry(mfr, width=10, borderwidth=5, textvariable=self.TL_2).grid(row=ligne, column=col+3, padx=5, pady=5)
        #-----------------------------------
        ligne+=1;col=0
        tk.Label(mfr,text="Substrate").grid(row = ligne, column= col)
        col+=1
        tk.Entry(mfr, width=10, borderwidth=5, textvariable=self.nSub_3).grid(row=ligne, column=col, padx=5, pady=5)
        tk.Entry(mfr, width=10, borderwidth=5, textvariable=self.nSub_2).grid(row=ligne, column=col+1, padx=5, pady=5)
        tk.Entry(mfr, width=10, borderwidth=5, textvariable=self.nSub_1).grid(row=ligne, column=col+2, padx=5, pady=5)
        #-----------------------------------
        ligne+=1
        tk.Label(mfr,text="Channel (LC)").grid(row = ligne, column= 2)
        ligne+=1
        tk.Entry(mfr, width=10, borderwidth=5, textvariable=self.Tchan).grid(row=ligne, column=2, padx=5, pady=5)

        return mfr
  
#--------------------------------------------------------------
if __name__ == '__main__':
   root = tk.Tk()
   main_app =LaFrame(root,\
           tk.DoubleVar(),tk.DoubleVar(),tk.DoubleVar(),\
           tk.DoubleVar(),tk.DoubleVar(),tk.DoubleVar(),\
           tk.DoubleVar(),tk.DoubleVar(),tk.DoubleVar(),\
           tk.DoubleVar(),tk.DoubleVar(),tk.DoubleVar(),\
           tk.DoubleVar(),tk.DoubleVar(),tk.DoubleVar()
           )
   root.mainloop()




