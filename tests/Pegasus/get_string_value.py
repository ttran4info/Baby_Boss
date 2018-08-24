def get_string_value(s):
    import  re, string
    s = re.sub(r"[^\w\s]", '', s)
    return s