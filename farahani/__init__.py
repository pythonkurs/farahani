import untangle
import urllib2

def calculate_repair():
    #infile_path='~/nyct_ene.xml'
    url = "http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml"
    
    xml_feed = urllib2.urlopen(url)
    doc = untangle.parse(xml_feed.read())
    #doc = untangle.parse(infile_path)
    #l=doc.get_elements()
    #print l  
    outages = doc.NYCOutages.outage
    #print outages
    #outage = outages[5]
    #k=outage.get_elements()
    #print k
    #print outage.reason.cdata
    
    total=0
    repair=0
    for outage in outages:
        total+=1
        if outage.reason.cdata=='REPAIR':
            repair+=1
    
    print 'The fraction of the escalators under repair is: '+str(float(repair)/total)  
