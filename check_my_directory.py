#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os


def freespace(p):
    """
    Returns the number of free bytes on the drive that p is on
    """
    s = os.statvfs(p)
    return s.f_bsize * s.f_bavail

def freespaceGB(p):
	return freespace(p)/(1024*1024*1024)

try:
	dir = sys.argv[1]
except:
	print "Specify directory on command line, please"
	sys.exit(0)

print "Analysis of", dir

#if not os.path.exists(dir):
if not os.path.isdir(dir):
	print dir, "does not exist"
	sys.exit(0)

print "Free space (GB):", int(freespaceGB(dir))

testfilename = os.path.join(dir, "blablajkjasldkjfkljklasdjlfk")
with open(testfilename,'w') as fout:
	fout.write('foo bar')
os.remove(testfilename)


print "Create file with unicode charachters in filename"
testfilename = os.path.join(dir, u'Hello ∆ ⋂ ∭ there 你好 世界 world.txt')
with open(testfilename,'w') as fout:
	fout.write('foo bar')
os.remove(testfilename)



# Can we unpack a rar file with a unicode filename inside?
'''
>>> file = open("unicode-file.rar", "r") 
>>> ba = bytearray(file.read())
>>> print ba
bytearray(b'Rar!\x1a\x07\x00\xcf\x90s\x00\x00\r\x00\x00\x00\x00\x00\x00\x00\xbf\'t \x82x\x00\x07\x00\x00\x00\x07\x00\x00\x00\x034\x01F\xbe\xe7\xabbJ\x1d0X\x00\xa4\x81\x00\x00Hello \xe2\x88\x86 \xe2\x8b\x82 \xe2\x88\xad there \xe4\xbd\xa0\xe5\xa5\xbd \xe4\xb8\x96\xe7\x95\x8c world.txt\x00"\xd1\x04\x06 \xc2\x10 - t\x00here( `O}Y \xa0\x16NLu w\x00orld\x00.txtfoo bar\xc4={\x00@\x07\x00')
'''

# the contents (bytes) of the rar file
ba = bytearray(b'Rar!\x1a\x07\x00\xcf\x90s\x00\x00\r\x00\x00\x00\x00\x00\x00\x00\xbf\'t \x82x\x00\x07\x00\x00\x00\x07\x00\x00\x00\x034\x01F\xbe\xe7\xabbJ\x1d0X\x00\xa4\x81\x00\x00Hello \xe2\x88\x86 \xe2\x8b\x82 \xe2\x88\xad there \xe4\xbd\xa0\xe5\xa5\xbd \xe4\xb8\x96\xe7\x95\x8c world.txt\x00"\xd1\x04\x06 \xc2\x10 - t\x00here( `O}Y \xa0\x16NLu w\x00orld\x00.txtfoo bar\xc4={\x00@\x07\x00')
rarfilename = os.path.join(dir, "testfileJKLJALKJFJLKFJLJS.rar")
with open(rarfilename,'w') as fout:
	fout.write(ba)

cmd = "unrar x -y " + rarfilename + " " + dir	# unrar x -y /home/mydir/testfile.rar /home/mydir/
print "cmd is ", cmd

unrarallok = False
for thisline in os.popen(cmd).readlines():
	if thisline.find("All OK")>=0:
		print "OK"
		unrarallok = True
		break
if unrarallok:
	print "Unrar with unicode went well!"
else:
	print "Unrar with unicode: failed!"
os.remove(rarfilename)
# to do: remove the unpacked file ...
os.remove('Hello ∆ ⋂ ∭ there 你好 世界 world.txt')



# Check which filesystem type it's on. FAT considered harmful (for big files)

if sys.platform.find('linux')>=0:
	# On Linux:
	# df -T /home/sander/weg

	'''
	$ df -T /media/sander/INTENSO
	Filesystem     Type 1K-blocks      Used Available Use% Mounted on
	/dev/sda1      vfat 488263616 163545248 324718368  34% /media/sander/INTENSO
	'''

	cmd = "df -T " + dir
	for thisline in os.popen(cmd).readlines():
		#print thisline
		if thisline.find('/')==0:
			fstype = thisline.split()[1]
			print "File system type:", fstype
			if fstype.lower().find('fat') >= 0:
				print "Warning: FAT found"











																																																																																																																																																																																																									
