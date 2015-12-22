# -*- coding:GBK -*-
__author__ = 'Dennie'
'file read and write'

import os
class fileRead_Write(object):
	def ReadFileTxt(self):
		contents = []
		try:
			self.Rfilename = raw_input('Enter file name:')
			self.fobj = open(self.Rfilename,'r')
			for self.eachline in self.fobj:
				contents.append(self.eachline)
			self.fobj.close()
		except IOError, self.e:
			print('File open Error!',self.e)
		return contents
	def makeFile(self):
		while True:
			self.Wfilename = raw_input('Enter file name to Creat:')
			if os.path.exists(self.Wfilename):
				print("ERROR:'%s' File already exists" % self.Wfilename)
			else:
				break
		self.fileName = open(self.Wfilename,'w')
		self.WriteContents = self.ReadFileTxt()
		self.fileName.writelines(self.WriteContents)
		self.fileName.close()
		print("Successful:Contents write in '%s'" % self.Wfilename)

if __name__ == '__main__':
	obj = fileRead_Write()
	obj.makeFile()