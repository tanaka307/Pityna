# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 15:13:19 2022

@author: OASoft
"""

from PyQt5 import uic

fin = open('qt_pityna.ui', 'r', encoding='utf-8')
fout = open('qt_pitynaUI.py', 'w', encoding='utf-8')
uic.compileUi(fin, fout)
fin.close()
fout.close()