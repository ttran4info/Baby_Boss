def get_left(left):
    import datetime
    from datetime import date
    from dateutil.relativedelta import relativedelta
    now = datetime.datetime.now()
    startdate = datetime.datetime(left)
    rdelta = relativedelta(now, startdate)
    #print startdate
    if rdelta.years >0 and rdelta.months >0 and rdelta.days>0:
        print rdelta.years, 'years', rdelta.months, 'months', rdelta.days, 'days days ago'
    elif rdelta.months >0 and rdelta.days>0:
        print rdelta.months, 'months',rdelta.days, 'days days ago'
    elif rdelta.days>1:
        print rdelta.days, 'days day ago'
    elif rdelta.days:
        print rdelta.days, 'day days ago'