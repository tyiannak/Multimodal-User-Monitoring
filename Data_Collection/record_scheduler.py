# -*- coding: utf-8 -*-
from threading import Timer
import subprocess
import sys

'''
   A simple script to run subscripts(chairlogger && mouselogger && keylogger)at the same time
'''
if __name__=='__main__':
   rec1 = "python3 /home/alex/Desktop/Test_Data/Logger/chairlogger.py"
   rec2 = "& python3 /home/alex/Desktop/Test_Data/Loggers/keylogger.py"
   rec3 = "& python3 /home/alex/Desktop/Test_Data/Loggers/mouselogger.py"
   rec = rec1+' '+rec2+' '+rec3
   subprocess.run(rec, shell=True)
