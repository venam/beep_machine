import sys, os

#A ajouter les rondes,blanches,noires,croches,dbl-croches,trpl-croches,pointee
#les pauses
class beeper():


    def __init__(self):
        self.output = ""
        self.delay  = "20"
        self.length = "120"

    def E2(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 82.407 "+"-l "+length+" -D "+delay

    def F2(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 87.31 "+"-l "+length+" -D "+delay

    def F2_(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 92.50 "+"-l "+length+" -D "+delay

    def G2(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 98.00 "+"-l "+length+" -D "+delay

    def G2_(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 103.83  "+"-l "+length+" -D "+delay

    def A2(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 110.00 "+"-l "+length+" -D "+delay

    def A2_(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 116.54 "+"-l "+length+" -D "+delay

    def B2(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 123.47 "+"-l "+length+" -D "+delay

    def C3(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 130.81 "+"-l "+length+" -D "+delay

    def C3_(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 138.59 "+"-l "+length+" -D "+delay

    def D3(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 146.83 "+"-l "+length+" -D "+delay

    def D3_(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 155.56 "+"-l "+length+" -D "+delay

    def E3(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 164.81 "+"-l "+length+" -D "+delay

    def F3(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 174.61 "+"-l "+length+" -D "+delay

    def F3_(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 185.00 "+"-l "+length+" -D "+delay

    def G3(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 196.00 "+"-l "+length+" -D "+delay

    def G3_(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 207.65 "+"-l "+length+" -D "+delay

    def A3(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 220.00  "+"-l "+length+" -D "+delay

    def A3_(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 233.08 "+"-l "+length+" -D "+delay

    def B3(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 246.94 "+"-l "+length+" -D "+delay

    def C4(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 261.63 "+"-l "+length+" -D "+delay

    def C4_(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 277.18 "+"-l "+length+" -D "+delay

    def D4(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 293.67 "+"-l "+length+" -D "+delay

    def D4_(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 311.13 "+"-l "+length+" -D "+delay

    def E4(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 329.63  "+"-l "+length+" -D "+delay

    def F4(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 349.23 "+"-l "+length+" -D "+delay

    def F4_(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 369.99 "+"-l "+length+" -D "+delay

    def G4(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 392.00 "+"-l "+length+" -D "+delay

    def G4_(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 415.30 "+"-l "+length+" -D "+delay

    def A4(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 440 "+"-l "+length+" -D "+delay

    def A4_(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 466.16 "+"-l "+length+" -D "+delay

    def B4(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 493.88 "+"-l "+length+" -D "+delay

    def C5(self, delay="",length=""):
        if delay=="" or length =="":
            delay  = self.delay
            length = self.length
        self.output+=" -n -f 523.25 "+"-l "+length+" -D "+delay

   #This might or might not work, or work only with the file generated by this module specially
    def read(self,file_location):
        file_content = open(file_location,'r').read()
        file_content = file_content.replace("#!/bin/sh\n","")
        file_content = file_content.split("-n -f ")
        file_content.remove("beep -l 1  ")

        for notes in file_content:
            notes = notes.replace("-l ","").replace("-D ","")
            notes = notes.split(" ")
            for description in notes:
                print description

    def back(self):
        splited = self.output.split("-n -f ")
        splited.pop()
        self.output = ""
        for a in splited:
            if a!=" ":
                self.output+= " -n -f " + a
            print a


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
                elif a                      == 'C#' or a=='c#':
                    note = "277.2"
                elif a                      == 'D#' or a=='d#':
                    note = "311.1"
                elif a                      == 'F#'  or a=='f#':
                    note = "370.0"
                elif a                      == 'G#' or a=='g#':
                    note == "415.3"
                elif a                      == 'A#'  or a=='a#':
                    note == "466.2"
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
        os.system("beep -l 1  "+self.output)




