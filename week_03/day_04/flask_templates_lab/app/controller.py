from flask import render_template, request
from app import app
from app.models.events_list import *
from app.models.event import *

@app.route("/")
def index():
    return render_template("index.html", title="DS Home", events=events)

@app.route("/add-event", methods=["POST"])
def add_event():
    eventDate = request.form["date"]
    eventName = request.form["name"]
    eventNumOfGuests = request.form["num_of_guests"]
    eventRoom = request.form["room"]
    eventDescription = request.form["description"]
    if ("recurring" in request.form):
        eventRecurring = True
    else:
        eventRecurring = False
    newEvent = Event(eventDate, eventName, eventNumOfGuests, eventRoom, eventDescription, eventRecurring)
    add_new_event(newEvent)
    return render_template("index.html", title="DS Home", events=events)

@app.route("/remove-event/<name>", methods=["POST"])
def remove_event(name):
    remove_existing_event(name)
    return render_template("index.html", title="DS Home", events=events)