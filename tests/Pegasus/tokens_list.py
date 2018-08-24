
def get_tokens_list(s):

     import re, string, textwrap
    
     # Remove all non-word characters (everything except numbers and letters)
     s = re.sub(r"[^\w\s]", '', s)

     # Replace all runs of whitespace 
     s1 = re.sub(r"\s+", '', s)

     # Split a string into N equal parts
     tokens=textwrap.wrap(s1, 32)

     return tokens
