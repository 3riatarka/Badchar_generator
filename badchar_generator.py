#!/bin/env python
# -*- encoding: utf-8 -*-

badcharlist = ''

i = 0 
while i <256:
    hexchar = 'x{0:02x}'.format(i)
    badcharlist += '\\'+hexchar
    i+= 1

print(badcharlist)
