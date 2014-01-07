# -*- coding: utf-8 -*-
"""
Created on Tue Jan 07 14:52:57 2014

@author: shuhaoye
"""
import os
import numpy
import matplotlib.pyplot as plt

class Doscar:
    def __init__(self,dosFileName,spin=2,path=None,onlyAttr=False):
        self.dosFileName=dosFileName;
        #tag=None for the Doscar is not initialized completedly
        self.tag=False;  
        if not (spin==1 or spin==2):
            print "spin must be 1 or 2";
            return;
        self.spin=spin;
        if not path:
            self.path=os.getcwd();
        self.init(onlyAttr);
        
    def init(self,onlyAttr=False):
        dosFile=None;
        try:
            dosFile=open(os.path.join(self.path,self.dosFileName));
            for i in range(0,5):
                dosFile.readline();
            attrLine=dosFile.readline();
            self.attr=[float(x) for x in attrLine.split()];
            if len(self.attr)!=5:
                print self.dosFileName,"broken";
                return;
            self.fermi=self.attr[3];
            self.num=int(self.attr[2]);
            if onlyAttr:
                return;
            self.dos=numpy.zeros((self.num,self.spin));
            self.energy=numpy.linspace(self.attr[1],self.attr[0],self.num);
            for i in range(0,self.num):
                dosLine=dosFile.readline();
                self.dos[i,:]=[float(x) for x in dosLine.split()[1:1+self.spin]];
            self.tag=True;
        finally:
            if dosFile:
                print self.dosFileName,"closed";
                dosFile.close();
    def plot(self,eRange=[-10,10],filename=None):
        if not self.tag:
            print "The Doscar object was initialized properly.";
            return;
        plt.xlim(eRange);
        plt.plot(self.energy-self.fermi,self.dos[:,0]);
        if self.spin==2:
            plt.plot(self.energy-self.fermi,-self.dos[:,1]);
        if not filename:
            filename=self.dosFileName;
        plt.xlabel("E(eV)");
        plt.ylabel("DOS(eV$^{-1}$)");
        plt.savefig(filename+'.jpg');
        
if __name__=='__main__':
    a=Doscar('DOSCAR');
    a.plot();