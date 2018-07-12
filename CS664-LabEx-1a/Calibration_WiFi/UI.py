# -*- coding: utf-8 -*-
'''
  Copyright (C) 2018 GT Silicon Pvt Ltd

  Licensed under the Creative Commons Attribution 4.0
  International Public License (the "CCBY4.0 License");
  you may not use this file except in compliance with the License.
  You may obtain a copy of the License at
  https://creativecommons.org/licenses/by/4.0/legalcode
'''

import Tkinter
from Tkinter import *
import ttk
from ttk import *


def okbtn():
    stop1 = file("stop", 'w')
    stop1.close()
    root.destroy()

root = Tkinter.Tk()
Label(root,text='Plesase press ok  to stop data logging').pack()
Button(root,text='OK',command=okbtn).pack()

root.mainloop()