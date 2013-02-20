import sys, os

class beeper():
    def __init__(self):
        self.output = " "

    def A(self, delay="2",length="3"):
        self.output+=" -n -f 440.0 "+"-l "+length+" -D "+delay


    def B(self, delay="2",length="3"):
        self.output+=" -n -f 493.9 "+"-l "+length+" -D "+delay


    def C(self, delay="2",length="3"):
        self.output+=" -n -f 261.6 "+"-l "+length+" -D "+delay


    def D(self, delay="2",length="3"):
        self.output+=" -n -f 293.7 "+"-l "+length+" -D "+delay


    def E(self, delay="2",length="3"):
        self.output+=" -n -f 329.6 "+"-l "+length+" -D "+delay


    def F(self, delay="2",length="3"):
        self.output+=" -n -f 349.2 "+"-l "+length+" -D "+delay


    def G(self, delay="2",length="3"):
        self.output+=" -n -f 392.0 "+"-l "+length+" -D "+delay

    def clear(self):
        self.output=" "

    def run(self,file=""):
        if(file!=""):
            open(file,'w').write("#!/bin/sh\nbeep -l 1"+self.output)
        os.system("beep -l 1"+self.output)




