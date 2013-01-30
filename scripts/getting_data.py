import untangle

infile_path='/Users/farahanihs/Documents/courses/python_course/farahani/scripts/nyct_ene.xml'
doc = untangle.parse(infile_path)
l=doc.get_elements()
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
    
    
    
    
#for outage in outages:
#    print outage
#    total+=1
#    if outage=='REPAIR':
#        repair+=1
#        
#print 'The fraction of the escalators under repair is: '+str(float(repair)/total)
        