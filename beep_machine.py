import sys, os

#A ajouter les rondes,blanches,noires,croches,dbl-croches,trpl-croches,pointee
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

    def beep(self,string):
        string = string.split(" ")
        if(len(string)%3!=0):
            print len(string)
            print "error in arguments"
            return
        i         = 0
        for a in string:
            if i>2:
                i=0
            if i==0:
                note = ""
                """
                A. - noire pointee
                A) - croche
                A))- couble croche
                Ao - ronde
                A| - blanche
                """
                if a                        == 'A' or a == 'a':
                    note = "440.0"
                elif a                      == 'B' or a == 'b':
                    note = "493.9"
                elif a                      == 'C' or a == 'c':
                    note = "261.6"
                elif a                      == 'D' or a == 'd':
                    note = "293.7"
                elif a                      == 'E' or a == 'e':
                    note = "329.6"
                elif a                      == 'F' or a == 'f':
                    note = "349.2"
                elif a                      == 'G' or a == 'g':
                    note = "392.0"
                else:
                    note = a
                self.output+=" -n -f "+note
            elif i==1:
                self.output+=" -l "+a
            elif i==2:
                self.output+=" -D "+a+" "
            i+=1

    def clear(self):
        self.output=" "

    def run(self,file=""):
        if(file!=""):
            open(file,'w').write("#!/bin/sh\nbeep -l 1"+self.output)
        os.system("beep -l 1"+self.output)




