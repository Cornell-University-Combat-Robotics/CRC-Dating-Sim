image lance neutral= "lance/lance_neutral.png"
image lance angry= "lance/lance_angry.png"
image lance proud= "lance/lance_proud.png"
image lance worried= "lance/lance_worried.png"
image lance love = "lance/lance_love.png"
image lance sad = "lance/lance_sad.png"
image lance blush = "lance/lance_blush.png"
image lance fuckboy = "lance/lance_fuckboy.png"
image lance cold = "lance/lance_cold.png"
image lance coat = "lance/lance_coat.png"


label English_Class:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg warren

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    n "You are walking to your English Class..."
    m "English! I am excited for class. I hope my professor is a good lecturer."
    m "Hmmm Morril 105... Ah found it!"
    m "It's the first day. I should try to make new friends..."

    show bruno neutral at truecenter
    n "In class, Professor Bruno talks about we are speaking English."
    hide bruno neutral

    n "You look around and there is an HDPE robot with cool green wheels to your left and ??? to your right."
    menu:
        "Talk to the robot to the left":
            jump Lance_in_English

        "Talk to the robot to the right":
            jump Lance_in_English

    # This ends the game.
    # return

label Lance_in_English: 
    n "You pick to the left."

    show lance neutral at truecenter: 
        zoom 0.5
    m "Hey, nice to meet you. I'm [m], what's your major? "
    l "Bonjour my sweet, enchante. As for my major… I'm a lover of finer things in life…  and beauty… beauties like you *wink*"
    m "*blush* Oh my… you flatter me sir."
    hide lance neutral

    show lance fuckboy at truecenter: 
        zoom 0.5
    l "*visible blush* Sir? Oh, do forgo the formalities, my name is Lance *wink w sparkle*"
    hide lance fuckboy

    show bruno neutral at truecenter
    prof "*AHEM*, we have sentences to read!"
    hide bruno neutral

    n "You both get back to class and focus."
    m "*thinking* dang what a flirtatious and suave robot, he sure is a smooth operator!"

    menu:
        "Leave class and search for Lance":
            jump Ask_Lance_out

label Ask_Lance_out: 
    scene bg arts

    n "You rush out of class and look for Lance before spotting him walking in the arts quad."
    n "You quickly hurry to catch up to him."

    show lance neutral at truecenter: 
        zoom 0.5
    l "My my, fancy seeing you again here darling! Come here often?"
    m "Only every Monday, Wednesday, Friday at 10:10 haha…"
    m "*thinking* wow, Lance seems like a really cool fella, I should ask him to hang and get to know him better!"
    hide lance neutral

    menu:
        "Would you like to enjoy a romantic picnic with me on the shores of Cayuga Lake?":
            jump lance_picnic_setup

        " Wanna study with me in Duffield?":
            jump lance_duffield

        "Wanna get some food at Oakies?":
            jump lance_oakies

label lance_picnic_setup:
    show lance neutral at truecenter: 
        zoom 0.5
    m "Would you like to enjoy a romantic picnic with me on the shores of Cayuga Lake?"
    show lance proud at truecenter: 
        zoom 0.5
    show heartpoint at left:
        zoom 3
    l "*eyes sparkle* why yes, dear, that would be most fantastic *bends to kiss your hand softly*"
    $ points += 1
    hide heartpoint
    jump lance_picnic

label lance_duffield:
    m "Want to join me as I work on my pset in Duffield?"
    show lance worried at truecenter: 
        zoom 0.5
    show heartbreak at left:
        zoom 3
    l "*looks at you with disdain* what is pset darling?"
    show lance angry at truecenter: 
        zoom 0.5
    show heartbreak at left:
        zoom 3
    n "As you explain what a pset is to Lance he grows more and more concerned before quickly getting upset"
    l "How dare you invite me to do something so cruel and unforgiving, that sounds like torture"
    n "Lance storms off"
    hide heartbreak
    return

label lance_oakies:
    show lance neutral at truecenter: 
        zoom 0.5
    m "Wanna get some food at Oakies?"
    show lance angry at truecenter: 
        zoom 0.5
    l "Yuck! Absolutely no romantic atmosphere there whatsoever. I only eat at Green Dragon sweetheart."

    menu:
        "Would you like to enjoy a romantic picnic with me on the shores of Cayuga Lake?":
            jump lance_picnic_setup

        " Wanna study with me in Duffield?":
            jump lance_duffield

label lance_picnic:
    scene bg stewart
    n "As the sun sets over Cayuga's waters, you arrive at Stewart Park."
    n "Through the waning light, you see the handsome Lance reclining on a picnic blanket by the water, reading a collection of Shakespeare's sonnets."
    show lance neutral at truecenter: 
        zoom 0.5
    n "As you arrive, he looks up and meets you with his soft, beautiful eyes."
    l "Welcome, dearest. I took the liberty of providing some food myself, I'm an excellent cook you see. So… what did you bring for the picnic?"

    menu:
        "Fine grape fruit to pair with some fresh caught oysters.":
            jump lance_grape

        "Nothing.":
            jump lance_nothing

        "Nature Valley granola bars.":
            jump lance_granola

label lance_grape:
    show lance neutral at truecenter: 
        zoom 0.5
    m "I brought some fine grape fruit to pair with some fresh caught oysters."
    show lance proud at truecenter: 
        zoom 0.5
    show heartpoint at left:
        zoom 3
    l "Why how excellent! These will go swimmingly with the charcuterie board I've prepared."
    $ points += 1
    hide heartpoint
    jump lance_sunset

label lance_nothing:
    show lance neutral at truecenter: 
        zoom 0.5
    m "Oh… I forgot to bring anything."
    show lance angry at truecenter: 
        zoom 0.5
    show heartbreak at left:
        zoom 3
    l "Oh… so you don't even care about me at all, do you?"
    $ points -= 1
    hide heartbreak
    jump lance_sunset

label lance_granola:
    show lance neutral at truecenter: 
        zoom 0.5
    m "Oh I can't cook so I just brought some Nature Valley granola bars."
    show lance worried at truecenter: 
        zoom 0.5
    l "Oh… um… well that wouldn't be my first choice for a romantic picnic but that's fine I guess."
    jump lance_sunset

label lance_sunset:
    n "You begin to dine together as the sun dips slowly over the horizon."
    n "As the night comes upon the town of Ithaca, you notice that your hand is placed awfully close to Lance's on the picnic blanket." 
    n "Will you make a move?"
    
    menu:
        "Brush your hand softly against his.":
            jump lance_handhold

        "Grab his hand fast.":
            jump lance_fasthand

        "Get up and say it's time to go.":
            jump lance_leave

label lance_handhold:
    show lance neutral at truecenter: 
        zoom 0.5
    n "Your hand brushes softly against Lance's"
    show lance blush at truecenter: 
        zoom 0.5
    show heartpoint at left:
        zoom 3
    l "*takes your hand lovingly* What soft and delicate hands you have my dear! *kisses your hand softly*"
    $ points += 1
    hide heartpoint
    jump lance_sunset_bye

label lance_fasthand:
    show lance neutral at truecenter: 
        zoom 0.5
    n "You go to grab Lance's hand but you do it a bit too hard and he jerks away."
    show lance angry at truecenter: 
        zoom 0.5
    show heartbreak at left:
        zoom 3
    l "YOWCH! Now that was not very elegant dear… I'm a fragile young bot you know… you could have broken something…"
    $ points -= 1
    hide heartbreak
    jump lance_sunset_bye


label lance_leave:
    show lance neutral at truecenter: 
        zoom 0.5
    n "You get nervous and your hands get weirdly sweaty and you stand up quickly and say it's time to go."
    show lance angry at truecenter: 
        zoom 0.5
    l "*side eye* Oh… but we were just… well, if you insist, my dear…"
    jump lance_sunset_bye

label lance_sunset_bye:
    show lance neutral at truecenter: 
        zoom 0.5
    n "Narrator: With the sun now long gone beneath the horizon, and the blinking stars starting to appear across the sky above, you pack up the picnic and head on home."
    if points >= 2: 
        l "Why, it's getting quite late, and the night grows cold. But how could I ever be truly cold when you warm my heart as you do? *his eyes sparkle*"
        jump lance_2nd_ask
    else: 
        l "You really need a lesson in the subtle ways of romance my darling. I think our paths shan't cross again. I will take my leave of you. "
        return

label lance_2nd_ask:
    m "Lance is so CUTE!! I want to meet with Lance again, I'll go ask him out!"
    menu:
        "Throw a rock at his window":
            n "You pelt rocks at Lance's window until he opens it and peers into his garden." 
            m "Hi Lance! I-"
            show lance neutral at truecenter: 
                zoom 0.5
            show heartpoint at left:
                zoom 3
            l "Oh [m]! Hmmm… [m], [m]... Wherefore art thou, [m]?... How lovely to see you here. I've been thinking of your beautiful eyes since the night I was so lucky to be in your company for that beautiful picnic. Would you care to join me on the suspension bridge this evening at the strike of midnight?"
            $ points += 1
            hide heartpoint
            jump lance_2nd_date

        "Text him":
            m "*texting* Lol Lance what a nice time we had last nite! I want to see u soon, k?"
            l "*voicemessage* sorry dear, I'm not much of a texter. I feel it takes away from the sweet romance of my gentle words. But no matter, would you care to meet me at the suspension bridge this evening at the strike of midnight?"
            jump lance_2nd_date

        "Be too shy":
            n "You are too shy to talk to Lance and never speak to him ever again."
            n "Lance sees you in class. His eyes pass over you as he goes to greet CRC-chan, the prettiest girl in school. He will never speak to you again"
            show heartbreak at left:
                zoom 3
            $ points -= 1
            hide heartbreak
            return

label lance_2nd_date:
    n "The clocktower begins to ring the 12 chimes of midnight, and through the darkness the lights of the suspension bridge come into view. In the cold fall night, Lance stands at the center of the bridge, looking pensively over the gorge, pondering its depths, a single rose held in his hand."
    show lance neutral at truecenter: 
        zoom 0.5
    l "My darling, you've made it. Your radiance positively lights up this dark autumn eve. "
    menu:
        "Flirt with him":
            m "*blush* Oh why thank you. You clean up well yourself, pretty boy."
            l "Careful darling, I may swoon." 
            show heartpoint at left:
                zoom 3
            $ points += 1
            hide heartpoint
            jump lance_2nd_date_pt2
        
        "Is that a Lance in your pants or are you just happy to see me?":
            m "Is that a Lance in your pants or are you just happy to see me?"
            show lance worried at truecenter:
                zoom 0.5
            show heartbreak at left:
                zoom 3
            $ points -= 1
            l "Oh my! How vulgar… and I thought you were a proper young robot!"
            hide heartbreak

            jump lance_2nd_date_pt2

        "Get Nervous":
            m "H-h-hi Lance um uh you are so cool haha"
            show lance worried at truecenter:
                zoom 0.5
            l "My goodness, I guess you'll need some help brushing up your romancing skills… *side eye*"
            jump lance_2nd_date_pt2

label lance_2nd_date_pt2:
    show lance cold at truecenter: 
        zoom 0.5

    n "The clocktower continues ringing out the 12 chimes of midnight as the cold autmn wind ruffles your hair in the lamplight. In the frigid fall air, you see Lance begin to feel the slightest shiver."
    menu: 
        "Lend him your coat":
            m "Oh darling, don't be cold, here, take my coat."
            show heartpoint at left:
                zoom 3
            $ points += 1
            show lance coat at truecenter:
                zoom 0.5
            l "*blushing* Oh my! How suave of you my sweet."
            hide heartpoint
            jump lance_final

        "Toughen up cupcake":
            m "Toughen up cupcake. You know it gets much colder in Ithaca when its actually winter."
            show lance sad at truecenter: 
                zoom 0.5
            show heartbreak at left:
                zoom 3
            $ points -= 1
            l "*sniffles, teeth chattering* Oh… well… that wasn't very kind…"
            hide heartbreak
            jump lance_final

        "Do nothing":
            n "You simply stand and watch Lance shiver."
            l " Oh, my, I guess I will just be cold. Silly me not bringing a coat haha…"
            jump lance_final

label lance_final:
    show lance neutral at truecenter: 
        zoom 0.5
    n "The twelfth chime of midnight rings out across the campus."
    n "Lance looks deeply into your eyes and you feel woozy. As you begin to lose balance, Lance swiftly scoops you into his arms and holds you in a romantic embrace."
    n "The time is right, and he closes his eyes, puckers his lips, and moves in close.  What a romantic moment! I should be really careful with my words."
    if points >= 4: 
        menu:
            "Profess your Love!":
                m "Oh Lance, kiss me with those sweet sensuous lips, because I LOVE you!"
                show heartpoint at left:
                    zoom 3
                n "His eyes sparkle with love! He leans in for a kiss. The kiss tastes metallic."
                hide heartpoint
                return

            "reject romance.":
                m "*lean away and pat him on the back* Ok there bud, hold your horses. Not to burst your bubble but I think we should set this all straight so no feelings get hurt. I just don't know if I'm feeling like ROMANCE right now… I was more going for a situationship friends with benefits part time no labels kind of casual thing, you know?"
                show lance sad at truecenter: 
                    zoom 0.5
                show heartbreak at left:
                    zoom 3
                l "Oh… um…ok then I guess. (he winces)"
                hide heartbreak
                return

            "(REJECT HIS EXISTENCE AND RUIN HIS DREAMS AFTER PRETENDING TO BE HIS FRIEND)":
                m "I have something to tell you sweetheart. I was just playing with you all along. You think you're so ROMANTIC, but you're no better than any other asshole at this school. You're an egotistical narcissist who thinks he's hot shit just because he's tall and dreamy, well I don't need you!"
                show lance sad at truecenter: 
                    zoom 0.5
                show heartbreak at left:
                    zoom 3
                n "You abandon LANCE on the bridge as he cries like a baby, his life's dreams shattered."
                hide heartbreak
                return
    else:
        menu:
            "reject romance.":
                m "*lean away and pat him on the back* Ok there bud, hold your horses. Not to burst your bubble but I think we should set this all straight so no feelings get hurt. I just don't know if I'm feeling like ROMANCE right now… I was more going for a situationship friends with benefits part time no labels kind of casual thing, you know?"
                show lance sad at truecenter: 
                    zoom 0.5
                show heartbreak at left:
                    zoom 3
                l "Oh… um…ok then I guess. (he winces)"
                hide heartbreak
                return

            "(REJECT HIS EXISTENCE AND RUIN HIS DREAMS AFTER PRETENDING TO BE HIS FRIEND)":
                m "I have something to tell you sweetheart. I was just playing with you all along. You think you're so ROMANTIC, but you're no better than any other asshole at this school. You're an egotistical narcissist who thinks he's hot shit just because he's tall and dreamy, well I don't need you!"
                show lance sad at truecenter: 
                    zoom 0.5
                show heartbreak at left:
                    zoom 3
                n "You abandon LANCE on the bridge as he cries like a baby, his life's dreams shattered."
                hide heartbreak
                return
    






'''
label lance_library:
    
    show lance neutral at truecenter: 
        zoom 0.5
    m "Let's study in the library. There are some business texts and such in Olin Library!"
    hide lance neutral
    
    show lance angry at truecenter: 
        zoom 0.5
    show heartbreak at left:
        zoom 3
    l "Bruh. I can't read. Not even a little bit. Peace."
    $ points -= 1
    hide lance angry
    hide heartbreak
    jump Bad_End

label lance_shopping:
    show lance neutral at truecenter: 
        zoom 0.5
    m "We should go shopping. We can go on a costly and hedonistic shopping spree with our parents' money!"
    hide lance neutral
    
    show lance worried at truecenter: 
        zoom 0.5
    l "I already own everything a man could ask for. Anywhere else?"
    hide lance worried

    menu:
        "Come golfing with me.":
            jump lance_golf

        "Buy me Prada... Balenciaga.":
            jump lance_shopping_end

label lance_shopping_end: 
    show lance worried at truecenter: 
        zoom 0.5
    m "Buy me Prada... Balenciaga."
    hide lance worried
    
    show lance angry at truecenter: 
        zoom 0.5
    show heartbreak at left:
        zoom 3
    l "You're just using me for my money."
    l "Goodbye forever."
    $ points -= 1
    hide lance angry
    hide heartbreak
    jump Bad_End

label lance_golf:
    show lance neutral at truecenter: 
        zoom 0.5
    m "Come golfing with me! I would like you and your incredible triceps like to accompany me on the golfing green this weekend!"
    hide lance neutral
    
    show lance proud at truecenter: 
        zoom 0.5
    show heartpoint at left:
        zoom 3
    l "YAS fam, can't wait to show you my swings!"
    $ points += 1
    hide lance proud
    hide heartpoint

    scene bg golf
    n "The next day..."
    n "You've arrived, and see that Lance has already begun hitting balls. You walk up to him."

    show lance proud at truecenter: 
        zoom 0.5
    l "Hey, took you long enough! I've already scored a birdie. What did you think of that?"
    hide lance proud

    menu:
        "That was sooo cool!":
            jump lance_golf1A

        "I can do better.": 
            jump lance_golf1B

        "Why did you hit the ball?! What did it ever do to you?!":
            jump lance_golf1C

label lance_golf1A: 
    show lance neutral at truecenter: 
        zoom 0.5
    m "That was sooo cool! Wow Lance! You have insane golf skills, you could be a pro!"
    hide lance neutral
    
    show lance blush at truecenter: 
        zoom 0.5
    show heartpoint at left:
        zoom 3
    l "Aww, thanks babe."
    $ points += 1
    hide lance blush
    hide heartpoint 
    jump lance_golf2

label lance_golf1B: 
    show lance neutral at truecenter: 
        zoom 0.5
    m "I can do better, amateur. Let me show you how a real golfer gets it done."
    n "You forcefully grab the club from Lance."
    hide lance worried
    
    show lance angry at truecenter: 
        zoom 0.5
    show heartbreak at left:
        zoom 3
    l "That was uncalled for."
    $ points -= 1
    hide lance angry
    hide heartbreak
    jump lance_golf2

label lance_golf1C: 
    show lance neutral at truecenter: 
        zoom 0.5
    m "Hey! Why'd you hit that ball?! What did it ever do to you?!"
    hide lance neutral

    show lance angry at truecenter: 
        zoom 0.5
    l "You are an odd egg."
    hide lance angry
    jump lance_golf2

label lance_golf2: 
    show lance neutral at truecenter: 
        zoom 0.5
    l "Anyway, want to take a swing?"
    hide lance neutral

    menu: 
        "Yes, please show me the ropes!":
            jump lance_golf2A     

        "No, thanks.":
            jump lance_golf2B

        "*get nervous*":
            jump lance_golf2C

label lance_golf2A: 
    show lance neutral at truecenter: 
        zoom 0.5
    m "Help me Lance, I cannot play golf, please guide me through the swing slowly with your strong arms!"
    hide lance neutral

    show lance proud at truecenter: 
        zoom 0.5
    show heartpoint at left:
        zoom 3
    l "Oh, why of course my dear!"
    $ points += 1
    hide lance proud
    hide heartpoint
    jump lance_golf3A

label lance_golf2B:
    show lance worried at truecenter: 
        zoom 0.5
    m "No, thanks. I am against the playing of golf for the environmental effects of the watering of golf courses."
    m "This entire establishment is a waste of our local freshwater resources and I will not stand for it."
    hide lance worried
    
    show lance angry at truecenter: 
        zoom 0.5
    show heartbreak at left:
        matrixcolor TintMatrix("#6967d4") * SaturationMatrix(0.01)
        zoom 3
    l "How dare you insult my favorite pastime!"
    l "You are obviously uncultured if you can't appreciate the finer things in life like the joy of hitting golf balls!"
    $ points -= 1
    hide lance angry
    hide heartbreak
    jump lance_golf3B

label lance_golf2C:
    show lance worried at truecenter: 
        zoom 0.5
    n "You get nervous and your hands get weirdly sweaty. You drop the golf club on your foot and get an ouchie."
    l "You're rather uncoordinated aren't you..."
    hide lance worried
    jump lance_golf3A

label lance_golf3A:
    n "You two spent the afternoon drilling shots. Lance seemed to have a good time."
    
    show lance proud at truecenter: 
        zoom 0.5
    l "I win! It's getting late! I must head to practice now, but that was super fun."
    hide lance proud
    jump lance_dinner

label lance_golf3B:
    n "You and Lance awkwardly continue the date."
    n "Lance did not seem to have a good time."
    
    show lance angry at truecenter: 
        zoom 0.5
    l "You are not fun to play golf with whatsoever. Bye, forever."
    hide lance angry
    jump Bad_End

label lance_dinner: 
    scene bg north
    m "Lance is so CUTE!! I want to meet with Lance again, I should ask him out on a second date!"
    menu: 
        "Call him":
            jump lance_dinner_A

        "Go to his house":
            jump lance_dinner_B

        "Be too shy":
            jump lance_dinner_C

label lance_dinner_A:
    n "You dial Lance's number that you found on Student Center."
    m "Hi Lance! I-"
    
    show lance blush at truecenter: 
        zoom 0.5
    show heartpoint at left:
        zoom 3
    l "Oh [m]! So good of you to call. I was just thinking about calling you. How've you been?"
    $ points += 1
    hide lance blush
    hide heartpoint
    
    show lance fuckboy at truecenter: 
        zoom 0.5
    l " Nevermind that... I have ultradeluxe reservations at Taverna Banfi in Botnell's own Batler Hotel this evening, would you care to join me?"
    hide lance fuckboy
    jump lance_dinner_1

label lance_dinner_B:
    n "You walk to Lance's dorm."
    m "Hi Lance! I just thought I'd come over-"
    
    show lance fuckboy at truecenter: 
        zoom 0.5
    l "Oh my my! What are you doing in my palatial home unannounced?"
    l "Well, that's one way to get a man out on a date... does Taverna Banfi for two interest you?"
    m "Oh.. why yes!"
    hide lance fuckboy
    jump lance_dinner_1

label lance_dinner_C:
    show heartbreak at left:
        zoom 3
    n "You are too shy to talk to Lance and never speak to him ever again."
    n "Lance sees you in class. His eyes pass over you as he goes to greet CRC-chan, the prettiest girl in school."
    n "He will never speak to you again."
    hide heartbreak
    jump Bad_End

label lance_dinner_1: 
    scene bg restaurant
    show lance neutral at truecenter: 
        zoom 0.5
    n "Lance elegantly awaits you at the finest table in all of Taverna Banfi."
    l "Hello [m]. Come, dine with me."
    n "What will you order?"
    hide lance neutral

    menu: 
        "Pasta with butter and choccy milk from the kids menu.":
            jump lance_dinner_1A
        "Just a water with a lime slice.":
            jump lance_dinner_1B
        "A fine steak and a 1969 vintage Dom Peringon Champagne, a wine far out of your tax bracket.":
            jump lance_dinner_1C

label lance_dinner_1A: 
    show lance neutral at truecenter:
        zoom 0.5
    m "I would like pasta with butter and choccy milk from the kids menu."
    hide lance neutral

    show lance worried at truecenter:
        zoom 0.5
    show heartbreak at left:
        zoom 3
    l "Ordering from the children's menu?"
    l "I'm afraid you can't do that dear, it's for 12 and under only. You seem to have no class."
    $ points -= 1
    hide lance worried
    hide heartbreak
    jump Bad_End

label lance_dinner_1B: 
    show lance neutral at truecenter:
        zoom 0.5
    m "I would like just a water with a lime slice."
    hide lance neutral

    show lance worried at truecenter:
        zoom 0.5
    l "Huh. That's a strange thing to order at a restaurant such as this."
    hide lance worried
    jump lance_dinner_2

label lance_dinner_1C:
    show lance neutral at truecenter:
        zoom 0.5
    m "I would like a fine steak and a 1969 vintage Dom Peringon Champagne, a wine far out of my tax bracket."
    hide lance neutral

    show lance fuckboy at truecenter:
        zoom 0.5
    show heartpoint at left:
        zoom 3
    l "What fine exquisite taste you have madame! I commend you."
    $ points += 1
    hide lance fuckboy
    hide heartpoint
    jump lance_dinner_2

label lance_dinner_2:
    show lance proud at truecenter:
        zoom 0.5
    n "The dinner is going well and you and Lance talk for an hour."
    l "It's nice to take a break after working so hard on my money management and asset-selling stock-rising business."
    hide lance proud

    show lance worried at truecenter:
        zoom 0.5
    l "I love my work, but sometimes it really takes a toll."
    hide lance worried

    menu: 
        "I want to support him!":
            jump lance_dinner_2A

        "What does your business do again?":
            jump lance_dinner_2B

        "Give him advice on his vague business plans.":
            jump lance_dinner_2C

label lance_dinner_2A:
    show lance worried at truecenter:
        zoom 0.5
    m "I want to support you in all your business endeavors!"
    hide lance worried

    show lance blush at truecenter:
        zoom 0.5
    show heartpoint at left:
        zoom 3
    l "Thanks, that means a lot to me."
    $ points += 1
    hide heartpoint

    l "People are always shooting my ideas down."
    hide lance blush
    jump lance_dinner_3

label lance_dinner_2B:
    show lance worried at truecenter:
        zoom 0.5
    m "Wait a minute... what does your money management asset-selling stock-rising business actually do again?"
    l "Oh... you dont know?"
    l "But I talk about it constantly to the point where it may be considered slightly annoying..."
    l "Oh well, let me just spend another hour re-explaining to you..."
    hide lance worried

    n "Lance explains his business to you a second time. The dinner continues and seems to go well."
    jump lance_dinner_3

label lance_dinner_2C:
    show lance worried at truecenter:
        zoom 0.5
    m "I understand you want to build your business, but are you sure that this company has an ethical basis in today's modern society?" 
    m "Are you really ready to brave the treachourous pitfalls of today's economy and bring a multifaceted business such as this into the market?"
    m "I think there may be some things you should rethink about this business plan, bucko."
    hide lance worried

    show lance angry at truecenter:
        zoom 0.5
    show heartbreak at left:
        zoom 3
    l "You think you can tell me how to run my business?! I am prepared! I've been telling you! Are you not listening to me? I hate you! We're over!"
    $ points -= 1
    hide lance angry
    hide heartbreak

    show lance sad at truecenter:
        zoom 0.5
    n "Lance runs and sobs because he got his feelings hurt."
    hide lance sad
    jump Bad_End

label lance_dinner_3: 
    show lance blush at truecenter:
        zoom 0.5
    l "I want to find someone who will never stop me from pursuing my dreams of obtaining unimaginable wealth."
    n "The lights dim. Lance leans in close and his eyes sparkle in the candlelight. What a romantic moment!"
    m "*thinking* This is an important moment. I should be really careful with my words."
    hide lance blush

    menu: 
        "Profess your love! <3" if points > 3:
            jump lance_dinner_3A

        "Support him as just friends.":
            jump lance_dinner_3B

        "REJECT HIS EXISTENCE AND RUIN HIS DREAMS AFTER PRETENDING TO BE HIS FRIEND.":
            jump lance_dinner_3C

label lance_dinner_3A:
    show lance blush at truecenter:
        zoom 0.5
    m "I will always support you Lance, because I LOVE you!"
    l "I..."
    hide lance blush

    show lance love at truecenter:
        zoom 0.5
    show heartpoint at left:
        zoom 3
    l "I love you too!"   
    n "His eyes sparkle with love! He leans in for a kiss. The kiss tastes metallic."
    l "I want you to stay with me as my partner both in life and in business!"
    l "Thank you for listening and supporting me."
    $ points += 1
    hide lance love
    hide heartpoint

    show lance fuckboy at truecenter:
        zoom 0.5
    l "Now let's get this bread!"
    hide lance fuckboy

    if points > 5:
        jump Good_End
    else: 
        jump Neutral_End_Love

label lance_dinner_3B:
    show lance blush at truecenter:
        zoom 0.5
    m "Yeah I support you in your business thingamajiggy. I'll always be your good pal, buddy!"
    hide lance blush

    show lance worried at truecenter:
        zoom 0.5
    l "Oh... um... you're my friend too... buddy."
    hide lance worried
    jump Neutral_End_Friend

label lance_dinner_3C:
    show lance blush at truecenter:
        zoom 0.5
    m "I have something to tell you sweetheart."
    l "Yes, [m]?"
    hide lance blush

    show lance sad at truecenter:
        zoom 0.5
    show heartbreak at left:
        zoom 3
    m "I was only talking to you in order to hear all of your business plans and use them for my competing business in the same market! Get owned Richie!"
    n "You abandon Lance at the table as he cries like a baby, his life's dreams shattered."
    $ points -= 1
    hide lance sad
    hide heartbreak
    jump Bad_End

label Bad_End: 
    scene bg duffield
    show lance sad at truecenter:
        zoom 0.5
    n "Lance does not reciprocate your feelings. He rejects your advances."
    l "Sorry, I don't think I'm interested anymore."
    n "You have betrayed Lance's trust and he hates you forever. Nice going, dumbass."
    n "THE END - RICHARD ROUTE - BAD ENDING."
    hide lance sad
    return

label Neutral_End_Friend: 
    scene bg duffield
    show lance neutral at truecenter:
        zoom 0.5
    n "You and Lance stay as friends for the rest of college."
    n "THE END - RICHARD ROUTE - NEUTRAL ENDING (FRIEND)."
    hide lance neutral
    return

label Neutral_End_Love: 
    scene bg duffield
    show lance blush at truecenter:
        zoom 0.5
    n "You date Lance for the rest of college."
    n "THE END - RICHARD ROUTE - NEUTRAL ENDING (LOVE)."
    hide lance blush
    return

label Good_End: 
    scene bg duffield
    show lance love at truecenter:
        zoom 0.5
    n "You and Lance walk to Duffield Atrium and get married and live happily ever after."
    n "THE END - RICHARD ROUTE - GOOD ENDING (LOVE)."
    hide lance love
    return
'''