def get_days(end_date):
    import datetime

    now = datetime.datetime.now()
    cdate = now.strftime("%m/%d/%y")
    pdate = end_date
    
    cdate1 = datetime.datetime.strptime(cdate, "%m/%d/%y").date()
    pdate1 = datetime.datetime.strptime(pdate, "%m/%d/%y").date()
    delta =  (cdate1 - pdate1).days
    return (delta + 1)
