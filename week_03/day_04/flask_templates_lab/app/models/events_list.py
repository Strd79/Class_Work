from app.models.event import *

event1 = Event("2020-09-18", "Office party", 50, "Board Room", "A socially distanced gathering of staff.", False)
event2 = Event("2020-09-19", "Hangover party", 1, "The couch", "Rest, drink plenty of water and eat junk food all day!", True)
events = [event1, event2]

def add_new_event(event):
    events.append(event)

def remove_existing_event(name):
    for event in events:
        if event.event_name == name:
            events.remove(event)