# Author: as-troska

import json             #Bibliotek for å håndtere JSON-formatet
import turtle
from unittest import result           #Bibliotek for å vise enkel grafikk
import urllib.request   #Bibliotek for å jobbe med http-requests
import time

def showISS():
    screen = turtle.Screen()
    screen.setup(720, 360)
    screen.bgpic("map.gif")
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.register_shape("iss.gif")
    iss = turtle.Turtle()
    iss.shape("iss.gif")
    iss.penup()
    iss.goto(get_position("lon"), get_position("lat"))
    

    location = turtle.Turtle()
    location.penup()
    location.color("red")
    location.goto(5.324383, 60.397076)
    location.dot(5)
    location.hideturtle()
    style = ("arial", 12, "bold")
    location.write(time.ctime(get_overpass(5.324383, 60.397076)), font=style)
    
    screen.exitonclick()

def get_overpass(lat, lon):
    overURL = "http://api.open-notify.org/iss-pass.json?lat=" + str(lat) + "&lon=" + str(lon)
    response = urllib.request.urlopen(overURL)
    result = json.loads(response.read())
    return int(result["response"][0]["risetime"])


def get_position(param):
    urlISS = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(urlISS)
    result = json.loads(response.read())
    #result = result["iss_position"]
    
    if param == "time":
        return result["timestamp"]
    elif param == "lat":
        return float(result["iss_position"]["latitude"])
    elif param == "lon":
        return float(result["iss_position"]["longitude"])
    elif param == "all":
        return result
    else:
        print("Invalid parameter in function call")
    print(result)



def get_people_in_space():
    url = "http://api.open-notify.org/astros.json"
    response = urllib.request.urlopen(url)

    result = json.loads(response.read())
    people = result['people']

    print("Antall menneske i rommet: ", result["number"])
    print("Desse folka er i rommet no: ")

    for x in people:
        print("Namn: ", x["name"], "    Stasjon: ", x["craft"])

#lat = get_position("lat")
#print(type(float(lat)))
showISS()