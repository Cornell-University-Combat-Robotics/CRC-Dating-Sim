# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Player") #change this to support self insert
define n = Character("Narrator", color="ffffff") 
define r = Character("Richard", color="ffa500")
define prof = Character("Prof Bruno", color="ffffff")
image bruno neutral = "bruno.png"
image bg duffield = Frame("Duffield-ext-pano_0.jpg")
image bg warren = Frame("warren_hall.jpg")
image bg ag = Frame("Cornell_Ag_quad.jpg")
image bg golf = Frame("RTJ3.jpg")
image bg north = Frame("north.jpg")
image bg restaurant = Frame("taverna-banfi.jpg")
image richard neutral= "richard_neutral.png"
image richard angry= "richard_angry.png"
image richard proud= "richard_proud.png"
image richard worried= "richard_worried.png"
image richard love = "richard_love.png"
image richard sad = "richard_sad.png"
image richard blush = "richard_blush.png"
image richard fuckboy = "richard_fuckboy.png"
image heart = "heart.PNG"

image heartbreak:
    "heart.PNG"
    0.2
    "heart1.PNG"
    0.2 #this part defines how long to wait before next frame
    "heart2.PNG"
    0.2
    "heart3.PNG"
    0.2
    "heart4.PNG"
    0.2
    "heart5.PNG"
    0.2
    repeat


image love:
    "heart.PNG"
    0.2
    "hearta.PNG"
    0.2 #this part defines how long to wait before next frame
    "heartb.PNG"
    0.2
    "heartc.PNG"
    0.2
    "heartb.PNG"
    0.2
    "hearta.PNG"
    0.2
    repeat

# The game starts here.
label start:
    $ points = 0 
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg duffield

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    n "Welcome to Botnell University! Here, all the smartest robots come to learn and prepare themselves to get a minimum wage job."

    m "Wow, the first day of class. I am so excited for my freshman year at Botnell University!"

    $ m = renpy.input("What is your name, Botnell Student?")

    $ m = m.strip()

    m "Alright, let me check my schedule. I forgot what class I have first."

    # This ends the game.
    # return

label AEM_Class:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg warren

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    n "You are walking to your AEM Class..."
    m "Marketing! I am excited for class. I hope my professor is a good lecturer."
    m "Hmmm Warren 105... Ah found it!"
    m "It's the first day. I should try to make new friends..."

    show bruno neutral at truecenter
    n "In class, Professor Bruno talks about how money is good."
    hide bruno neutral

    n "You look around and there is ??? to your left and one orange robot to your right."
    menu:
        "Talk to the robot to the left":
            jump Richard_in_AEM

        "Talk to the robot to the right":
            jump Richard_in_AEM

    # This ends the game.
    # return

label Richard_in_AEM: 
    n "You pick to the right."
    show richard neutral at truecenter: 
        zoom 0.5
    m "Hey, nice to meet you. I'm [m], what's your major? "
    r "Hey! I'm a Business major and a pro golfer, look at my triceps. Here's my business card and $100."
    m "Money? You must be really rich!"
    hide richard neutral

    show richard fuckboy at truecenter: 
        zoom 0.5
    r "Actually my friends call me Richard."
    hide richard fuckboy

    show bruno neutral at truecenter
    prof "AHEM! We have business to attend to!"
    hide bruno neutral

    n "You both get back to class and focus."
    m "Dang what a jock, I guess he liked when I gave him a compliment on his vast generational wealth."

    menu:
        "Leave Class and search for Richard":
            jump Ask_Richard_out

label Ask_Richard_out: 
    scene bg ag
    show richard neutral at truecenter: 
        zoom 0.5
    r "Oh hey! What's up?"
    m "*thinking* Wow, Richard seems like a really cool fella, I should ask him to hang and get to know him better!"

    "I should ask Richard to:"
    hide richard neutral

    menu:
        "Come golfing with me.":
            jump richard_golf

        "Come study in the library.":
            jump richard_library

        "Come shopping.":
            jump richard_shopping

label richard_library:
    show richard neutral at truecenter: 
        zoom 0.5
    m "Let's study in the library. There are some business texts and such in Olin Library!"
    hide richard neutral
    show richard angry at truecenter: 
        zoom 0.5
    $ points -= 1

    show heartbreak at left:
        matrixcolor TintMatrix("#6967d4") * SaturationMatrix(0.01)
        zoom 3
    
    r "Bruh. I can't read. Not even a little bit."
    hide richard angry
    hide heartbreak
    jump Bad_End

label richard_shopping:
    show richard neutral at truecenter: 
        zoom 0.5
    m "We should go shopping. We can go on a costly and hedonistic shopping spree with our parents' money!"
    hide richard neutral
    show richard worried at truecenter: 
        zoom 0.5
    r "I already own everything a man could ask for. Anywhere else?"
    hide richard worried

    menu:
        "Come golfing with me.":
            jump richard_golf

        "Buy me Prada... Balenciaga.":
            jump richard_shopping_end

label richard_shopping_end: 
    show richard worried at truecenter: 
        zoom 0.5
    m "Buy me Prada... Balenciaga."
    hide richard worried
    show richard angry at truecenter: 
        zoom 0.5
    r "You're just using me for my money."
    r "Goodbye forever."
    hide richard angry
    jump Bad_End

label richard_golf:
    show richard neutral at truecenter: 
        zoom 0.5
    m "Come golfing with me. I would like you and your incredible triceps like to accompany me on the golfing green this weekend!"
    hide richard neutral
    show richard proud at truecenter: 
        zoom 0.5
    r "YAS fam, can't wait to show you my swings!"
    show love at left:
        zoom 3
    $ points += 1
    hide richard proud
    scene bg golf
    n "The next day..."
    n "You've arrived, and see that Richard has already begun hitting balls. You walk up to him."
    show richard proud at truecenter: 
        zoom 0.5
    r "Hey, took you long enough! I've already scored a birdie. What did you think of that?"
    hide richard proud
    hide love
    menu:
        "That was sooo cool!":
            jump richard_golf1A

        "I can do better.": 
            jump richard_golf1B

        "Why did you hit the ball?! What did it ever do to you?!":
            jump richard_golf1C

label richard_golf1A: 
    show richard neutral at truecenter: 
        zoom 0.5
    m "That was sooo cool! Wow Richard! You have insane golf skills, you could be a pro!"
    show love at left:
        zoom 3
    hide richard neutral
    show richard blush at truecenter: 
        zoom 0.5
    r "Aww, thanks babe."
    $ points += 1
    hide richard blush
    hide love 
    jump richard_golf2

label richard_golf1B: 
    
    show richard neutral at truecenter: 
        zoom 0.5
    show heartbreak at left:
        matrixcolor TintMatrix("#6967d4") * SaturationMatrix(0.01)
        zoom 3
    m "I can do better, amateur. Let me show you how a real golfer gets it done."
    hide richard worried
    n "You forcefully grab the club from Richard."
    show richard angry at truecenter: 
        zoom 0.5
    r "How DARE you!"
    $ points -= 1
    hide richard angry
    hide heartbreak
    jump richard_golf2

label richard_golf1C: 
    show richard neutral at truecenter: 
        zoom 0.5
    m "Hey! Why'd you hit that ball?! What did it ever do to you?!"
    hide richard neutral
    show richard angry at truecenter: 
        zoom 0.5
    r "You are an odd egg."
    hide richard angry
    jump richard_golf2

label richard_golf2: 
    show richard neutral at truecenter: 
        zoom 0.5
    r "Want to take a swing?"
    hide richard neutral
    menu: 
        "Yes, please show me the ropes!":
            jump richard_golf2A     

        "No, thanks.":
            jump richard_golf2B

        "*get nervous*":
            jump richard_golf2C

label richard_golf2A: 
    show richard neutral at truecenter: 
        zoom 0.5
    
    m "Help me Richard, I cannot play golf, please guide me through the swing slowly with your strong arms!"
    hide richard neutral
    show love at left:
        zoom 3
    show richard proud at truecenter: 
        zoom 0.5
    r "Oh, why of course my dear!"
    $ points += 1
    hide richard proud
    hide love
    jump richard_golf3A

label richard_golf2B:
    show richard worried at truecenter: 
        zoom 0.5
    show heartbreak at left:
        matrixcolor TintMatrix("#6967d4") * SaturationMatrix(0.01)
        zoom 3
    m "No, thanks. I am against the playing of golf for the environmental effects of the watering of golf courses."
    m "This entire establishment is a waste of our local freshwater resources and I will not stand for it."
    hide richard worried
    show richard angry at truecenter: 
        zoom 0.5
    r "How dare you insult my favorite pastime!"
    r "You are obviously uncultured if you can't appreciate the finer things in life like the joy of hitting golf balls!"
    $ points -= 1
    hide richard angry
    hide heartbreak
    jump richard_golf3B

label richard_golf2C:
    show richard worried at truecenter: 
        zoom 0.5
    n "You get nervous and your hands get weirdly sweaty. You drop the golf club on your foot and get an ouchie."
    r "*side eye* Well you're rather uncoordinated aren't you..."
    hide richard worried
    jump richard_golf3A

label richard_golf3A:
    n "You two spent the afternoon drilling shots. Richard seemed to have a good time."
    show richard proud at truecenter: 
        zoom 0.5
    r "I win! It's getting late! I must head to practice now, but that was super fun."
    hide richard proud
    jump richard_dinner

label richard_golf3B:
    show richard angry at truecenter: 
        zoom 0.5
    n "Richard did not seem to have a good time."
    r "You are not fun to play golf with whatsoever. Bye, forever."
    hide richard angry
    jump Bad_End

label richard_dinner: 
    scene bg north
    m "Richard is so CUTE!! I want to meet with Richard again, I should ask him out on a second date!"
    menu: 
        "Call him":
            jump richard_dinner_A

        "Go to his house":
            jump richard_dinner_B

        "Be too shy":
            jump richard_dinner_C

label richard_dinner_A:
    n "You dial Richard's number that you found on Student Center."
    show richard neutral at truecenter: 
        zoom 0.5
    m "Hi Richard! I-"
    r "Oh [m]! So good of you to call. I was just thinking about calling you. How've you been?"
    show love at left:
        zoom 3
    $ points += 1
    r " Nevermind that... I have ultradeluxe reservations at Taverna Banfi in Botnell's own Batler Hotel this evening, would you care to join me?"
    hide richard neutral
    hide love
    jump richard_dinner_1

label richard_dinner_B:
    n "You walk to Richard's dorm."
    show richard neutral at truecenter: 
        zoom 0.5
    m "Hi Richard! I just thought I'd come over-"
    hide richard neutral
    show richard fuckboy at truecenter: 
        zoom 0.5
    r "Oh my my! What are you doing in my palatial home unannounced?"
    r "Well, that's one way to get a man out on a date... does Taverna Banfi for two interest you?"
    m "Oh.. why yes!"
    hide richard fuckboy
    jump richard_dinner_1

label richard_dinner_C:
    n "You are too shy to talk to Richard and never speak to him ever again."
    n "Richard sees you in class. His eyes pass over you as he goes to greet CRC-chan, the prettiest girl in school."
    n "He will never speak to you again."
    jump Bad_End

label richard_dinner_1: 
    scene bg restaurant
    show richard neutral at truecenter: 
        zoom 0.5
    n "Richard elegantly awaits you at the finest table in all of Taverna Banfi."
    r "Hello [m]. Come, dine with me."

    "What will you order?"
    hide richard neutral
    menu: 
        "Pasta with butter and choccy milk from the kids menu.":
            jump richard_dinner_1A
        "Just a water with a lime slice.":
            jump richard_dinner_1B
        "A fine steak and a 1969 vintage Dom Peringon Champagne, a wine far out of your tax bracket.":
            jump richard_dinner_1C

label richard_dinner_1A: 
    show heartbreak at left:
        matrixcolor TintMatrix("#6967d4") * SaturationMatrix(0.01)
        zoom 3
    $ points -= 1
    show richard worried at truecenter:
        zoom 0.5
    m "I would like pasta with butter and choccy milk from the kids menu."
    r "Ordering from the children's menu?"
    r "I'm afraid you can't do that dear, it's for 12 and under only. You seem to have no class."
    hide richard worried
    hide heartbreak
    jump Bad_End

label richard_dinner_1B: 
    show richard worried at truecenter:
        zoom 0.5
    m "I would like just a water with a lime slice."
    r "Huh. That's a strange thing to order at a restaurant such as this."
    hide richard worried
    jump richard_dinner_2

label richard_dinner_1C:
    $ points += 1
    show richard proud at truecenter:
        zoom 0.5

    m "I would like a fine steak and a 1969 vintage Dom Peringon Champagne, a wine far out of my tax bracket."
    show love at left:
        zoom 3
    r "What fine exquisite taste you have madame! I commend you. (lifts glass like Jay Gatsby)"
    hide richard proud
    hide love
    jump richard_dinner_2

label richard_dinner_2:
    show richard neutral at truecenter:
        zoom 0.5
    n "The dinner is going well and you and Richard talk for an hour."
    r "It's nice to take a break after working so hard on my money management and asset-selling stock-rising business."
    r "I love my work, but sometimes it really takes a toll."

    hide richard neutral
    menu: 
        "I want to support him!":
            jump richard_dinner_2A

        "What does your business do again?":
            jump richard_dinner_2B

        "Give him advice on his vague business plans.":
            jump richard_dinner_2C

label richard_dinner_2A:
    $ points += 1
    show richard neutral at truecenter:
        zoom 0.5
    m "I want to support you in all your business endeavors!"
    show love at left:
        zoom 3
    hide richard neutral

    show richard blush at truecenter:
        zoom 0.5
    r "Thanks, that means a lot."
    hide richard blush
    hide love
    jump richard_dinner_3

label richard_dinner_2B:
    show richard worried at truecenter:
        zoom 0.5
    m "Wait a minute... what does your money management asset-selling stock-rising business actually do again?"
    r "Oh... you dont know?"
    r "But I talk about it constantly to the point where it may be considered slightly annoying..."

    r "Oh well, let me just spend another hour re-explaining to you..."
    hide richard worried
    jump richard_dinner_3

label richard_dinner_2C:
    $ points -= 1
    show heartbreak at left:
        matrixcolor TintMatrix("#6967d4") * SaturationMatrix(0.01)
        zoom 3
    show richard angry at truecenter:
        zoom 0.5
    m "I understand you want to build your business, but are you sure that this company has an ethical basis in today's modern society?" 
    m "Are you really ready to brave the treachourous pitfalls of today's economy and bring a multifaceted business such as this into the market?"
    m "I think there may be some things you should rethink about this business plan."
    r "You think you can tell me how to run my business?! I hate you! We're over!"
    n "Richard is sobbing because he got his feelings hurt."
    hide richard angry
    hide heartbreak
    jump Bad_End

label richard_dinner_3: 
    show richard neutral at truecenter:
        zoom 0.5
    n "The lights dim. Richard leans in close and his eyes sparkle in the candlelight. What a romantic moment!"
    r "That means a lot to me. People are always shooting my ideas down."
    r "I want to find someone who will never stop me from pursuing my dreams of obtaining unimaginable wealth."
    m "*thinking* This is an important moment. I should be really careful with my words."
    hide richard neutral
    menu: 
        "Profess your love!" if points > 3:
            jump richard_dinner_3A

        "Stay just friends.":
            jump richard_dinner_3B

        "REJECT HIS EXISTENCE AND RUIN HIS DREAMS AFTER PRETENDING TO BE HIS FRIEND.":
            jump richard_dinner_3C

label richard_dinner_3A:
    show richard love at truecenter:
        zoom 0.5
    m "I will always support you Richard, because I LOVE you!"
    n "His eyes sparkle with love! He leans in for a kiss. The kiss tastes metallic."
    hide richard love
    if points > 4:
        jump Good_End
    elif points > 3: 
        jump Neutral_End
    else: 
        jump Bad_End

label richard_dinner_3B:
    show richard worried at truecenter:
        zoom 0.5
    m "Yeah I support you in your business thingamajiggy. I'll always be your good pal, buddy!"
    r "Oh... um... you're my friend too... buddy. (he winces)"
    hide richard worried
    jump Bad_End

label richard_dinner_3C:
    show richard sad at truecenter:
        zoom 0.5
    m "I have something to tell you sweetheart."
    m "I was only talking to you in order to hear all of your business plans and use them for my competing business in the same market! Get owned Richie!"
    n "You abandon Richard at the table as he cries like a baby, his life's dreams shattered."
    hide richard sad
    jump Bad_End

label Bad_End: 
    scene bg duffield
    show richard sad at truecenter:
        zoom 0.5
    n "Richard does not feel like his love is returned. He rejects your advances."
    r "Sorry, I don't think I'm interested anymore."
    n "You have betrayed Richard's trust and he hates you forever. Nice going, dumbass."
    hide richard sad
    return

label Neutral_End: 
    scene bg duffield
    show richard blush at truecenter:
        zoom 0.5
    n "You date Richard for the rest of college."
    n "THE END - RICHARD ROUTE - NEUTRAL ENDING."
    hide richard blush
    return

label Good_End: 
    scene bg duffield
    show richard love at truecenter:
        zoom 0.5
    n "You and Richard walk to Duffield Atrium and get married and live happily ever after."
    n "THE END - RICHARD ROUTE - GOOD ENDING."
    hide richard love
    return