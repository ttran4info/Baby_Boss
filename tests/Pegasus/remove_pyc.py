#removing files containing compiled code/ byte code
def rm_pyc():
	import os
	retvalue = os.system("find . -name '*.pyc' -exec rm -rf {} \;")
