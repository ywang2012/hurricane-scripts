#!/bin/env python

import os, sys

date = sys.argv[1]
case = sys.argv[2]
var  = sys.argv[3]

basedir = "/scratch/ywang/hurr2"

#print date,case,var

for seq in range(1,866) :
  frm = "%s%03d.png" %(var,seq)
  fam = os.path.join(basedir,date,case,var,frm)
  if not os.path.lexists(fam) :
    fsec = (seq-1)*300
    print fam
    print "%s missing, forecast hour %d, %d seconds" % (frm, fsec//3600, fsec%3600)
'''
for seq in range(1,866) :
  fam = os.path.join(basedir,date,case,var+'_big',frm)
  if not os.path.lexists(fam) :
    fsec = (seq-1)*300
    print fam
    print "%s missing in Big directory, forecast hour %d, %d seconds" % (fam, fsec//3600, fsec%3600)
'''
