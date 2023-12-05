define e = Character("loki", color="#16a00a")

default question_tally = 0                                  # variable used in question_selector
$ animal = ''                                               # variable to store the chosen animal


###


label start:
    scene bg tree                                       # SCREEN 1
    show loki neutral
    e "Ah, here you are my fellow time traveler, I sorta need your help, the multiverse depends on you, follow me"
    
    show loki neutral at left with move
    label the_question:                                     # SCREEN 2
        scene bg portals toh scott
        show loki neutral at left with move
        e "Debemos ir por uno de estos portales {u}rapido{/u} o \"no podremos seguir\""
        call question_selector

        menu:                                               # SCREEN 3
            "toh":      # SCREEN 4-1                          # FOX
                scene bg lumity 1
                show lumity dance
                "..."
                show lumity scared at left with moveinleft
                "toh!Juli" "{i}Someone{/i} is here, I can barely see them{size=+10}why are they...{/size}"
                jump quick_fox_path
            "scott":                                 # DOG
                hide eileen with dissolve                   # SCREEN 4-1
                $ animal = 'dog'
                "Eileen" "{b}Yes{/b}, because I am... {color=#808080}always... {size=-5}sleepy...{/size}{/color}"
                jump lazy_dog_path
            "Question [question_tally]: [repeat_question]": # SCREEN 4-3
                jump the_question
        jump end

label question_selector:
    $ NumberGenerator = renpy.random.randint(1, 3)
    if NumberGenerator == 3:
        $ repeat_question = "What?"
    elif NumberGenerator >= 2 and NumberGenerator < 3 or NumberGenerator == 5:
        $ repeat_question = "Say that again?"
    else:
        $ repeat_question = "Huh?"
    $ question_tally += 1
    return

label quick_fox_path:
    # Path for "The Quick Fox" option
    scene forest with fade
    show eileen vhappy at right
    e "Eileen danced through the enchanted forest, showcasing her incredible speed."
    jump to_concert

label lazy_dog_path:
    # Path for "The Lazy Dog" option
    scene bedroom with fade
    show eileen sleepy at right
    e "Eileen curled up in a cozy bed, embracing her love for peaceful naps."
    return to_concert

label to_concert:
    # Common part for both paths
    menu:
        "Continue to Concert":  # CONTINUE
            jump alternate_ending
        "Stay in the Forest":    # STAY_FOREST
            scene forest with fade
            e "Eileen decided to stay in the enchanted forest, exploring its mysteries."
            jump to_concert
        "Explore the Castle":    # EXPLORE_CASTLE
            scene castle with fade
            e "Eileen embarked on a journey through the castle, discovering its secrets."
            jump to_concert

label alternate_ending:
    scene bg_alter_ending
    show eileen shocked
    e "As Eileen reached the concert, a magical portal appeared!"
    e "Eileen had a choice to make..."

    menu:
        "Enter the Portal":    # ENTER_PORTAL
            scene bg_portal with fade
            e "Eileen bravely entered the portal, eager for new adventures in a different realm."
            return end_alternate
        "Stay at the Concert": # STAY_CONCERT
            e "Eileen chose to stay at the concert, enjoying the music and festivities with newfound friends."
            jump end_concert

label end_alternate:

    scene mystical_realm with vpunch
    e "Eileen's journey continued in a mystical realm, filled with magic and wonders."

    return

label end_concert:
   
    scene concert1 with vpunch
    e "Eileen danced the night away, surrounded by the joyous melodies of the concert."

    return
