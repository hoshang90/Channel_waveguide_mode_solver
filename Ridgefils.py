#!/usr/bin/python3
"""Fully vectorial finite-difference mode solver example."""
import numpy as np
from Channels_multilayer import Channel
class Ridge(Channel):
    """ modes propres dans guide canal de type ridge 
    fils de Channels ->Channel
    indice effectifs: https://www.computational-photonics.eu/eims.html
    ___________________________________
        nc, Hc
    <-- LB --> <-- LC --> <-- LB -->
               _________
        nc    |   ng    | nc, H1
     ----------          -------------   
                 ng  , H2
    -------------------------------------
        nsub,Hsub
    _______________________________________
    Usage:
 g=ra.Ridge(wl=0.64,pas=0.1, nc=1.,Hc=0.8,
    LB=5,LC=3.1,ng=1.62,H1=2.3,H2=2., nsub=1.61,Hsub=2,OR=4)
 g.Traceindice()
 g.Calcule(Nmodes=2,verbose=True,trace=True) => calcule des modes [0..1]
 g.TraceMode(0)
 g.Intensite()
 g.VariaXY(self,X0=0.1, X1=5, dX=0.2,vX='LC',
                Y0=0.1,Y1=5,dY=0.2,vY='H1',fich="dataDn")
 
    """
    def __init__(self,wl=0.64,pas=0.1,\
            nc=1.,Hc=0.8,\
            LB=5,LC=3.1,\
            ng=1.62,H1=2.3, H2=2.,\
            nsub=1.61,Hsub=2,OR=4
            ):
        # --------- ridge
        Channel.__init__(self,wl=wl,pas=pas,nc=nc,nc_2=nc,nc_3=nc\
            ,Hc=Hc,LB=LB,LB_R=LB,LC=LC,n1B=nc,n1D=nc,n1C=ng,H1=H1,\
            n2B=ng,n2D=ng,n2C=ng,H2=H2,nsub=nsub,nsub_2=nsub,nsub_3=nsub,Hsub=Hsub,OR=OR)
        

    def LaStructure(self):
        """ Dessine la structure sur le terminal """
        reponse="-"*40+"\n"
        reponse+=" nc={:.3f}, Hc={}\n".format(np.sqrt(self.nc2),self.Hc)
        reponse+="<- LB={} -->| <-  LC={}   ->| <- LB ->\n".format(self.LB,self.LC)
        reponse+=" "*12+"-"*14+"\n"
        reponse+=" nc={:.3f}  |   ng={:.3f}   | nc , H1={}\n".\
                format(np.sqrt(self.n1B2),np.sqrt(self.n1C2),self.H1)
        reponse+="-"*12+" "*14+"-"*10+"\n"
        reponse+=" "*10+"ng={:.3f}, H2={:.2f}\n".\
                format(np.sqrt(self.n2B2),self.H2)
        reponse+="-"*40+"\n"
        reponse+=" "*10+"nsub={:.3f}, Hsub={}\n".format(np.sqrt(self.ns2),self.Hsub)
        reponse+="-"*40+"\n"
        return reponse
        


#if __name__ == '__main__':
 #   g=Ridge()
    #np.set_printoptions(precision=2)
    #print(g.epsfunc(g.x,g.y))
    #g.plotindice()
  #  g.Calcule()
    #g.TraceMode()

