#This is just plot evolution of TE0,TM0 neff and DN from the VariX method by changing the variables. 
from Channels_multilayer import Channel
g=Channel(wl=0.64,pas=0.1,nc=1., nc_2=1., nc_3=1.,Hc=0.8,\
        LB=5, LC=3.1,LB_R=5,n1B=1.,n1C=1.62,n1D=1.,H1=2.3,\
        n2B=1.62,n2C=1.62,n2D=1.62,H2=2.,\
        nsub=1.61,nsub_2=1.61,nsub_3=1.61,Hsub=2.,OR=2.5)
#g.Calcule()
g.VariaX(X0=1,X1=1.33,dX=0.01,variable='nc',trace=True,Show_Struct=False,fich="Data")
