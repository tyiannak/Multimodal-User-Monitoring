# -*- coding: utf-8 -*-
import key_log_functions as lf
from pynput import keyboard
import logging
import time
import os
import sys

if __name__=='__main__':

    fname = lf.get_date()+'.txt'
    raw_data = lf.create_directories()
    fname = os.path.join(raw_data,fname)
    logging.basicConfig(filename=fname,level=logging.DEBUG,format="%(asctime)s    %(message)s")
    
    with keyboard.Listener(on_press = lf.on_press_keys) as listener:
        listener.join()
