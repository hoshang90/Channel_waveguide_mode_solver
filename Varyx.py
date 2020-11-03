#This is just plot evolution of TE0,TM0 neff and DN from the VariX method by changing the variables. 
from Channels_multilayer import Channel
g=Channel(wl=0.64,pas=0.1,nc=1., nc_2=1., nc_3=1.,Hc=0.8,\
        LB=5, LC=3.1,LB_R=5,n1B=1.,n1C=1.62,n1D=1.,H1=2.3,\
        n2B=1.62,n2C=1.62,n2D=1.62,H2=2.,\
        nsub=1.615,nsub_2=1.615,nsub_3=1.615,Hsub=2.,OR=2.5)
#g.Calcule()
g.VariaX(X0=0.5,X1=8,dX=0.1,variable='LC',trace=True,Show_Struct=False,fich="Data")
