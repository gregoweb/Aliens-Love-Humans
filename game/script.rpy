# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bgcity

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play music "alienslove.mp3" fadeout 1.0 fadein 1.0

    "Look what a beautiful night we have tonight.. The city is full of love !"
    "That's why some lonely Aliens come to planet Earth to really feel the the power of love"
    $ customer = 0
    $ totalcash = 0
    $ currency = 0
    $ tuto = 3
    $ alienscar = ['Suzy','kind','girl','Bob','rough','girl','Alfred','kind','boy','Dominic','rough','boy']
    $ satisfaction = 50

    while satisfaction > 0:
        $ satisfaction = 50
        show ufo:
            xalign .49 yalign 0.0
            linear 1.0 yalign .35


        #$ al = renpy.random.choice(['alien1', 'alien2', 'alien3'])
        #image alien = "[al].png"

        $ d4roll = renpy.random.randint(0, 3)
        $ mood = renpy.random.choice(['fav','dif'])
        image alien = "alien[d4roll] [mood].png"

        show alien:
            xalign 0.18
            yalign .69

        "We have a  new customer"

        if tuto > 0:
            $ tuto -= 1
            if mood == 'fav':
                "Look at those eyes ! We have a customer who knows what he wants"
            else:
                "Look at those eyes ! This customer seems to be shy"
        #endif
        $ aliensname = alienscar [3*d4roll]
        $ personality = alienscar [3*d4roll+1]
        $ gender = alienscar [3*d4roll+2]
        "[aliensname]" "Give me some love, I am looking for a [personality] [gender]"



        menu:
            "kind girl":
                jump kg
            "rough girl":
                jump rg
            "kind boy":
                jump kb
            "rough boy":
                jump rb

        label kg:
            #guessed personality
            $ gpersonality = 'kind'
            $ ggender = 'girl'
            jump guessed
        label rg:
            $ gpersonality = 'rough'
            $ ggender = 'girl'
            jump guessed
        label kb:
            $ gpersonality = 'kind'
            $ ggender = 'boy'
            jump guessed
        label rb:
            $ gpersonality = 'rough'
            $ ggender = 'boy'
            jump guessed

        label guessed:
            if mood == 'fav':
                if personality == gpersonality:
                    $ satisfaction += 25
                else:
                    $ satisfaction -= 25

                if gender == ggender:
                    $ satisfaction += 25
                else:
                    $ satisfaction -= 25
            else:
                if personality != gpersonality:
                    $ satisfaction += 25
                else:
                    $ satisfaction -= 25

                if gender != ggender:
                    $ satisfaction += 25
                else:
                    $ satisfaction -= 25

            $ currency = satisfaction * 10
            play sound "coin.wav"
            "[aliensname]" "Here is your cash : [currency]"
            $ totalcash += currency



        show ufo:
            xalign .49 yalign 0.35
            linear 1.0 yalign 0.0
        "[aliensname]" "Goodbye"
        $ customer += 1

    #endwhile
hide ufo

label goodend:
    "... Well played your total cash is [totalcash] with [customer] customers "
    # This ends the game.

    return
