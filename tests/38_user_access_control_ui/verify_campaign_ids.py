
def verify_campaign_ids(campaigns):
    for x in campaigns:
        #for x in list:
            if x is not None:
                #return True
                return "JSON returns a list of campaign ids"
            else:
                return "list of campaign is blank"