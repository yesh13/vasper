# -*- coding: utf-8 -*-
"""
Created on Tue Jan 07 19:02:14 2014

@author: shuhaoye
"""

import doscar
import eigenval


class PlotHelper:
    def __init__(self,filename,spin=2):
        self.filename=filename;
        self.spin=spin;
        self.lim=[-5,5];
        self.eigFileName=self.getEigFileName();
        self.dosFileName=self.getDosFileName();
    def setLim(self,lim):
        self.lim=lim;
    def getEigFileName(self):
        return "EIGENVAL";
    def getDosFileName(self):
        return "DOSCAR";
    def plotDoscar(self):
        if not "mDos" in dir(self):
            self.mDos=doscar.Doscar(self.dosFileName,spin=self.spin);
        if self.mDos.tag==False:
            self.mDos.init();
        self.mDos.plot(eRange=self.lim)
    def plotEigenval(self):
        if not "mDos" in dir(self):
            self.mDos=doscar.Doscar(self.dosFileName,spin=self.spin,onlyAttr=True);
        
        if not "mEig" in dir(self):
            self.mEig=eigenval.Eigenval(self.eigFileName,spin=self.spin);
        self.mEig.plot(eRange=self.lim,fermi=self.mDos.fermi);


if __name__=="__main__":
    a=PlotHelper("ddd");
    a.setLim([-0.75,0.75]);
    a.plotEigenval();
    a.plotDoscar();