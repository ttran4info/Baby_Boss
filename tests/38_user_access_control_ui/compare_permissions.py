import json
#test_json='{"5":{"name":"NCS","permission":"READ"},"6":{"name":"CATALINA","permission":"READ"},"7":{"name":"USADATA","permission":"READ"},"8":{"name":"ACXIOM","permission":"READ"},"9":{"name":"EXPERIAN","permission":"READ"},"10":{"name":"NESTLE","permission":"READ"},"1":{"name":"4INFO","permission":"READ,WRITE"}}'

def compare_permissions(test_json1,test_json2):
    dict1 = json.loads(test_json1)
    dict2 = json.loads(test_json2)
    j1=str(dict1)
    j2=str(dict2)
    s='same permissions'
    d='permissions differ'
    if j1==j2:
        return s
    else:
        return d