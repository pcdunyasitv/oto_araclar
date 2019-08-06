#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import py_compile

os.system("apt-get install figlet")
os.system("clear")
os.system("firlet Derleme Programı")

derle = raw_input("Program İsmini Girin : ")

py_compile.compile(derle)
