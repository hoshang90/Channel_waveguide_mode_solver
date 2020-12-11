#!/usr/bin/python3
# -*-coding:Utf-8 -*
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
class LaFrame(tk.Frame):
    def __init__(self,master,Var_var,X1_var,X2_var,dX_var,addX_var,addY_var,
            Dir_label_var,FileName_var, Show_Struct_var,SaveFile_var,Dn_diff_var):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.configure_gui(Var_var,X1_var,X2_var,dX_var,addX_var,addY_var,Dir_label_var
                ,FileName_var,Show_Struct_var,SaveFile_var,Dn_diff_var)
        self.create_widgets()

    def _close(self):
        self.destroy()

    def configure_gui(self,Var_var,X1_var,X2_var,dX_var,addX_var,addY_var,Dir_label_var,FileName_var
            ,Show_Struct_var,SaveFile_var,Dn_diff_var):
        self.Var_var=Var_var;self.X1_var=X1_var;self.X2_var=X2_var;self.dX_var=dX_var;self.addX_var=addX_var;
        self.addY_var=addY_var;self.dir_label_var=Dir_label_var;self.FileName_var=FileName_var;
        self.Show_Struct_var=Show_Struct_var;self.SaveFile_var=SaveFile_var;self.Dn_diff_var=Dn_diff_var
        return 1       
    
    def create_widgets(self):
        mfr=tk.LabelFrame(self.master,bd=3,pady=4)#text="input Variable ",bd=3,pady=4)
        mfr.pack(side=tk.LEFT,fill=tk.X,expand=1)
        #-----------------------------------
        ligne=0
        tk.Label(mfr,text="Select the variable").grid(row=ligne,column=0)
        ttk.Combobox(mfr, width=8, textvariable=self.Var_var, values=["nc","n_rib","n_ridge","n_sub",\
                "H1","H2","LC"]).grid(row=ligne, column=1, padx=5, pady=5)
        #tk.Separator(frame,orient='horizontal').grid(row=ligne+1,columnspan=10,sticky='EW')
        ligne+=1
        tk.Label(mfr,text="X1").grid(row=ligne,column=0,sticky='E')
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.X1_var).grid(row=ligne, column=1, padx=5, pady=5)
        ligne+=1
        tk.Label(mfr,text="X2").grid(row=ligne,column=0,sticky='E')
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.X2_var).grid(row=ligne, column=1, padx=5, pady=5)
        tk.Label(mfr,text="Add X").grid(row=ligne,column=2,sticky='E')
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.addX_var).grid(row=ligne, column=3, padx=5, pady=5)
        ligne+=1
        tk.Label(mfr,text='dX').grid(row = ligne, column=0,sticky='E')#,columnspan=3)
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.dX_var).grid(row=ligne, column=1, padx=5, pady=5)
        tk.Label(mfr,text="Add Y").grid(row=ligne,column=2,sticky='E')
        tk.Entry(mfr, width=5, borderwidth=5, textvariable=self.addY_var).grid(row=ligne, column=3, padx=5, pady=5)
        ligne+=1
        tk.Label(mfr,textvariable=self.dir_label_var).grid(row = ligne, column=0,columnspan=8)
        ligne+=1
        tk.Button(mfr,text='Save as', command=lambda:self.file_save_as()).grid(row = ligne, column= 0)
        tk.Entry(mfr, width=10, borderwidth=5, textvariable=self.FileName_var).grid(row=ligne, column=1, padx=5, pady=5)
        ligne+=1
        tk.Checkbutton(mfr,text="Save file",variable=self.SaveFile_var).grid(row = ligne, column= 0)
        tk.Checkbutton(mfr,text="Dn difference",variable=self.Dn_diff_var).grid(row = ligne, column=1)
        tk.Checkbutton(mfr,text="Show sturcture",variable=self.Show_Struct_var).grid(row = ligne, column=2)
        return mfr
    def file_save_as(self):
        """Ask the user where to save the file and save it there. 
        Returns True if the file was saved, and False if the user
        cancelled the dialog.
        """
        self.save_as_path =tk.filedialog.askdirectory(initialdir=os.getcwd(),title="Select As")#,filetypes=("json", "*.json")
        if self.save_as_path:
            os.chdir(self.save_as_path)
            self.dir_label_var.set((os.getcwd()+"/"+self.FileName_var.get()).replace(os.sep, '/'))
        else:
            tk.messagebox.showinfo("Warning",'Please try again to save the file')

#--------------------------------------------------------------
if __name__ == '__main__':
   root = tk.Tk()
   main_app =LaFrame(root,\
           tk.StringVar,tk.DoubleVar(),tk.DoubleVar(), tk.DoubleVar(),tk.DoubleVar(),tk.DoubleVar()\
           ,tk.StringVar(),tk.StringVar(),tk.BooleanVar(),tk.BooleanVar(),tk.BooleanVar())
   root.mainloop()
