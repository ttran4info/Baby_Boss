#!/usr/bin/python

import sys

def get_match(str1,str2):
#	str1= ${str1} 
#'Ad Groups (86)'
#	str2=${str2} 
#'86
	str1=str(str1)
	str2=str(str2)
	found= str1.find(str2)
	if found!=-1 and isinstance( str2, int ):
		return int(str2)
	elif found!=-1 and isinstance( str2, str ) and len(str2)<=2:
		return int(str2)
	elif found!=-1 and isinstance( str2, str ) and len(str2)>2:
		return str2
	else:	
		return sys.exit(1)
                #return "no matches found"