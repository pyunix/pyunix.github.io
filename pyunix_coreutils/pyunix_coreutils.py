import argparse
import os
import sys

#class coreutils:
#   def __init__(self):
#       pass
    
def ls():
    PYUArgs = argparse.ArgumentParser(
                    prog='ls',
                    description='List information about files',
                    epilog='PyUnix ls')
    PYUArgs.add_argument('-a','--all',action='store_true', help='do not ignore entries starting with .')
    PYUArgs.add_argument('-l',action='store_true',help='use a long listing format')
    PYUArgs.add_argument('files', nargs='*')
    PYUParsed = PYUArgs.parse_args()
    #print(PYUParsed)
    
    if PYUParsed.files == None:
        PYUFiles = "."
    else:
        PYUFiles = PYUParsed.files
    

    for PYUY in PYUFiles:
#        if len(PYUParsed.files) >= 2:
#            print(f"{PYUY}:")
        for PYUX in os.listdir(PYUY):
            if PYUParsed.l == True:
                PYUStat = os.stat(PYUX)
                print(f"{PYUStat.st_mode} {PYUStat.st_nlink} {PYUStat.st_uid} {PYUStat.st_gid} {PYUStat.st_size}\t{PYUStat.st_mtime}\t{PYUX}")
            else :
                print(PYUX)