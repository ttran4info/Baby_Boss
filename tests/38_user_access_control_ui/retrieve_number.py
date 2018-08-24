
import re

def retrieve_number(string1):
    #e.g. string1 = '((321L,),)'
    n=int(re.search(r'\d+', string1).group())
    return n
