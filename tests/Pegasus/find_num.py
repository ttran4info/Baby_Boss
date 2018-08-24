
import re

def get_number(str1):
    #str1="PAUSED(67)"
    nums = re.compile(r"\d+(?:\.\d+)?")
    to_int=int(nums.search(str1).group(0))
    return to_int
