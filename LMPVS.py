from os import listdir
from os.path import isfile, join, isdir
from sys import stdin
import sys 
import subprocess, shlex
from subprocess import check_output

# Declaring a global variable for the PVS path
PVSPATH=check_output(["pwd"])
PVSPATH=PVSPATH[:len(PVSPATH)-1]+'/'

# List all the packages on the PVS path
def list_packages():	
	basepath=PVSPATH
	packages=[]
	
	paths=listdir(basepath)
	
	for f in paths:
		if 'lib' in str(f):
			dir=basepath+f+'/'
			pks=listdir(dir)
			for d in pks:
				if isdir(dir+d):
					packages.append(d)
					#print d
	print ('Total packages ' + str(len(packages)))
	ans=raw_input('Do you want to print all packages? (Y/N) ')
	if ans=='Y' or ans=='y':
		packages.sort()
		for f in packages:
			print f

# List all the theories on the PVS path
def list_theories():
	basepath=PVSPATH
	theories=[]
	
	paths=listdir(basepath)
	
	for f in paths:
		if 'lib' in str(f):
			dir=basepath+f+'/'
			pks=listdir(dir)
			for d in pks:
				if isdir(dir+d):
					dir2=dir+d+'/'
					ths=listdir(dir2)
					for t in ths:
						if not(isdir(t)) and t not in theories:
							theories.append(t)
	print ('Total theories ' + str(len(theories)))
	ans=raw_input('Do you want to print all theories? (Y/N) ')
	if ans=='Y' or ans=='y':
		for f in theories:
			print f

# Update the nasalib, cloning the github
def uptade():
	ans=raw_input('Indicate the path to save the repository: ')
	args=shlex.split('git clone https://github.com/samowre/PVS.git /tmp/repo')
	p=subprocess.Popen(args)
	TerminateProcess()

options={"list":list_packages,"list-all":list_theories}

options[sys.argv[1]]()
	
