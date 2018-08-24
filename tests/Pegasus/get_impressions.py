def get_impressions(str1):
    import re
    num1 = re.compile("^\d.\d")
    num2 = re.compile("\d\d")
    int1=num1.search(str1).group(0)
    int2=num2.search(str1).group(0)
    return [float(int1),int(int2)]

def get_current_impression(str1):
    import re
    num1 = re.compile("^\d.\d")
    int1=num1.search(str1).group(0)
    return float(int1)

def get_targeted_impression(str1):
    import re
    num2 = re.compile("\d\d")
    int2=num2.search(str1).group(0)
    return int(int2)

def get_current_left(str1):
    if "." in str1[0:2]:
        num1=str1[0:3]
    elif "." in str1[0:3]:
        num1=str1[0:4]
    else:
        num1=str1[0:2]
    return float(num1)
