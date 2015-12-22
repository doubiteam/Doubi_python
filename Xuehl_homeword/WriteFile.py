# -*-coding:utf-8-*-
'''
Created on 2015-12-21-

@author: Xue.HL
'''

fa = file("C:\\stu\\a.txt", "r+")
fb = file("C:\\stu\\b.txt", "r+")
fb.writelines(fa.readlines())
fa.close()
fb.close()  