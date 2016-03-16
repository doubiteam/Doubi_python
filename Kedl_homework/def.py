# -*- coding:GBK -*-
__author__ = 'Dennie'
def inter(s1,s2):
	res = []
	for x in s1:
		if x in s2:
			res.append(x)
	return res
s1 = 'spam'
s2 = 'soam'
print (inter(s1,s2))