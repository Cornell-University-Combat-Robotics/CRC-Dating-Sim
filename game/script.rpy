#characters
define m = Character("Player") #change this to support self insert
define n = Character("Narrator", color="ffffff") 
define r = Character("Richard", color="ffa500")
define prof = Character("Prof Bruno", color="ffffff")
image bruno neutral = "bruno.png"

#backgrounds
image bg duffield = Frame("bg/Duffield-ext-pano_0.jpg")
image bg warren = Frame("bg/warren_hall.jpg")
image bg ag = Frame("bg/Cornell_Ag_quad.jpg")
image bg golf = Frame("bg/RTJ3.jpg")
image bg north = Frame("bg/north.jpg")
image bg restaurant = Frame("bg/taverna-banfi.jpg")

#sprites
image heart = "heart.PNG"

image heartbreak:
    "sprites/heart.PNG"
    0.2
    "sprites/heart1.PNG"
    0.2 #this part defines how long to wait before next frame
    "sprites/heart2.PNG"
    0.2
    "sprites/heart3.PNG"
    0.2
    "sprites/heart4.PNG"
    0.2
    "sprites/heart5.PNG"
    0.2
    repeat


image heartpoint:
    "sprites/heart.PNG"
    0.2
    "sprites/hearta.PNG"
    0.2 #this part defines how long to wait before next frame
    "sprites/heartb.PNG"
    0.2
    "sprites/heartc.PNG"
    0.2
    "sprites/heartb.PNG"
    0.2
    "sprites/hearta.PNG"
    0.2
    repeat


screen stats():
    # $ points = 0 
    zorder 100    
    if quick_menu:
        vbox:            
            xalign 0.0
            yalign 0.8

            $ Rizzpoints = "Rizzpoints: " + str(points)

            text _("{color=#ffffff}" + Rizzpoints + "{/color}")


init python:
    config.overlay_screens.append("stats")

# The game starts here.
label start:
    $ points = 0

    scene bg duffield

    n "Welcome to Botnell University! Here, all the smartest robots come to learn and prepare themselves to get a minimum wage job."

    m "Wow, the first day of class. I am so excited for my freshman year at Botnell University!"

    $ m = renpy.input("What is your name, Botnell Student?")

    $ m = m.strip()

    m "Alright, let me check my schedule. I forgot what class I have first."

    jump AEM_Class
