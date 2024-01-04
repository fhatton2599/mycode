#!/bin/env python3

#Write print statement "My eyes! The goggles do nothing!"

#use challenge dictionary
def chmain():
    challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
    a = challenge[2][1]

    print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!")
chmain()


#use trial dictionary
def trmain():

    trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

    #eyes
    eye = trial[2].get("goggles")

    #goggles
    gog = trial[2].get("eyes")

    #nothing
    noth = trial[3]

    print(f"My {eye}! The {gog} do {noth}!")

trmain()


#use nightmare dictionary
def nightmain():

    nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

    #eyes
    eye= nightmare[0]["user"]["name"]["first"]

    #goggles
    gog= nightmare[0]["kumquat"]

    #nothing
    noth= nightmare[0]["d"]

    print(f"My {eye}! The {gog} do {noth}!")

nightmain()
