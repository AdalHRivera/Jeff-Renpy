# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image bg black = "images/black.jpg"
image bg houseext = "images/BG_house_exterior.jpg"
image bg houseint = "images/BG_house_interior.jpg"
image bg busstop = "images/BG_bus_stop.jpg"
image bg funeral = "images/BG_backyard_night.jpg"
image bg bathroom1 = "images/BG_bathroom1.jpg"
image bg hospital = "images/BG_hospital.jpg"
image bg bathroom2 = "images/BG_bathroom2.jpg"
image bg scream = "images/JEFF.jpg"

image jeff = "sprites/Jeff/normal.png"
image jeff happy = "sprites/Jeff/happy.png"
image jeff annoyed = "sprites/Jeff/annoyed.png"
image jeff angry = "sprites/Jeff/angry.png"
image jeff shock = "sprites/Jeff/shock.png"
image jeff blood = "sprites/Jeff/normalB.png"
image jeff annoyed blood = "sprites/Jeff/annoyedB.png"
image jeff angry blood = "sprites/Jeff/angryB.png"
image jeff shock blood = "sprites/Jeff/shockB.png"
image jeff insane = "sprites/Jeff/insane.png"

image liu = "sprites/Liu/normal.png"
image liu happy = "sprites/Liu/happy.png"
image liu annoyed = "sprites/Liu/annoyed.png"
image liu angry = "sprites/Liu/angry.png"
image liu shock = "sprites/Liu/shock.png"
image liu blood = "sprites/Liu/normalB.png"
image liu annoyed blood = "sprites/Liu/annoyedB.png"

image patrick = "sprites/Pat/normal.png"
image patrick annoyed = "sprites/Pat/annoyed.png"
image patrick shock = "sprites/Pat/shock.png"

image cop = "sprites/Cop/cop.png"

# Declare characters used by this game.
define j = Character('Jeff', color="#f00")
define l = Character('Liu', color="#33f")
define d = Character('Dad', color="#c30")
define m = Character('Mom', color="#f06")
define p = Character('Patrick', color="ff0")
define c = Character('Cop', color="#33c")


# The game starts here.
label start:

    $ kill = False
    $ coward = False
    $ confess = False
    $ sacrifice = False

    play music "music/intro.mp3"

    scene bg black

    "The Rupertsons arrive at their new home in a quiet suburban town."

    scene bg houseext
    with fade

    "It had been a very long trip, but the car slows to a halt in front of the house."
    "Jeff and Liu wake up from their uncomfortable sleeping positions in the backseat..."

    show jeff at left
    show liu at right
    with easeinleft

    j "Finally!"
    l "Would you look at that!"
    m "So, what do you think? Doesn't the house look nice?"
    j "Are you kidding? This is cool!"
    d "It definitely makes this boring trip worth it, right?"
    l "Sure does!"

    show liu happy

    l "Hey, Jeff, how about we go and explore the house?"

    show jeff happy

    j "Sounds like a good idea! Come on!"

    hide liu
    hide jeff
    with easeoutright

    scene bg houseint
    with fade

    show jeff happy at left
    show liu happy at right
    with easeinright

    j "Wow! Isn't this neat?"
    l "Ha, ha, ha! Race you to the rooms!"

    hide liu
    with easeoutleft

    show jeff annoyed

    j "Liu!"

    hide jeff
    with easeoutleft

    scene bg houseext
    with fade

    m "*sigh*"
    m "These kids do seem very happy to see the house."
    d "Good thing, dear. They haven't been like this since the incident."
    m "Yeah... Especially Jeff..."
    j "Come on, Mom! Check out the view from up here!"
    m "Oh! I'm coming, honey!"

    scene bg black
    with fade

    "Days pass. The Rupertsons settle down on their new abode."
    "Jeff's mom begins to open up to her neighbors, and the kids grow excited as the first day of school grows near."
    "Until finally..."

    scene bg busstop
    with fade

    show jeff
    with easeinbottom

    j "(I'm actually nervous.)"
    j "(I'm returning to having a normal life...)"
    j "(Will I really be able to fit in?)"

    show jeff at left
    show liu happy at right
    with easeinright

    l "What's troubling you, Jeff?"
    l "Don't worry! School will go easy. They always go easy on the new kids."

    play sound "sfx/skating.mp3"
    play music "music/suspense.mp3"

    "Suddenly, skateboards begin to roll out of nowhere."
    "A band of nasty-dressed bullies circle around Jeff and Liu."
    "One of them approaches the two and smiles menacingly..."

    show liu
    hide liu
    with easeoutright

    show jeff at right
    show patrick at left
    with easeinleft

    p "Patrick's the name, pain is my game!"
    j "(That is so lame...)"
    p "So, two newbies, huh? Interesting..."
    l "We don't want any problems here."
    p "Oh, there's no problem going on at all, little guy."
    p "That is, if you have your bus fare ready."
    l "Bus fare? What the hell are you talking about?"
    p "A bus fare, kid. As in, a fare for getting on the bus."
    p "Everyone who gets on MY bus has to pay ME the bus fare."

    show jeff annoyed at right

    j "That's just stupid!!"
    l "Jeff! Calm down!"
    p "Quite the mouth, eh, little one? Guess that makes you first in line."

    show patrick annoyed

    p "Come on, I ain't got all day."

    menu:
        "Give lunch money":
            jump lunchmoney

        "Punch in the gut":
            jump fight

        "Run away":
            jump run

label run:

    show jeff at right

    "Jeff breaks into a sprint and dashes away from Patrick, much to his own surprise."

    hide patrick
    with easeoutleft

    hide jeff
    with easeoutright

    show jeff
    with easeinleft

    "One of the bully skateboarders attempts to stop him with a punch."

    menu:
        "Evade":
            jump runaway

        "Punch him back":
            jump murder

label runaway:

    with vpunch

    "Jeff rolls below the trajectory of the incoming blow, picking up his speed as he dashes away."

    hide jeff
    with easeoutright

    l "JEFF!! WHERE ARE YOU GOING??"

    "Jeff can't hear his brother over his determination to get away from that fight."

    $ coward=True
    scene bg black
    with fade

    jump police

label lunchmoney:

    j "Fine. Here."

    "As Jeff hands Patrick everything he has on his wallet, Patrick socks him in the chest."

    play sound "sfx/punch.mp3"

    show jeff shock
    with vpunch

    j "*GASP* *GASP* *GASP*"

    hide patrick
    show patrick

    p "Ha, ha, ha, ha, ha! That's for bitching up on me up front!"

    show jeff angry

    "Jeff's eyes begin to see red..."

    jump fight

label fight:

    "Before Patrick even realizes what Jeff has in mind, Jeff jabs his abdomen repeatedly."
    play sound "sfx/punch.mp3"
    play sound "sfx/sock.mp3"
    show patrick shock
    with hpunch

    "The bully skateboarders hurl themselves at both Liu and Jeff, punches flailing in every direction."

    hide patrick
    with easeoutleft
    show jeff angry at center
    play sound "sfx/punch.mp3"
    with hpunch
    with easeinright

    "Jeff thrusts his arms in various directions. Every way they go, his hands grab a limb and twist it."
    play sound "sfx/punch.mp3"
    with hpunch
    play sound "sfx/crack1.mp3"
    with hpunch
    "Cries of pain and clean loud cracks are heard as bones snap here and there."
    with hpunch
    play sound "sfx/crack2.mp3"
    with hpunch
    play sound "sfx/crack3.mp3"
    with hpunch
    "One bully attempts to tackle Jeff and neutralize him."

    jump murder

label murder:

    show jeff angry

    "Jeff quickly takes him by the wrist and ravages his arm before throwing himself at the bully."
    play sound "sfx/crack5.mp3"
    with hpunch
    with hpunch
    with hpunch
    "His punches begin to draw blood..."
    show jeff angry blood
    play sound "sfx/crack4.mp3"
    play sound "sfx/crack1.mp3"
    play sound "sfx/punch.mp3"
    with hpunch
    "A thick puddle begins to grow under the pinned down bully..."
    play sound "sfx/punch.mp3"
    play sound "sfx/crack2.mp3"
    with hpunch

    hide jeff
    show liu shock

    l "Jeff, STOP!!"

    "Upon hearing his brother, Jeff returns to his senses and jumps back at the horror he caused..."

    hide liu
    show jeff shock blood
    play music "music/shock.mp3"

    "Laying in front of him is the body of the bully he was beating down..."


    "...headless."
    "His head has been smashed like a watermelon into the ground."

    $ kill = True

    p "What the-?!"
    j "..."

    "Shocked, Jeff stands frozen on the street..."

    l "Run, Jeff!! RUN!!!"

    "Liu grabs Jeff by his sweater and pulls him away from the bullies..."

    hide jeff
    with easeoutright

    scene bg black
    with fade

    "...away from the carnage..."

    jump police

label police:

    scene bg black
    with fade

    "Later that night..."
    "Jeff is walking to his house..."

    if kill:
        l "Okay, please tell me you can come up with something to explain this..."

    j "(It's too late to lie about school being great...)"

    if kill:
        j "(...and my clothes are drenched in blood...)"
        l "Jeff, HIDE!"
        j "What?!"
        l "The COPS!!"

    if coward:
        j "!!"
        j "(The cops!)"

    play music "music/scary.mp3"

    scene bg houseext
    show cop
    with fade

    "A police car is parked in front of the house..."
    "A single cop is at the door, talking to Jeff's mom about something..."

    if kill:
        j "This is bad."
        l "So, so bad..."
        j "(What do I do??)"

        menu:
            "Go and confess to the cops":
                jump confess

            "Talk it with Liu":
                jump sacrifice

    if coward:
        jump sacrifice

label sacrifice:

    $ sacrifice = True

    if kill:
        j "What do we do?"
        l "I don't think there is a choice, Jeff."
        l "We can't run anywhere."
        l "..."
        j "..."
        l "I'm turning myself in."
        j "What?!"

        "Before Jeff even finishes his exclamation, Liu is walking towards the cop."

    if coward:
        j "(Crap...)"
        j "(Mom probably called the cops on me and will yell at me on sight.)"
        j "(Better stay hidden for a while until the cop leaves...)"
        "Whatever conversation Jeff's mom is having with the policeman, the two don't seem to finish off very soon..."
        j "(Please... just go...)"

    jump bargein

label confess:

    $ confess = True
    j "I'm going to confess everything."
    l "No, Jeff! What will happen to you??"
    j "I don't know!"
    j "But today, I don't want to lie anymore!"

    "Jeff walks towards the house, where the cop continues talking with his mom."

    j "Mom..."

    m "JEFF!! Where were you?!?!"

    show cop at right
    show jeff blood at left
    with easeinleft


    if kill:
        m "OH MY GOD!! What happened to your clothes?!?!"

    j "I, uhh... have to tell you something..."

    jump bargein

label bargein:

    c "What, who are you?"

    show cop at right
    with easeinleft

    if confess:
        show jeff blood at left
        with easeinleft

        j "My name is Jeff."
        j "You're likely here because of... what happened this morning."
        c "There was a murder at the bus stop, alright..."
        if kill:
            c "By the looks of it, you were involved in it, kid."
            c "Say, what can you tell me?"
        else:
            c "But you don't look like the kind of guy who does that."
            c "Did you have something to report?"

        j "Well..."
        l "It was me."

        show jeff shock blood

        j "!!"
        c "!!!"
        m "Liu!"

        show jeff shock blood at center
        show liu blood at left
        with easeinleft

        l "I was defending my brother from some bullies."
        l "I guess I got too angry."

        show jeff annoyed blood

        j "But Liu! I did-"

        show liu annoyed blood

        l "C'mon, Jeff! Look at my hands!"
        "Indeed, Liu's hands were covered in blood."
        "Unbeknownst to both Jeff and the cop, it was Liu's own blood."
        "His ass had been kicked."
        l "You were helpless!"
        j "Liu! No!"
        l "It's ok, Jeff. What's done is done."

        jump arrest

    if sacrifice:

        show liu blood at left
        with easeinleft

        l "I am Liu."
        m "My God, Liu, where have you been?!"
        l "Mom, sir."
        l "To make a long story short."
        l "It was me."
        c "Excuse me?"
        l "I guess you're inquiring about the accident this morning."
        c "Then that means you know some information about it."
        l "Yes I do. In fact, I just told you."
        l "It was me."
        m "LIU?!"
        if coward:
            "In all his desperation to escape, Jeff had forgotten about Liu."
            "Liu took the blow for him, and now he's taking the blame."

    jump arrest


label arrest:
    c "Sir, whether you're telling the truth or not, I'm afraid I'll have to take you in."
    l "I'm sorry, Mom."
    m "*sob*"

    hide liu
    hide cop
    with easeoutright

    if kill:
        show jeff shock blood at center
        with fade
    else:
        show jeff shock at center
        with fade

    j "Liu..."
    j "Why..."

    scene bg black
    with fade

    stop music

    "And so, Liu gets sentenced to five years in juvenile detention..."
    "Jeff's guilt begins to eat away at him..."

    "PART II COMING SOON"


    if coward:
        scene bg scream
        play sound "sfx/scream.ogg"
        with hpunch
        with hpunch
        with hpunch
        with hpunch

    scene bg black

    return
