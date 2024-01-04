#!/usr/bin/env python3

#bring in shell utilites
import shutil
#access low leverl OS
import os

def main():
    """called at runtime"""
    #start in this directory
    os.chdir('/home/student/mycode/')

    #move raynor from mycode to ceph storage
    shutil.move('raynor.obj', 'ceph_storage/')
    
    #program pauses here for input
    xname = input('What is the new name for kerrigan.obj? ')

    #move kerrigan and change name to xname input
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
