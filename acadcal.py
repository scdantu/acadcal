#!/usr/bin/env python2
from icalendar import Calendar, Event
import datetime as dtime
import random
#from datetime import datetime
from icalendar import vCalAddress, vText
import tempfile, os
import pytz

cal=Calendar()
cal.add('prodid', '-//Microsoft Corporation//Outlook 16.0 MIMEDIR//EN')
cal.add('version', '2.0')

def main():
    global cal
    lecture_start=dtime.datetime(2021,10,06,9,0,0,tzinfo=pytz.utc)
    lab_start=dtime.datetime(2021,10,06,12,0,0,tzinfo=pytz.utc)

    for i in range(0,9,1):
        curr_date=lecture_start+dtime.timedelta(days=i*7)
        end_date=curr_date+dtime.timedelta(hours=1)

        print(str(curr_date),str(end_date))
        event=create_event("CS5701: Lecture","Orange",curr_date,end_date,event_location="LECT C")
        cal.add_component(event)

        lab_start_date=lab_start+dtime.timedelta(days=i*7)
        lab_end_date=lab_start_date+dtime.timedelta(hours=2)

        event=create_event("CS5701: Lab","Orange",lab_start_date,lab_end_date,event_location="TOWA 407")
        cal.add_component(event)

    f=open('cs5701.ics','wb')
    f.write(cal.to_ical())
    f.close()
def create_event(event_name="Lecture",category="Blue",date_start=dtime.datetime.now(),date_end=dtime.datetime.now(),event_location=""):
    event = Event()
    event.add('summary', event_name)
    event.add('dtstart',date_start)
    event.add('dtend',date_end)
    curr_time = dtime.datetime.now(pytz.utc)
    event.add('dtstamp',curr_time)
    organizer = vCalAddress('MAILTO:sarath.dantu@brunel.ac.uk')
    organizer.params['cn'] = vText('Sarath Dantu')
    organizer.params['role'] = vText('CHAIR')
    event['organizer'] = organizer
    event['location'] = vText(event_location)
    event['uid']=str(random.randrange(0,10000000))
    event.add('categories',vText(category+' category'))
    event.add('priority', 5)
    return event
main()
