import untangle
import urllib2

def calculate_repair():
    
    url = "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"
    
    xml_feed = urllib2.urlopen(url)
    doc = untangle.parse(xml_feed.read())

    outages = doc.NYCOutages.outage
    

    
    total=0
    repair=0
    for outage in outages:
        total+=1
        if outage.reason.cdata=='REPAIR':
            repair+=1
    
    print 'The fraction of the escalators under repair is: '+str(float(repair)/total)  
