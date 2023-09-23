# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Richard")
define m = Character("Player") #chnage this to support self insert 
define prof = Character("Prof Bruno")
image bg duffield = Frame("Duffield-ext-pano_0.jpg")
image bg warren = Frame("warren_hall.jpg")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg duffield

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    
    m "Wow first day of class. I am so exctied for my freshman year at Cornell University"

    m "Hehe. Let's check my schedule. I forgot what class I had first."

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
    "You are walking to your AEM Class"

    m "Marketing! I am excited for class. I hope my professor is a good lecturer."

    m "Hmmm Warren 105....Ah found it"

    m "It's the first day. I should try to make new friends..."
    
    "In class, Professor Bruno talks about how money is good."
    "You look around and there is ??? to your left and one orange robot to your right."

    menu:
        "Talk to person to the left":
            jump Richard_in_AEM

        "Talk to the person to the right":
            jump Richard_in_AEM

    # This ends the game.
    # return

label Richard_in_AEM: 
    "You pick to the right."
    m "Hey nice to meet you. I’m PLAYER, what’s your major? "
    r "Hey I’m a Business major and a pro golfer, look at my triceps. Here’s my business card and $100 "
    m "Money? You must be really rich"
    r "*visible blush* actually my friends call me RiCHARD  *wink w sparkle*"
    prof "*AHEM*, we have business to attend to!"

    m "*thinking* dang what a jock, I guess he liked when i gave him a compliment on his vast generational wealth."

    menu:
        "Leave Class":
            jump Ask_Richard_out

label Ask_Richard_out: 
    r "Oh hey bro what’s up!"
    m "*thinking* wow, Richard seems like a really cool fella, I should ask him to hang and get to know him better!"

    "Ask Richard to"

    menu:
        "Come golfing with me.":
            jump richard_golf

        "Let’s study in the library.":
            jump richard_library

        "We should go shopping.":
            jump richard_shopping


label richard_golf:
    m "Would you and your incredible triceps like to accompany me on the golfing green this weekend?"
    r "YAS fam, can’t wait to show you my swings! *skip to next day*"

    "You’ve arrived, and see that Richard has already begun hitting balls. You walk up to him. "
    r "hey took you long enough I’ve already scored a bogie. What did you think of that?"
    
    menu:
        "That was sooo cool":
            jump richard_golf2

        "I can do better":
            jump richard_golf2

        "Why did you hit the ball what did it ever do to you?":
            jump richard_golf2

label richard_library:
    m "Want to go study some business texts and such in Olin Library?"
    r "Bruh. I can’t read. Not even a little bit. *looks sad and dejected*"

    ".:. Bad Ending."
    return

label richard_shopping:
    m "Hey Richard! Let’s go on a costly and hedonistic shopping spree with our parents’ money!"
    r "I already own everything a man could ask for. Anywhere else?"

    ".:. Bad Ending."
    return

label richard_golf2: 
    "richard visibly blushes. hehehehehe"
    r "Want to take a swing?"

    menu: 
        "Yes, please show me the ropes!":   
            jump richard_golf3     

        "no thanks":
            jump no_golf

#         "*get nervous*"
#             jump


# label richard3: