#cannot click or press enter on the background, the message cannot continue if the user doesn't click the black background 




define e = Character("Eileen")

define j = Character("Jen")
# Main script for the demo!

define n = Character("You")

# NVL characters are used for the phone texting
define n_nvl = Character("You", kind=nvl)
define e_nvl = Character("user1234", kind=nvl)
define j_nvl = Character("feeling_jenerous", kind=nvl)
            

# Let's assume you have a function to initialize contacts

# The game starts here.

label start:
    
    #set up the background 
    #scene room with dissolve
    $ mail = []
    $ mail_queue = []
    $ contacts = []     
    $ user_input = []

    # create a contact the player can send messages to

    # to change the draft message, do something like $ fredo.draft = "fred_draft2"
    # $ fredo.delete() if you don't want him on the list anymore (sorry fred)
    
    show screen message_overlay
    

    $ add_message("Test message", "saguaro", "sup")
    #$ add_message("Test2 message", "saguaro", "sup","sa_reply")
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    # Example of receiving a new message  
    
    ############################################
    #in case need to test the ai algo
    ############################################
    #$ user_input = renpy.call_screen("input", prompt="Say Something?", someText = "")
    #n_nvl "[user_input]"
    
    
    #first scene of introduction
    nvl_narrator "Added Eileen to the group"
    nvl_narrator "Added Jen to the group"
    n_nvl "{image=emoji/wave.png}"
    j_nvl "{image=emoji/wave.png}"
    e_nvl "{image=emoji/wave.png}"
    j_nvl " hi, you can just call me jen"
    j_nvl " i didn't think they'd actually just randomly sort us like this"
    e_nvl " yeah that's odd"
    j_nvl " i guess we'll just see each other around"
    j_nvl "bye for now"
    
    
    #show screen chat_room_selection
    
    #menu (nvl = True):
    #    "Test message":
    #        n_nvl "Test message"
    #        e_nvl "This is a test message."
    #    "Test2 message":
    #        n_nvl "Test2 message"
    #        e_nvl "This is a test message."
    
    
    #$ x = renpy.call_screen("input", prompt="What's your name?", someText = "")
    #n_nvl "My name is [x]"
    #n_nvl "Nice to meet you!"
    #e_nvl "Nice to meet you too! {image=emoji/wave.png}"
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    $ add_message("About future", "feeling_jenerous", "Hi", "jen_reply")
    n "There's new messages in the message box"
    n "I should check them out"
    n "You can reply to the message by clicking the reply"
    
    if check("About future"):
        n "Here we go"
    else :
        n "I should check the message"
    
    
    
    nvl_narrator "The conversation ends"
        
    
    
    #show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return


#the chat room one 
#label open_phone:
#    call screen chat_room_selection
#    
#    return



#label sa_reply(current_message):
#    menu:
#        "Open the message":
#            $ current_message.reply_label = None
#            n_nvl "[current_message.body]"
#            e_nvl "{image=emoji/wave.png}"
#            e_nvl "Thanks"
#            e_nvl "Bye"
#            $ delete_replied("Test2 message")
#        "Ignore the message":
#            pass
#    return


#First part of Jen (about future)
label jen_reply(current_message):
        menu:
            "Open the message":
                #delete the message from the queue
                $ current_message.reply_label = None
                j_nvl "[current_message.body]"
                n_nvl "{image=emoji/wave.png}"
                j_nvl "i finally have some free time"
                j_nvl "i've been working on an assignment all day"
                n_nvl "Are you in school?"
                j_nvl "yeah"
                j_nvl "3rd year of uni"
                menu (nvl = True):
                    "What's your program":
                        n_nvl "What's your program"
                        j_nvl "computer science but specifically it's web design"
                        j_nvl "so i've got opinions about this app's ui haha"
                        n_nvl "Really?"
                        j_nvl "yeah"
                        
                    "That's cool":
                        n_nvl "That's cool"
                        j_nvl "yeah I guess so"
                j_nvl "honestly i'm not really sure what i'm doing"
                j_nvl "hopefully i'll figure it out by the time i graduate"
                n_nvl "What's your plan after graduating?"
                j_nvl "uhhhh find a job?"
                j_nvl "honestly i'm not really sure"
                j_nvl "which isn't great"
                j_nvl "i mean i've done a few co-op terms but i didn't really click with any of them"
                j_nvl " i don't know if i'm even in the right field"
                j_nvl "maybe i'll just go back to school"
                j_nvl "but i can't do that forever but i also can't really come up with anything"
                
                $ delete_replied("About future")
                $ add_message("About Hobbies", "feeling_jenerous", "Hi", "jen_reply2")
                $ add_message("Sleeping Problem", "user1234", "Hi", "lain_reply")
                
                
                #$ x = renpy.call_screen("input", prompt="Say Something?", someText = "")
                #$ player = renpy.input("what is your name?")
                #n_nvl "[x]"
                
                
            "Ignore the message":
                pass
        return

#Second part of Jen (about hobbies)
label jen_reply2(current_message):
    menu:
        "Open the message":
            $ current_message.reply_label = None
            j_nvl "[current_message.body]"
            n_nvl "Hi. Free time again?"
            j_nvl "yeah"
            j_nvl "got lucky this week, i didn't have a lab"
            j_nvl " so i'm just spending that time drawing"
            menu (nvl = True):
                "You draw?":
                    n_nvl "You draw?"
                    j_nvl "when i have the time"
                    j_nvl "it's just a hobby"
                    n_nvl "That's cool"
                    j_nvl "yeah"
                "What do you like to draw?":
                    n_nvl "What do you like to draw?"
                    j_nvl "i like flowers"
                    j_nvl "i used to draw a ton of them all over my notebooks"
                    j_nvl "still do, when i'm zoning out in my lecture"
            n_nvl "What are you drawing?"
            j_nvl "i don't really know yet"
            j_nvl "just kinda been doodling"
            j_nvl "school takes up so much of my time these days that i feel like it just sucks the inspiration out of me haha"
            #after the two conversation player can write to jen
            $ delete_replied("About Hobbies")
            $ jendo = Contact("feeling_jenerous", "jen_draft")

            
            n "I should write to Jen"
            n "go to the message tap and click draft new"

            pass
        "Ignore the message":
            pass


    return
#user1234 sleeping problem
#don't know what to write the school name and game name 
label lain_reply(current_message):
    menu:
        "Open the message":
            $ current_message.reply_label = None
            e_nvl "psst"
            e_nvl "Earth to Player..."
            e_nvl "Hey! Wake up!"
            e_nvl "Wake up! Wake up! Wake up! Wake up! Wake up! Wake up!" # continues to spam until user responds
            n_nvl "Do you have any idea what time it is?"
            e_nvl "Time to play a round of csgo! Wanna join?"
            n_nvl "Not really.."
            e_nvl "Whatever. Your loss."
            n_nvl "Tomorrow is a weekday. Don't you have school or work tomorrow?"
            e_nvl "School, yes."
            n_nvl "…Shouldn't you be sleeping?"
            e_nvl "That's where you're wrong. This is when the csgo servers are most active aka, the best time to get my rank up~"
            n_nvl "Shouldn't you be more concerned about getting your grades up?"
            nvl_narrator "user1234 fails to respond for a couple of minutes"
            n_nvl "…Hello?"
            e_nvl "Sorry, I was in the middle of a ranked match. You were saying?"
            n_nvl "Why would you beg to chat with me if you're clearly preoccupied?"
            e_nvl "Hey, no need to catch an attitude. After missing introductions yesterday, I was warned by a certain organizer of this project that I must fulfill a “quota” of activity on this app every day. So I'm doing just that, if you don't mind"
            n_nvl "Speaking of introductions, I haven't even gotten your name yet."
            e_nvl "Let's see… name's Lain, 15 years old, I go to fake high school, Leo rising…is there anything else I'm missing?"
            n_nvl "Are you sure you should be telling me your school?"
            e_nvl "No big deal. There's tons of people here. Can't be that easy, right?"
            n_nvl "I don't think that's safe but anyway… Why did you miss introductions yesterday?"
            e_nvl "They were at noon. Why would I be up at that hour?"
            n_nvl "That's a pretty normal hour to be awake…"
            e_nvl "Not for me. 12 pm is when I get my much-needed beauty sleep."
            n_nvl "Do you usually sleep through the day and game throughout the night?"
            e_nvl "Well, yes! Bedtime is at 7 am for me!"
            n_nvl "How do you wake up for school?"
            e_nvl "Easy. I don't."
            n_nvl "That can't be good for your grades."
            e_nvl "Yeah well."
            n_nvl "What will your parents think?"
            e_nvl "Looks like I just met my activity quota. Now if you'll excuse me, I have another match to get to."
            nvl_narrator "user1234 goes offline"
            $ delete_replied("Sleeping Problem")
            $ add_message("Family Situation", "user1234", "Hi", "lain_reply2")
            pass
        "Ignore the message":
            pass
    return


label lain_reply2(current_message):
    menu:
        "Open the message":
            $ current_message.reply_label = None
            e_nvl "You awake?"
            n_nvl "It's nice of you to ask this time."
            e_nvl "…"
            n_nvl "So, what game are you in the middle of playing now?"
            e_nvl "I'm not really in the mood for your sarcasm right now."
            n_nvl "Is something wrong?"
            e_nvl "Yes. Something terrible has happened."
            e_nvl "My mom confiscated my gaming pc."
            n_nvl "I'm sorry that happened to you. May I ask why?"
            e_nvl "She found out I've been skipping classes."
            n_nvl "That sucks. I'm surprised you got away with it for so long though."
            e_nvl "You'd be surprised how easy it is when your mom doesn't give a shit about her only child."
            n_nvl "That's an accusation."
            e_nvl "Well it's true. All she cares about is her stupid job. She's only punishing me to pretend she cares about my education."
            n_nvl "I'm sure it's all out of love."
            e_nvl "Yeah, right. A love to make my life miserable."
            n_nvl "Well look on the bright side. Without video games, you have the opportunity to fix your sleep schedule."
            e_nvl "Well I'm still up now, so it didn't really help much, did it?"
            e_nvl "Besides, it's not like videogames are the only reason I stay up late."
            e_nvl "The daytime is just suffocating."
            e_nvl "At night, I don't have to deal with my mom or with school or with responsibilities. Nighttime is just for me."
            n_nvl "It seems like the nighttime is just an escape from dealing with your issues."
            e_nvl "I mean, what is there to do during the daytime? What do YOU do?"
            n_nvl "Well for one, I go to school."
            e_nvl "Funny."
            n_nvl "But you could also use the daytime to talk to people about your issues rather than avoiding them. This lifestyle isn't healthy long-term."
            e_nvl "Thanks, mom."
            $ delete_replied("Family Situation")
            $ add_message("Lain Ending", "user1234", "Hi", "lain_end")
            pass
        "Ignore the message":
            pass
    return


#just the draft to write to jen about the branching endings 
#no ending yet
label jen_draft(contact, message_title="feeling_jenerous future decision"):
    menu:
        "Open the message":
            $ contact.draft_label = None
            j_nvl " i just don't know what i should do"
            menu (nvl = True):
                "Keep carrying on?":
                    n_nvl "Keep carrying on?"
                    j_nvl "hm"
                    j_nvl "i guess that is kind of my only option huh"
                    j_nvl "yeah i mean i've already made it this far"
                    j_nvl "it'd be a waste of everyone's time if i didn't finish it"
                    $ add_message("Jen Ending", "feeling_jenerous", "Hi", "jen_reply_end1")
                "You can switch programs to something you like, right?":
                    n_nvl "You can switch programs to something you like, right?"
                    j_nvl "i mean"
                    j_nvl "yeah i could"
                    j_nvl "i'm already this far in my program though, so i don't know if it'd be worth it to switch entirely"
                    j_nvl "but doing art… i like that idea"
                    j_nvl "i'll give it some thought"
                    $ add_message("Jen Ending", "feeling_jenerous", "Hi", "jen_reply_end2")
                "I don't know":
                    n_nvl "I don't know"
                    j_nvl "that's okay"
                    j_nvl "it's not really fair of me to decide for me"
                    j_nvl "i just… "
                    j_nvl "…"
                    j_nvl "i think i need a break"
                    #ending 3
                    n "feeling_jenerous “disappears”. All her social media accounts have been deactivated in the midst of a breakdown and no one can contact her."
                    n "The other characters talk about it and express their concern. They hope she isn't going to hurt herself but no one knows for sure."
        "Ignore the message":
            pass

    return


#jen ending1
label jen_reply_end1(current_message):
    menu:
        "Open the message":
            $ current_message.reply_label = None
            j_nvl "Hi"
            j_nvl " i think i'm gonna hold on for a little longer in my program"
            j_nvl "comp sci is reliable, even if the job market's looking a little dicey these days"
            j_nvl "worst case is that i just fall back on some other field"
            $ delete_replied("Jen Ending")
            pass
        "Ignore the message":
            pass
    return

#jen ending2
label jen_reply_end2(current_message):
    menu:
        "Open the message":
            $ current_message.reply_label = None
            j_nvl "hi"
            j_nvl " i think you're right"
            j_nvl " i should at least try doing something i like, like art"
            j_nvl "maybe i'll take a break year to try it"
            j_nvl "it's gonna be a weird conversation with my parents"
            j_nvl " but it's the first thing i'm looking forward to doing in a while"
            $ delete_replied("Jen Ending")
            pass
        "Ignore the message":
            pass
    return

#1234 ending 
label lain_end(current_message):
    menu:
        "Open the message":
            $ current_message.reply_label = None
            e_nvl "I see you're still online…"
            n_nvl "Likewise. I guess my advice didn't resonate with you."
            e_nvl "I wouldn't say that."
            e_nvl "Actually, I'm trying my best to heed your advice. But I'm feeling too restless to sleep."
            n_nvl "Have you gotten your gaming pc back?"
            e_nvl "No."
            n_nvl "Have you talked to your mom about your grievances at least?"
            e_nvl "Not yet."
            n_nvl "What's holding you back?"
            e_nvl "It's not that easy. Honestly, maybe you should just talk to her."
            $ delete_replied("Lain Ending")
#I think there still somethings going on with the ending
            pass
        "Ignore the message":
            pass 
            
    return