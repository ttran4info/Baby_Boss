
import re

def make_list(string1):
    #e.g. string1 = '((321L,),)'
    r=re.findall('\d+', string1)
    return r
