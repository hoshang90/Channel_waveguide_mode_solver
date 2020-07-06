#!/usr/bin/python3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mpl_toolkits.axes_grid1 import make_axes_locatable
import os
import matplotlib.colors as colors
import numpy as np
from Channels_multilayer import Channel
import matplotlib.pyplot as plt
from tkinter import filedialog
from scipy.stats import multivariate_normal # these are for the line profile profile
import scipy
#--------- les frames ----------------
import FrameStruct
import FrameLbdaORMode
import FrameMapping
import FrameFileNameXY

class Mul_Ch_Wav_Mod_Sol(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        Frame.__init__(self, self.master)
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        # creates variable to be updated by the user. values are further obtained by the .get() method
        self.nC_1 = DoubleVar();self.nC_1.set(1.); self.nC_2 = DoubleVar();self.nC_2.set(1.); self.nC_3 = DoubleVar();self.nC_3.set(1.);
        self.nL1_1 = DoubleVar();self.nL1_1.set(1.);self.nL1_2 = DoubleVar();self.nL1_2.set(1.62);self.nL1_3 = DoubleVar();self.nL1_3.set(1.)
        self.nL2_1 = DoubleVar();self.nL2_1.set(1.62);self.nL2_2 = DoubleVar();self.nL2_2.set(1.62);self.nL2_3 = DoubleVar();self.nL2_3.set(1.62);
        self.nSub_1 = DoubleVar();self.nSub_1.set(1.61);self.nSub_2 = DoubleVar();self.nSub_2.set(1.61);self.nSub_3 = DoubleVar();self.nSub_3.set(1.61);
        self.TL_1 = DoubleVar();self.TL_1.set(2.3);self.TL_2 = DoubleVar();self.TL_2.set(2.);self.TChan = DoubleVar();self.TChan.set(3.1)
        self.WL = DoubleVar();self.WL.set(0.64);self.OPR = DoubleVar();self.OPR.set(1.97);self.vVaryH1LC_H1 = StringVar();self.vVaryH1LC_H1.set('1.0 to 4.0');
        self.vVaryH1LC_LC = StringVar();self.vVaryH1LC_LC.set('1.5 to 5.0');self.vVaryH1LC_H2 = DoubleVar();self.vVaryH1LC_H2.set(1.0);
        self.vVaryH1LC_SaveAs = StringVar();self.vVaryH1LC_SaveAs.set('Filename');self.vSimulat = DoubleVar();self.vSimulat.set(np.zeros((1,1)))
        self.LC_1= DoubleVar();self.LC_1.set(1.5); self.LC_2= DoubleVar();self.LC_2.set(5.0)
        self.H1_1=DoubleVar();self.H1_1.set(1.); self.H1_2=DoubleVar();self.H1_2.set(4.)
        self.H2value=DoubleVar();self.H2value.set(1.)
        self.grating_period = DoubleVar();self.grating_period.set(0.83);self.diffraction_mode = IntVar();self.diffraction_mode.set(1);
        self.Nmodes = IntVar();self.Nmodes.set(2)
        self.FileName=StringVar();self.FileName.set("filename.ecc")
        self.dir_label=StringVar();self.dir_label.set((os.getcwd()+"/"+self.FileName.get()).replace(os.sep, '/'))
        self.WorkDir=StringVar()
        #for the profile
        self.x_cut = DoubleVar();self.x_cut.set(3.1);self.y_cut = DoubleVar();self.y_cut.set(2.3)
        #self.vVaryH1LC_SaveAs_loc = StringVar();self.vVaryH1LC_SaveAs_loc.set('C:/Users/Home')#location to save
        #self.create_buttons()

    def create_widgets(self):
        topframe=Frame(self.master)
        topframe.pack()
        nbook=ttk.Notebook(topframe)
        f1=ttk.Frame(nbook)
        f2=ttk.Frame(nbook)
        nbook.add(f1,text="Simulation")
        nbook.add(f2,text="Mapping")
        nbook.pack()
        FrameDessous=Frame(self.master)
        FrameDessous.pack(side=BOTTOM)
        Button(FrameDessous, text="Close", fg='red', command=self.close_all).pack(side=LEFT)
        Button(FrameDessous, text="Close plots", fg='red', command= self.close_plots).pack(side=LEFT)

        #----  Tab 1 -------------  frame f1     
        tf1=ttk.Frame(f1)
        tf1.pack()
        FrameStruct.LaFrame(tf1,\
                self.nC_1,self.nC_2,self.nC_3,self.nL1_1,self.nL1_2,self.nL1_3,self.nL2_1,self.nL2_2,self.nL2_3,\
                self.nSub_1,self.nSub_2,self.nSub_3,self.TL_1,self.TL_2,self.TChan).pack()
        FrameLbdaORMode.LaFrame(tf1,self.WL,self.OPR,self.Nmodes).pack()
        bf1=ttk.Frame(f1)
        bf1.pack(side=BOTTOM)
        self.ButtonsSimulOne(bf1).pack()
        #----------- tab 2 ------------ frame f2
        tf2=ttk.Frame(f2)
        tf2.pack()
        FrameMapping.LaFrame(tf2,\
                self.H1_1, self.H1_2, self.LC_1,self.LC_2, self.H2value\
                ).pack(side=LEFT)
        FrameFileNameXY.LaFrame(tf2,\
                self.FileName, self.x_cut, self.y_cut,self.dir_label).pack(side=LEFT)
       
        bf2=ttk.Frame(f2)
        bf2.pack(side=BOTTOM)
        self.ButtonsMapping(bf2).pack()


    def ButtonsSimulOne(self,topframe):
        frame=Frame(topframe, bd=3,pady=2)
       # frame.pack()
        Button(frame, text="Solve", fg='green', command=self.Solve).pack(side=LEFT)
        Button(frame, text="Plot_indices", fg='green', command=self.Plot_indices).pack(side=LEFT)
        return frame

    def ButtonsMapping(self,topframe):
        frame=Frame(topframe, bd=3,pady=2)
        self.Save_as_en=Button(topframe, text="Save As",command=lambda:self.file_save_as());self.Save_as_en.pack(side=LEFT)
        Button(topframe, text="Simulate", fg='Green', command=self.Simulate).pack(side=LEFT)
        Button(topframe, text="Browse A File", command=self.fileDialog).pack(side=LEFT)
        Button(topframe, text="Plot Ecc.",command=lambda:self.plot_simulate_ecc()).pack(side=LEFT)
        Button(topframe, text="Plot S3",command=lambda:self.plot_simulate_ecc(What_plot='S3')).pack(side=LEFT)
        Button(topframe, text="Plot \u0394n", command=self.plot_simulate_dn).pack(side=LEFT)
        Button(topframe, text="Plot profile_ecc",fg='green', command=lambda:self.plot_line_profile()).pack(side=LEFT)
        Button(topframe, text="Plot profile_S3",fg='green', command=lambda:self.plot_line_profile(What_plot='S3')).pack(side=LEFT)
        return frame

    def Plot_indices(self):
        self.g = Channel(wl=self.WL.get(), pas=0.1, \
                       nc=self.nC_1.get(), nc_2=self.nC_2.get(), nc_3=self.nC_3.get(), Hc=0.8, \
                       LC=self.TChan.get(), LB=5., LB_R=5., \
                       n1B=self.nL1_1.get(), n1C=self.nL1_2.get(), n1D=self.nL1_3.get(), H1=self.TL_1.get(), \
                       n2B=self.nL2_1.get(), n2C=self.nL2_2.get(), n2D=self.nL2_3.get(), H2=self.TL_2.get(), \
                       nsub=self.nSub_1.get(), nsub_2=self.nSub_2.get(), nsub_3=self.nSub_3.get(), Hsub=2.,
                       OR=self.OPR.get())
        self.g.Traceindice()

    def fileDialog(self): # to brows the file
        self.vSimulat = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select A File",filetypes=[('ecc',"*.ecc"),('All files', '*')])
        if self.vSimulat:
            self.dr=np.loadtxt(self.vSimulat, delimiter=' ', comments='#')#self.df.to_numpy()
            self.line15=open(self.vSimulat, "r").readlines()[15]
            if 'Dimentions of the graph are:' in self.line15:
                X=self.line15.strip('#');X=X.strip('Dimentions of the graph are:');X=X.strip('\n')
                self.dimentions_var=np.fromstring(X, dtype=np.float, sep=',')
                self.LC_1.set(self.dimentions_var[0]);self.LC_2.set(self.dimentions_var[1])
                self.H1_1.set(self.dimentions_var[3]);self.H1_2.set(self.dimentions_var[4])
            else:
                messagebox.showinfo("Warning",'please check your file to see if the dimentions are in line 15')
        else:
            messagebox.showinfo("Warning",'Please choose a file to plot')
    def file_save_as(self):
        """Ask the user where to save the file and save it there. 
        Returns True if the file was saved, and False if the user
        cancelled the dialog.
        """
        self.save_as_path =filedialog.askdirectory(initialdir=os.getcwd(),title="Select As")#,filetypes=("json", "*.json")
        if self.save_as_path:
            os.chdir(self.save_as_path)
            self.dir_label.set((os.getcwd()+"/"+self.FileName.get()).replace(os.sep, '/'))
        else:
            messagebox.showinfo("Warning",'Please try again to save the file')
    def plot_line_profile(self,What_plot='ecc'):
        fig, main_ax = plt.subplots(figsize=(6, 6))
        divider = make_axes_locatable(main_ax)
        top_ax = divider.append_axes("top", 1.05, pad=0.1, sharex=main_ax)
        right_ax = divider.append_axes("right", 1.05, pad=0.1, sharey=main_ax)
        self.curX = self.x_cut.get()  # position of the vertical line  They should be always a float with one decimal like 1.1 or 1.2 etc...
        self.curY = self.y_cut.get()  # position of the horizontal line
        self.w_array = np.arange(self.LC_1.get(), self.LC_2.get(),0.1)  # introduce the x axis scale (xmin,xmax,step) we should know all these three parameters from the file we introduce in the  next step
        self.h_array = np.arange(self.H1_1.get(),self.H1_2.get(), 0.1)  # introduce the y axis scale (ymin,ymax,step)
        self.DnCB=((0.001*(float(self.WL.get()))*float(self.OPR.get()))/180)
        ecc = (self.DnCB/(self.dr+np.sqrt(self.DnCB**2+self.dr**2)))  # define eccentricity matrix
        # make some labels invisible
        top_ax.xaxis.set_tick_params(labelbottom=False)
        right_ax.yaxis.set_tick_params(labelleft=False)
        main_ax.set_xlabel('W (\u03BCm)')
        main_ax.set_ylabel('H (\u03BCm)')
        top_ax.set_ylabel(r'E$_{cc}$')
        right_ax.set_xlabel(r'E$_{cc}$')
        z_max = 1  # z.max()
        self.curX = np.around(float(self.curX), 2)
        self.curY = np.around(float(self.curY), 2)
        if What_plot=='S3':
            ecc=np.sin(2*np.arctan((np.real(ecc))**-1)) # this line is to plot S3
        im = main_ax.imshow(ecc,cmap="nipy_spectral", extent=[self.LC_1.get(), self.LC_2.get(), self.H1_1.get(),self.H1_2.get()], origin='lower')
        main_ax.autoscale(enable=False)
        right_ax.autoscale(enable=False)
        top_ax.autoscale(enable=False)
        right_ax.set_xlim(right=z_max)
        top_ax.set_ylim(top=z_max)
        self.v_line = main_ax.axvline(self.curX, color='b')
        self.h_line = main_ax.axhline(self.curY, color='g')
        self.v_prof, = right_ax.plot(ecc[:, (np.argmax(np.where(np.around(self.w_array, 2) == self.curX, self.w_array, 0)))], self.h_array,'b-')  # (np.argmax(np.where(np.around(self.h_array,2)==self.curY,self.h_array,0)))
        self.h_prof, = top_ax.plot(self.w_array, ecc[(np.argmax(np.where(np.around(self.h_array, 2) == self.curY, self.h_array, 0))), :],'g-')  # (np.argmax(np.where(np.around(self.w_array,2)==self.curX,self.w_array,0)))
        if What_plot=='S3':
            cax = divider.new_vertical(size="5%", pad=0.4, title="Stokes parameter S3")
        else:
            cax = divider.new_vertical(size="5%", pad=0.4, title="Eccentricity")
        fig.add_axes(cax)
        fig.colorbar(im, cax=cax, orientation="horizontal")
        cax.set_xlim(0, 1)
        cax.set
        # plt.savefig('colorbar_positioning_03.png', format='png', bbox_inches='tight')##################
        plt.show()
    def plot_simulate_ecc(self,What_plot='ecc'):
        if self.vSimulat:
            fig, self.ax = plt.subplots(figsize=(8, 6))
            #plt.title("Eccentricy as a function of channel dimensions")
            print("Optcal rotaion is: "+ str(self.OPR.get()))
            self.DnCB=((0.001*(float(self.WL.get()))*float(self.OPR.get()))/180)
            print("Circular bireferengence (CB) is: "+ str(self.DnCB))
            ecc=self.DnCB / (self.dr + np.sqrt(self.DnCB**2 + self.dr**2))
            if What_plot=='S3':
                ecc=np.sin(2*np.arctan((np.real(ecc))**-1)) # this line is to plot S3
            im = plt.imshow(ecc,cmap="nipy_spectral", extent=[self.LC_1.get(), self.LC_2.get(), self.H1_1.get(),self.H1_2.get()], origin='lower')
            plt.xlabel('W (\u03BCm)')
            plt.ylabel('H (\u03BCm)')
            divider = make_axes_locatable(self.ax)
            if What_plot=='S3':
                cax = divider.new_vertical(size="5%", pad=0.4, title="Stokes parameter S3")
            else:
                cax = divider.new_vertical(size="5%", pad=0.4, title="Eccentricity")
            fig.add_axes(cax)
            fig.colorbar(im, cax=cax, orientation="horizontal")
###################################################################################################### mshu x y labela wash karw
        # plt.savefig('colorbar_positioning_03.png', format='png', bbox_inches='tight')
            cid = fig.canvas.mpl_connect('button_press_event', self.onclick)
            plt.show()
            plt.close()
        else:
            messagebox.showinfo("Warning",'Please choose a file to plot')

    def plot_simulate_dn(self):
        if self.vSimulat:
            fig, self.ax = plt.subplots(figsize=(8, 6))
            #plt.title("Modal bireferengence as a function of channel dimensions")
            im = plt.imshow(self.dr,cmap="nipy_spectral",norm=colors.LogNorm(vmin=self.dr.min(),\
                    vmax=10*self.dr.max()),extent=[self.LC_1.get(), self.LC_2.get(), self.H1_1.get()\
                    ,self.H1_2.get()], origin='lower')
            plt.xlabel('W (\u03BCm)')
            plt.ylabel('H (\u03BCm)')
            divider = make_axes_locatable(self.ax)
            cax = divider.new_vertical(size="5%", pad=0.4, title="Modal bireferengence")
            fig.add_axes(cax)
            fig.colorbar(im, cax=cax,orientation="horizontal")
            # plt.savefig('colorbar_positioning_03.png', format='png', bbox_inches='tight')
            cid = fig.canvas.mpl_connect('button_press_event', self.onclick)
            plt.show()
            plt.close()
        else:
            messagebox.showinfo("Warning",'Please choose a file to plot')

    def onclick(self,event):
        print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %(event.button, event.x, event.y, event.xdata, event.ydata))
        self.ax.plot(event.xdata, event.ydata, 'k+',markersize=15)
        plt.show()

    def close_all(self):
        # Button(self.root,text = 'Click Me', command=lambda:[self.funcA(), self.funcB(), self.funcC()])
        self.master.destroy()
        plt.close('all')
    def Solve(self):
        self.g = Channel(wl=self.WL.get(), pas=0.1, \
                       nc=self.nC_1.get(), nc_2=self.nC_2.get(), nc_3=self.nC_3.get(), Hc=0.8, \
                       LC=self.TChan.get(), LB=5., LB_R=5., \
                       n1B=self.nL1_1.get(), n1C=self.nL1_2.get(), n1D=self.nL1_3.get(), H1=self.TL_1.get(), \
                       n2B=self.nL2_1.get(), n2C=self.nL2_2.get(), n2D=self.nL2_3.get(), H2=self.TL_2.get(), \
                       nsub=self.nSub_1.get(), nsub_2=self.nSub_2.get(), nsub_3=self.nSub_3.get(), Hsub=2.,
                       OR=self.OPR.get())
        self.g.Calcule(Nmodes=self.Nmodes.get())
        #self.g.Intensite()
        plt.show()

    def NumOf_guided_modes(self): # This will print angles which can give coupled light.
        print("Coupling neff is calculated with equation\n n_eff=n_top.sin(\u03B8) + (m.(\u03BB/\u039B) \n where "
              "n_eff is effective refractive index, n_top is refractive index of the cover\n"
              "\u03B8 is coupling angle,m is diffraction mode, \u03BB is wavelength, and \u039B is grating period")
        self.g = Channel(wl=self.WL.get(), pas=0.1, \
                       nc=self.nC_1.get(), nc_2=self.nC_2.get(), nc_3=self.nC_3.get(), Hc=0.8, \
                       LC=self.TChan.get(), LB=5., LB_R=5., \
                       n1B=self.nL1_1.get(), n1C=self.nL1_2.get(), n1D=self.nL1_3.get(), H1=self.TL_1.get(), \
                       n2B=self.nL2_1.get(), n2C=self.nL2_2.get(), n2D=self.nL2_3.get(), H2=self.TL_2.get(), \
                       nsub=self.nSub_1.get(), nsub_2=self.nSub_2.get(), nsub_3=self.nSub_3.get(), Hsub=2.,
                       OR=self.OPR.get())
        if self.g.NmaxPlan()==0: # blow H2==0.9 NmaxPlan is 0 and it does not give good value.
            messagebox.showinfo("Hey", 'It looks like NmaxPlan is {}'.format(self.g.NmaxPlan()))
            pass
        else:
            for i in np.real((self.g.NumOf_guidedModes(Nmodes=self.Nmodes.get())[1:])):
                print("For the {:.4f} mode there is one coupling angle at {:.4f}".format(i,self.Nmode_effective(i)))
    
    def Nmode_effective(self,n_eff): # to find n_e that is effective refractive index of the grating
        '''This method returns guided modes of the structure (not leaky modes)'''
        #print(self.grating_period,self.diffraction_mode)
        n_top=np.average(np.array([self.nC_1.get(),self.nC_2.get(),self.nC_3.get()]))
        m=self.diffraction_mode.get(); WL=self.WL.get(); GP=self.grating_period.get()
        TheSin=( n_eff-m*WL/GP )/n_top
        if np.abs(TheSin) >1:
            theta = 0
        else:
            theta=np.rad2deg(np.arcsin(TheSin) )
        return theta

    def Simulate(self):
        if messagebox.askyesno("Warning! ", 'This may take several minutes\n Are you sure you want to continue?'):
            messagebox.showinfo("Simulation",'You can see the see the remaining time in the run window')
            self.g = Channel(wl=self.WL.get(), pas=0.1, \
                       nc=self.nC_1.get(), nc_2=self.nC_2.get(), nc_3=self.nC_3.get(), Hc=0.8, \
                       LC=self.TChan.get(), LB=5., LB_R=5., \
                       n1B=self.nL1_1.get(), n1C=self.nL1_2.get(), n1D=self.nL1_3.get(), H1=self.TL_1.get(), \
                       n2B=self.nL2_1.get(), n2C=self.nL2_2.get(), n2D=self.nL2_3.get(), H2=self.TL_2.get(), \
                       nsub=self.nSub_1.get(), nsub_2=self.nSub_2.get(), nsub_3=self.nSub_3.get(), Hsub=2.,
                       OR=self.OPR.get())
            self.g.H2 = self.H2value.get()
            self.g.VariaXY(X0=self.LC_1.get(), X1=self.LC_2.get(), dX=0.1, Y0=self.H1_1.get(), Y1=self.H1_2.get(), dY=0.1, fich=self.FileName.get())
        else:
            messagebox.showinfo("Canceled",'You have successfully canceled the simulation')
    def close_plots(self):
        plt.close('all')
        
if __name__ == '__main__':
    root = Tk()  # we car write any name instead of root
    root.title('Multilayer channel waveguide mode solver')
    # root.iconbitmap('rib_waveguide.ico')
    #root.geometry("750x900")
    app = Mul_Ch_Wav_Mod_Sol(root)
    app.mainloop()
