#!/usr/bin/python3
# -*-coding:Utf-8 -*
import tkinter as tk
class LaFrame(tk.Frame):
    def __init__(self,master,H1_1,H1_2,LC_1,LC_2,H2value):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.configure_gui(H1_1,H1_2,LC_1,LC_2,H2value)
        self.create_widgets()

    def _close(self):
        self.destroy()

    def configure_gui(self,H1_1,H1_2,LC_1,LC_2,H2value):
        self.H1_1=H1_1; self.H1_2=H1_2
        self.LC_1=LC_1;self.LC_2=LC_2
        self.H2value=H2value
        return 1       
    
    def create_widgets(self):
        mfr=tk.LabelFrame(self.master,text="input (\u03BCm) ",bd=3,pady=4)
        mfr.pack(side=tk.LEFT,fill=tk.X,expand=1)
        #-----------------------------------
        ligne=0
        tk.Label(mfr,text="<-- LC -->").grid(row=ligne,column=1)
        tk.Label(mfr,text='W(LC)min=').grid(row = ligne, column= 2,sticky='E')
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.LC_1).grid(row=ligne, column=3, padx=5, pady=5,sticky='W')
        tk.Label(mfr,text='W(LC)max=').grid(row = ligne, column= 4)#,columnspan=3)
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.LC_2).grid(row=ligne, column=5, padx=5, pady=5)
        ligne+=1
        tk.Label(mfr,text="_"*8).grid(row=ligne,column=1)
        #---
        ligne+=1
        tk.Label(mfr,text="|          |").grid(row=ligne,column=1)
        tk.Label(mfr,text="↕H1max").grid(row=ligne,column=2,sticky='E')
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.H1_2).grid(row=ligne, column=3, padx=5, pady=5)
        ligne+=1
        tk.Label(mfr,text='↕H1min').grid(row = ligne, column=2,sticky='E')#,columnspan=3)
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.H1_1).grid(row=ligne, column=3, padx=5, pady=5)
        tk.Label(mfr,text="|          |").grid(row=ligne,column=1)
        #--
        ligne+=1
        Lmax=15
        tk.Label(mfr,text="-"*Lmax).grid(row=ligne,column=0)
        tk.Label(mfr,text="-"*(Lmax+4)).grid(row=ligne,column=2)
        ligne+=1
        tk.Label(mfr,text="↕H2=").grid(row=ligne,column=2,sticky='E')
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.H2value).grid(row=ligne, column=3, padx=5, pady=5)
        ligne+=1
        tk.Label(mfr,text="-"*(Lmax)).grid(row=ligne,column=0)
        tk.Label(mfr,text="-"*12).grid(row=ligne,column=1)
        tk.Label(mfr,text="-"*Lmax).grid(row=ligne,column=2)
        return mfr
#--------------------------------------------------------------
if __name__ == '__main__':
   root = tk.Tk()
   main_app =LaFrame(root,\
           tk.DoubleVar(),tk.DoubleVar(), tk.DoubleVar(),tk.DoubleVar(),tk.DoubleVar()
           )
   root.mainloop()




