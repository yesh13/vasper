# -*- coding: utf-8 -*-
"""
Created on Tue Jan 07 16:55:32 2014

@author: shuhaoye
"""

import os
import numpy
import matplotlib.pyplot as plt

class Eigenval:
    def __init__(self,eigFileName,spin=2,path=None):
        self.eigFileName=eigFileName;
        #tag=None for the Eigenval is not initialized completedly
        self.tag=False;  
        if not (spin==1 or spin==2):
            print "spin must be 1 or 2";
            return;
        if not path:
            path=os.getcwd();
        eigFile=None;
        self.spin=spin;
        try:
            eigFile=open(os.path.join(path,eigFileName));
            for i in range(0,5):
                eigFile.readline();
            attrLine=eigFile.readline();
            self.attr=[float(x) for x in attrLine.split()];
            if len(self.attr)!=3:
                print eigFileName,"broken";
                return;
            self.nband=int(self.attr[2]);
            self.nkpoint=int(self.attr[1]);
            self.eig=numpy.zeros((spin,self.nband,self.nkpoint));
            for ik in range(0,self.nkpoint):
                eigFile.readline();
                eigFile.readline();
                for iband in range(0,self.nband):  
                    eigLine=eigFile.readline();
                    self.eig[:,iband,ik]=\
                        [float(x) for x in eigLine.split()[1:1+spin]];
            self.tag=True;
        finally:
            if eigFile:
                print eigFileName,"closed";
                eigFile.close();
    def plot(self,eRange=[-10,10],fermi=0,filename=None):
        if not self.tag:
            print "The Eigenval object was initialized properly.";
            return;
        plt.ylim(eRange);
        for ispin in range(0,self.spin):
            for iband in range(0,self.nband):
                if ispin:
                    color='r';
                else:
                    color='g';
                plt.plot(self.eig[ispin,iband,:],color);
        if not filename:
            filename=self.eigFileName;
        plt.xlabel("K");
        plt.ylabel("EIGEN(eV)");
        plt.savefig(filename+'.jpg');
        
if __name__=='__main__':
    a=Eigenval('EIGENVAL');
    print a.attr;
    a.plot();