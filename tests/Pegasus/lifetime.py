import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
def lifetime():
    now = datetime.datetime.now()
    end_date=date(2011,07,9)
    rdelta = relativedelta(now, end_date)



    if rdelta.years >0 and rdelta.months >0 and rdelta.days>0:
        return str(rdelta.years)+' years '+str(rdelta.months)+' months '+str(rdelta.days)+ ' days ago'
    elif rdelta.years >5:
        return str(rdelta.years)+' years ago'
    elif rdelta.months >0 and rdelta.days>0:
        return rdelta.months, 'months',rdelta.days, 'days ago'
    elif rdelta.days>1:
        return rdelta.days, 'days ago'
    elif rdelta.days:
        return rdelta.days, 'days ago'