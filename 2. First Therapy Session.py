# this is made by Kevin Sanchez
import time

print("""Dr. Hill: Before we begin, there are a few things I need to make sure you understand. You see, no one can
change what happened last year. The past is beyond our control. You have to accept this in order to move forward.
But there is freedom in this revelation. Everything you do, every decision you make from now on, will open doors to the
future. I want you to remember this. I want you to remember this as you play your game. Every single choice will affect
your fate, and the fate of those around you.""")
time.sleep(23)

print("""
--
Dr. Hill: So, you have committed to commence with this 'game'. This is significant. And I want to help you see
it through. Sometimes... Sometimes these things can be a little scary... even terrifying... but I am here to make sure
that no matter how upsetting things may get, you'll always find a way to work through it.""")
time.sleep(13)

print("""
--
Dr. Hill: Alright. We will start with a simple exercise. Could you please pick up the card? And I want you to look at
the picture on the other side, and tell me what you feel about it. It is essential that you answer honestly in order to
get the most out of this experience.""")

card = input("""
--
    You flip the picture, its daytime and saw a scarecrow in the middle of the field with a barn behind it.

Dr. Hill: So... how did that picture make you feel? Remember: be honest.

It makes me happy or I feel uneasy. (1) / (2)""")
# describe them more vividly
if card == "1":
    input("That's good. In what way it made you happy? The sunshine or It's peaceful. (1) / (2)")
    if card == "1":
        input("Dr. Hill: Sunshine! I see. So which word would describe how you feel about darkness?"
              "I feel depressed or It scares me. (1) / (2)")
        if card == "1":
            print("--")
            print("Dr. Hill: Well, winter nights are cold and dark. Depression... feelings of loneliness are not "
                  "uncommon.")
            print("")
            input("Dr. Hill: This night, in which your game takes place, is particularly cold and dark... I would "
                  "think that you might feel... isolated at times. Does that bother you?"
                  "Yes, it does or I'd be fine? (1) or (2)")
            if card == "1":
                print("--")
                print("Dr. Hill: Oh! Well... in that case, this game might be a little challenging for you."
                      "Still, there's an opportunity for you here to engage with the others... connect with them."
                      "Before you start to split them up. Before you... isolate them.")
                print("")
                print("Dr. Hill: Oh! Well it seems we have uncovered some significant topics to explore in our next"
                      "session. But, for now, we're out of time. Have fun... on your own... until then...")
                print("")
                print("Dr. Hill proceeds to stand up from his chair and walks over to the nearby window, "
                      "humming a tune as he goes.")

            elif card == "2":
                print("--")
                print("Dr. Hill: Well! Not much of a people-person, are we?")
                print("")
                print("Dr. Hill: Well it seems we have uncovered a significant topic to explore in our next session."
                      "But, for now, we're out of time. Have fun on your own until then.")
                print("")
                print("Dr. Hill proceeds to stand up from his chair and walks over to the nearby window, "
                      "humming a tune as he goes.")
        elif card == "2":
            print("--")
            print("Dr. Hill: Afraid? Really? That's interesting. Where I come from, way up North in Sweden, the "
                  "nights are 18 hours long. And why do you think you are afraid of the dark?")
            input("Everyone fears it or I don't know. (1) / (2)")
            if card == "1":
                print("--")
                print("Dr. Hill: No. No no no. Not everyone but it's a perfectly natural fear. Darkness after all, is "
                      "the unseen and therefore the unknown... And what could inspire fear more than the terror of"
                      "uncertainty?")
                print("")
                print("Dr. Hill looks at his watch.")
                print("")
                print("Dr. Hill: Oh dear. We seem to be out of time for this session. We'll talk again, soon. Until "
                      "then I suggest you stay away from... dark places.")
                print("")
                print("Dr. Hill proceeds to stand up from his chair and walks over to the nearby window, "
                      "humming a tune as he goes.")

            elif card == "2":
                print("--")
                print("Dr. Hill: Well... it's a perfectly natural fear. Darkness after all, is the unseen and "
                      "therefore the unknown... And what could inspire fear more than the terror of uncertainty? "
                      "We seem to be out of time for this session, but we'll talk again very soon.")
                print("")
                print("Dr. Hill proceeds to stand up from his chair and walks over to the nearby window, "
                      "humming a tune as he goes.")

    elif card == "2":
        print("--")
        input("Dr. Hill: Ahh. Interesting. It's interesting. So would it make you happy to spend a whole week here..."
              "all by yourself? Yes or No.").lower().strip()
        if card == "yes":
            input("Dr. Hill: And what if I told that this cottage... was haunted?"
                  "I wouldn't care or I'd be scared. (1) / (2)""")
            if card == "1":
                print("--")
                print("Dr. Hill: Ah, what lies beyond the veil of death is after all, the ultimate unknown. And what "
                      "could inspire fear more than the terror of uncertainty? Ah I'm sorry, we're out of time for "
                      "this session... we'll talk again very soon.")
                print("")
                print("Dr. Hill proceeds to stand up from his chair and walks over to the nearby window, "
                      "humming a tune as he goes.")

            elif card == "2":
                print("--")
                print("Dr. Hill: Ahh... a level headed response. But... everyone is frightened of something... I "
                      "wonder what it is that does frighten you? I really do. Sorry! We're out of time. Let's "
                      "investigate that in our next session, shall we?")
                print("")
                print("Dr. Hill proceeds to stand up from his chair and walks over to the nearby window, "
                      "humming a tune as he goes.")
        if card == "no":
            print("--")
            input("""
            --
            Dr. Hill: And why is that?
            I'd be lonely or  I'd be scared. (1) / (2) """)
            if card == "1":
                print("--")
                print("Dr. Hill: Oh, well. There is a fine line between the peacefulness of solitude and the "
                      "loneliness of isolation. This is something we need to explore further, don't you agree? But I'm "
                      "afraid we're out of time for now. Until our next session, try to surround yourself with "
                      "friends... in a place that makes you feel... safe.")
                print("")
                print("Dr. Hill proceeds to stand up from his chair and walks over to the nearby window, "
                      "humming a tune as he goes.")

            elif card == "2":
                print("--")
                print("Dr. Hill: Oh, there's something in that picture that scares you?")
                input("The Scarecrow or I'm not sure. (1) / (2)")
                if card == "1":
                    print("--")
                    print("Dr. Hill: Well of course, a man hanging in a field is a naturally unsettling image. "
                          "...But perhaps we can explore your fears a bit further in our next session. I'm afraid "
                          "we're out of time.")
                    print("")
                    print("Dr. Hill proceeds to stand up from his chair and walks over to the nearby window, "
                          "humming a tune as he goes.")

                elif card == "2":
                    print("--")
                    print("Dr. Hill: Well... that is very interesting... I'm afraid we're out of time. But please - "
                          "I would like you to contemplate what is it that is missing from that picture? This thing "
                          "that is driving your fear? We need to unwrap it. Next time.")
                    print("")
                    print("Dr. Hill proceeds to stand up from his chair and walks over to the nearby window, "
                          "humming a tune as he goes.")
elif card == "2":
    print("--")
    print("Dr. Hill: Okay... Honesty is good. But what do you think it is that makes you feel... uneasy?")
    input("The Scarecrow or I'm not sure. (1) / (2)")
    if card == "1":
        print("--")
        print("Dr. Hill: I see... I see... Let's say the scarecrow were not there... Would you feel comfortable "
              "staying there on your own for a period of time? Say a week, for example?")
        input("Sure or No I wouldn't. (1) / (2)")
        if card == "1":
            print("--")
            print("Dr. Hill: And what if I told you that this cottage... was haunted?")
            input("I wouldn't care or I'd be scared. (1) / (2)")
            if card == "1":
                print("--")
                print("Dr. Hill: So the scarecrow frightens you... and yet you don't appear to be bothered by the "
                      "possibility of the supernatural... I suspect that someone is not being entirely honest with me. "
                      "Our time's up, let's investigate that in our next session, shall we?")
                print("")
                print("Dr. Hill proceeds to stand up from his chair and walks over to the nearby window, "
                      "humming a tune as he goes.")
            elif card == "2":
                print("--")
                print("Dr. Hill: Ah. Alright, alright, I sense that you suffer from a significant fear of... of the "
                      "supernatural. What lies beyond the veil of death is, after all, the ultimate unknown. Don't you "
                      "agree? And what could inspire fear more than the terror of uncertainty?")
                print("")
                print("Dr. Hill pauses for a moment.")
                print("")
                print("Dr. Hill: Please remember... this is only a game.")
    elif card == "2":
        print("--")
        input("Dr. Hill: If it is something you cannot see, then why does it make you feel uneasy? I mean, is "
              "there something in the house? It's in the house or No, It's not there. (1) / (2) ")
        if card == "1":
            print("--")
            input("Dr. Hill: And this thing in the house... is it alive? It's alive or I don't know. (1) / (2) ")
            if card == "1":
                print("--")
                print("Dr. Hill: I see... and is this threat human or is there some... other fear that you would "
                      "like to talk to me about? It's human or It's not human. (1) / (2) ")
                if card == "1":
                    print("--")
                    print("Dr. Hill: An unseen human threat inside of the house. That's a unique perspective... "
                          "Ah dear. We will have to explore your fears further in our next session, I'm afraid our "
                          "time is up for now.")
                    print("")
                    print("Dr. Hill proceeds to stand up from his chair and walks over to the nearby window, "
                          "humming a tune as he goes.")
                elif card == "2":
                    print("--")
                    print("Dr. Hill: Huh. So if it's not in the house then where do you think it is? Can it be in the "
                          "field? It's in the field or It's not there. (1) / (2) ")
                if card == "1":
                    print("--")
                    input("Dr. Hill: I see... and is this threat human, or is there some... other fear that you would "
                          "like to talk to me about? It's human or It's not human. (1) / (2)")
                    if card == "1":
                        print("--")
                        print("Dr. Hill: So you think there's a person in this field that is a threat to you? That's "
                              "quite intriguing. Ah well! Perhaps we can explore your fears a bit further in our next "
                              "session. I'm afraid we've run out of time.")
                        print("")
                        print("Dr. Hill proceeds to stand up from his chair and walks over to the nearby window, "
                              "humming a tune as he goes.")
                    elif card == "2":
                        print("--")
                        print("Dr. Hill: An inhuman threat. That's fascinating. Ah well! Perhaps we can explore your "
                              "fears a bit further in our next session. I'm afraid we've run out of time.")
                        print("")
                        print("Dr. Hill proceeds to stand up from his chair and walks over to the nearby window, "
                              "humming a tune as he goes.")
                elif card == "2":
                    print("--")
                    print("Dr. Hill: Is this threat... real? Or is it something... in your imagination?")
                    input("It's Real or It's in my Head. (1) / (2)")
                    if card == "1":
                        print("--")
                        print("Dr. Hill: Oh! Ah well, perhaps we can explore your fears a bit further in our next "
                              "session. I'm afraid... we've run out of time.")
                        print("")
                        print("Dr. Hill proceeds to stand up from his chair and walks over to the nearby window, "
                              "humming a tune as he goes.")
                    elif card == "2":
                        print("--")
                        print("Dr. Hill: Ah. You seem to possess a very active imagination. Perhaps we explore your "
                              "fears a bit further in the next session. I'm afraid... We've run out of time.")
                        print("")
                        print("Dr. Hill proceeds to stand up from his chair and walks over to the nearby window, "
                              "humming a tune as he goes.")