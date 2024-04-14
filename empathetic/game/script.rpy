#cannot click or press enter on the background, the message cannot continue if the user doesn't click the black background 




define e = Character("Eileen")

define j = Character("Jen")
# Main script for the demo!

define n = Character("You")

# NVL characters are used for the phone texting
define n_nvl = Character("You", kind=nvl)
define e_nvl = Character("user1234", kind=nvl)
define j_nvl = Character("feeling_jenerous", kind=nvl)
define g_nvl = Character("G.Chas", kind=nvl)

###python
init python:
    import nltk
    
    from nltk.sentiment import SentimentIntensityAnalyzer

    def vader(text):
        sia = SentimentIntensityAnalyzer()
        scores = sia.polarity_scores(text)
        compound_score = scores['compound']
        if compound_score > 0.05:
            sentiment = 'positive'
        elif compound_score < -0.05:
            sentiment = 'negative'
        else:
            sentiment = 'neutral'
        results = sentiment
        return results

# Let's assume you have a function to initialize contacts

# The game starts here.

label start:
    
    #set up the background 
    #scene room with dissolve
    $ mail = []
    $ mail_queue = []
    $ contacts = []     

    # create a contact the player can send messages to

    # to change the draft message, do something like $ fredo.draft = "fred_draft2"
    # $ fredo.delete() if you don't want him on the list anymore (sorry fred)
    
    show screen message_overlay
    

    #$ add_message("Test message", "saguaro", "sup")
    #$ add_message("Test2 message", "saguaro", "sup","sa_reply")
    
    ############################################
    #in case need to test the ai algo
    ############################################
    #$ user_input = renpy.call_screen("input", prompt="Say Something?", someText = "")
    #$ sentiment = vader(user_input)
        
    #if sentiment == 'positive':
    #    n "positive"
    #elif sentiment == '"negative':
    #    n "negative"
    #else:
    #    n "neutral"
        

    #n_nvl "[user_input]"
    
    
    #first scene of introduction
    nvl_narrator "Added feeling_jenerous to the group"
    nvl_narrator "Added G.Chas to the group"
    nvl_narratpr "Added user1234 to the group"
    n_nvl "{image=emoji/wave.png}"
    j_nvl "{image=emoji/wave.png}"
    e_nvl "{image=emoji/wave.png}"
    g_nvl "{image=emoji/wave.png}"
    j_nvl " hi, you can just call me jen"
    j_nvl " i didn't think they'd actually just randomly sort us like this"
    e_nvl " yeah that's odd"
    j_nvl " i guess we'll just see each other around"
    j_nvl "bye for now"


    $ add_message("About future", "feeling_jenerous", "Hi", "jen_reply")
    
    
    n "There's new messages in the message box"
    n "I should check them out"
    n "You can reply to the message by clicking the reply"
        
    #force the player to play the game    
    while check("About future") == False:
        n "I should check the message"
        n "You can reply to the message by clicking the reply"
                    
        
    
    nvl_narrator "The conversation ends"
        
    
    n "The end of the game"
    #show eileen happy

    # These display lines of dialogue.

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return


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
                $ add_message("Judgement", "G.Chas", "Hi", "gchas_reply")
                
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

#Grace judgement on the conversation
#are we going to make a different version scene for the previous conversation?
label gchas_reply(current_message):
    menu:
        "Open the message":
            $ current_message.reply_label = None
            g_nvl "Hello"
            n_nvl "Hi"
            g_nvl "Could I get your opinion on something?"
            n_nvl "Sure."
            g_nvl "I was in a conversation with the others earlier and something happened. Here:"

            # Simulating viewing a previous conversation
            nvl_narrator "You are viewing a previous conversation."

            e_nvl "Anyone on? I'm bored."
            e_nvl "And I have that quota thing to meet."
            j_nvl "i am."
            e_nvl "Anything interesting happen?"
            e_nvl "Without my gaming pc, I've been bored out of my mind."
            j_nvl "don't you have any hobbies?"
            e_nvl "Yeah but they're all on my pc."
            j_nvl "surely not all of them."
            e_nvl "Hey some people only have one hobby and that's bullying kids on Twitter."
            
            nvl_narrator "G.Chas is online"
            
            j_nvl "???"
            e_nvl "Not that I do that!"
            e_nvl "I'm not THAT toxic."
            e_nvl "I just do it in game chats during matches, that's all."
            g_nvl "Seems like I might've come in a bad time"
            g_nvl "But my two cents is that negativity you put out in the world will inevitably come back to you in some way."
            e_nvl "Well hi to you too."
            e_nvl "And it's fine, I can take whatever trash talk people say during matches."
            g_nvl "But what about outside of games? You might get a reputation for being unpleasant to talk with. It'd be harder to make friends with good people."
            e_nvl "Eh."
            e_nvl "It's whatever."
            g_nvl "I just think it's something you should keep in mind. I wouldn't want you to miss out on people you can be friends with."
            e_nvl "Yeah whatever."
            e_nvl "I'll think about it if you get off my case."
            e_nvl "You sure know how to nag."
            g_nvl "I'm sorry."
            e_nvl "It's fine."
            e_nvl "Anyway!"
            e_nvl "I'm still bored so."
            e_nvl "Tell me something fun."
            j_nvl "hmm a friend of mine is celebrating her anniversary with her s.o."
            e_nvl "Ew relationships but congrats to her."
            g_nvl "Congratulations! How long have they been together?"
            j_nvl "2 years! My friend met her girlfriend in our second year of uni. they were sharing a lot of classes and hit it off as friends. a year later, they started going out."
            e_nvl "Is getting gross what happens when you get older."
            e_nvl "Jk jk, sounds cute I guess."
            g_nvl "Did your friend date anyone before?"
            j_nvl "no, which is why we (me and our other friends) thought it was nice that her first partner is good to her."
            j_nvl "they disagree on small stuff like any pair of people do but generally they're very good together."
            g_nvl "I see. And what about the partner?"
            j_nvl "why are you asking? That's getting into personal territory i don't know if i'm cleared to share."
            g_nvl "Oh, I'm sorry. I guess I was just wondering if both of them had explored all their options first."
            e_nvl "What does that mean lol."
            g_nvl "There are a lot of wonderful people in our lives. Ignoring half of them just feels like a disservice."
            e_nvl "What."
            j_nvl "what?"
            e_nvl "Wait."
            e_nvl "Do you mean guys?"
            e_nvl "Because newsflash, they suck."
            e_nvl "I'm only 15 and even I already know that."
            g_nvl "There could be many opportunities you're missing."
            j_nvl "sorry, do you have a problem with female friend having a girlfriend?"
            g_nvl "It just feels weird to me that she's not giving men a chance."
            j_nvl "so you do."
            g_nvl "That's not what I was saying."
            e_nvl "Uhh yeah kinda was."
            j_nvl "look, it's not your place to judge my friend's relationship and it's definitely not your place to suggest that she's “missing opportunities” by dating a girl first. If i thought there was a problem with her partner as a person, i would've stepped in by now."
            j_nvl "i need a break."
            
            nvl_narrator "Feeling_jenerous is offline"
            
            e_nvl "Well"
            e_nvl "Uhh idk what to say so I'm gonna join some raids"
            e_nvl "Bye"
            
            nvl_narrator "user1234 is offline"
            
            g_nvl "Sorry."
            nvl_narrator "End of previous conversation."

            g_nvl "It's a lot to read. I apologize for that."
            g_nvl "It's just that the conversation hasn't been sitting well with me. I spoke my mind, just as I'd always been encouraged to. It's never been a problem before, so I don't know why it spiralled out of control like that."
            g_nvl "The other two both suggested that I said something wrong. You're an outside perspective on this conversation. Do you agree with them?"
            menu (nvl = True):
                "Yes.":
                    n_nvl "Yes."
                    g_nvl "I see. If three whole people think so, then I must be in the wrong somehow."
                "No.":
                    n_nvl "No."
                    g_nvl "Thank you, truly."
            g_nvl "Still, I'm a bit unnerved. You three aren't like anyone I've talked to before. It makes me wonder if it's just them that act like this or if I've just spent too much time around the same type of person in my life."
            g_nvl "Jen seemed like she flipped a dial. Lain… She was her usual self, I suppose."
            g_nvl "I think I'm just a little shocked. I didn't think I was appearing as judgemental, but that's what Jen seemed to think."
            g_nvl "I just feel uncomfortable with what she was saying. It's not right, at least according to my religion. God crafted us this way for a reason and not going along with His intentions feels like betraying the gift He gave us."            
            menu (nvl = True):
                "Not everyone follows the same god and not everyone follows a god in the first place.":           
                    n_nvl "Not everyone follows the same god and not everyone follows a god in the first place."
                    g_nvl "Really? But God is the only one. There isn't anyone else who can match His love for us."
                "I think you should do some research.":
                    n_nvl "I think you should do some research."
                    g_nvl "You have a point. I'll do that."
                "Even so, you kept pushing.":                           
                    n_nvl "Even so, you kept pushing."
                    g_nvl "Oh. I suppose I was 'nagging' again, like Lain said."
            g_nvl "Thank you for hearing me out. I think I should take some time to think about this. You have my deepest apologies for dragging you into this."
            
            $ delete_replied("Judgement")
            $ add_message("Horizon", "G.Chas", "Hi", "gchas_reply2")
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

label gchas_reply2(current_message):
    menu:
        "Open the message":
            $ current_message.reply_label = None
            g_nvl "Hello again. I wanted to continue off our last conversation."
            g_nvl "I'm so… confused. In the area where I live, we're all Christians and part of a community that I love. But after we talked last time, I decided to search for some information."
            g_nvl "The world beyond my home is so much more unfamiliar than I thought. I know that all people are children of God, but apparently not all people think that way?"
            g_nvl "And gay people are everywhere and in everything. It's like they're shoving it down our throats. I don't hate the people because I must love them as my fellow human, but… I saw people hating Christians just for existing. They called us all hateful, bigoted, and homophobic. I know that's not true. The kindest, most loving people I know could never say the things they were claiming we say."
            menu (nvl = True):
                "Hateful people, even if they're in the minority, will have the loudest voices.":
                    n_nvl "Hateful people, even if they're in the minority, will have the loudest voices."
                    g_nvl "Yeah… That's very true, isn't it? It's just that I know for a fact that it's not all Christians who act like that. I pray for people to find peace, because that is how they'll enter Heaven."
                "A lot of people were silenced and harassed by Christians for decades":                           
                    n_nvl "A lot of people were silenced and harassed by Christians for decades for being gay."
                    g_nvl "I understand keeping quiet about it, because otherwise it'd turn into a huge scandal, but why call it harassment when it isn't? We're just trying to guide people back to the right path." 
                    n_nvl "A lot of actions that don't seem like harassment from the person saying it might come off as harassment to the person hearing it."
                    n_nvl "If someone kept nitpicking you about the way you dress or your weight and they wouldn't stop even when you tell them to, would you call it harassment?"
                    n_nvl "You have a point."
                "Queer people finally have a time and place to be who they are without shame.":
                    n_nvl "Queer people finally have a time and place to be who they are without shame."
                    g_nvl "But it is shameful because they're being so blatant about it. It makes me feel uncomfortable, like I can't be myself."
                    n_nvl "That's exactly how they felt."
                    g_nvl "Really? I didn't realize it was like this."
                "Click this to enter your thought":
                    $ user_input = renpy.call_screen("input", prompt="Say Something?", someText = "")
                    $ senti = vader(user_input)
                    if senti == 'positive':
                        n_nvl "[user_input]"
                        g_nvl "But it is shameful because they're being so blatant about it. It makes me feel uncomfortable, like I can't be myself."
                        n_nvl "That's exactly how they felt."
                        g_nvl "Really? I didn't realize it was like this."
                    elif senti == 'negative':
                        n_nvl "[user_input]"                                        
                        g_nvl "I understand keeping quiet about it, because otherwise it'd turn into a huge scandal, but why call it harassment when it isn't? We're just trying to guide people back to the right path." 
                        n_nvl "A lot of actions that don't seem like harassment from the person saying it might come off as harassment to the person hearing it."
                        n_nvl "If someone kept nitpicking you about the way you dress or your weight and they wouldn't stop even when you tell them to, would you call it harassment?"
                        n_nvl "You have a point."
                    else:
                        n_nvl "[user_input]"
                        g_nvl "Yeah… That's very true, isn't it? It's just that I know for a fact that it's not all Christians who act like that. I pray for people to find peace, because that is how they'll enter Heaven."
                    
            g_nvl "It just feels like it goes against everything we're taught, even common sense to be kind. I can't understand why gay people and my fellow Christians would say things like that."

            $ delete_replied("Horizon")
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
                "Click this to enter your thought":
                    $ user_input1 = renpy.call_screen("input", prompt="Say Something?", someText = "")
                    $ senti1 = vader(user_input1)
        
                    if senti1 == 'positive':
                        n_nvl "[user_input1]"
                        n_nvl "You can switch programs to something you like, right?"
                        j_nvl "i mean"
                        j_nvl "yeah i could"
                        j_nvl "i'm already this far in my program though, so i don't know if it'd be worth it to switch entirely"
                        j_nvl "but doing art… i like that idea"
                        j_nvl "i'll give it some thought"
                        $ add_message("Jen Ending", "feeling_jenerous", "Hi", "jen_reply_end2")
                    elif senti1 == '"negative':
                        n_nvl "[user_input1]"
                        n_nvl "I don't know"
                        j_nvl "that's okay"
                        j_nvl "it's not really fair of me to decide for me"
                        j_nvl "i just… "
                        j_nvl "…"
                        j_nvl "i think i need a break"
                        #ending 3
                        n "feeling_jenerous “disappears”. All her social media accounts have been deactivated in the midst of a breakdown and no one can contact her."
                        n "The other characters talk about it and express their concern. They hope she isn't going to hurt herself but no one knows for sure."                            
                    else:
                        n_nvl "[user_input1]"
                        j_nvl "hm"
                        j_nvl "i guess that is kind of my only option huh"
                        j_nvl "yeah i mean i've already made it this far"
                        j_nvl "it'd be a waste of everyone's time if i didn't finish it"
                        $ add_message("Jen Ending", "feeling_jenerous", "Hi", "jen_reply_end1")
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
            menu (nvl = True):
                "convince her to attempt other, more helpful methods to cope with insomnia/addiction":
                    n_nvl "why not?"
                    e_nvl "can you lay off with the questions? It's getting annoying."
                    n_nvl "I'm sorry, I'm just trying to help."
                    e_nvl "Well stop. You have no idea what my mom is like."
                    n_nvl "You're right, I'm sorry."
                    e_nvl "Thank you. Now, back to the REAL issue at hand, how am I going to spend the entire night without gaming?"
                    n_nvl "You can start by logging off."
                    e_nvl "And then what?"
                    n_nvl "Uh, stare at the ceiling until you fall asleep?"
                    e_nvl "ha.ha.ha. what else u got"
                    n_nvl "Well personally, I'd read a book or something to pass the time by."
                    e_nvl "Personally, I'd rather stare at the ceiling until I fell asleep."
                    n_nvl "What do you have against a good book?"
                    e_nvl "for one, they're boring."
                    n_nvl "I mean, if you're going to be awake with no video games, you might as well make use of your time and do something worthwhile, right?"
                    e_nvl "i guess."
                    n_nvl "It's hard to force yourself to fall asleep if you're not tired. Reading helps destimulate my brain and quicken the process, though."
                    e_nvl "hm."
                    e_nvl "ugh. fine. I'll find smth to read if it means you won't nag me anymore."
                "Enable her gaming addiction and avoidant habits even more (if the player is more hostile)":
                    n_nvl "Stop putting it off, it'll only make it harder to talk to her."
                    e_nvl "Honestly, maybe you should just talk to her."
                    n_nvl "I don't think she'd take well to a stranger confronting her about her parenting…"
                    e_nvl "Right? So maybe you can lay off on the nagging."
                    n_nvl "Where did this hostility come from?"
                    e_nvl "Stop doing that."
                    n_nvl "Huh? I don't understand. I was just trying to help."
                    e_nvl "Well stop. You clearly don't understand anything about me or my life. People like you annoy me."
                    n_nvl "I'm sorry but you need to fix your attitude; this is probably why your mom doesn't love you."
                    e_nvl "And you need to fix your saviour complex. It's sooo fake."
                    n_nvl "You're never going to find the help you need if you keep pushing people away like this."
                    e_nvl "And who said I needed help? What's wrong with how I'm living?"
                    n_nvl "I mean, you're gaming till 7am every night which is unhealthy. Anyone can tell that you're unhappy with your circumstances."
                    e_nvl "God, this is why I hate talking to people like you and my mom, it just makes me more annoyed. Always trying to therapize me because I don't fall into YOUR standard of what happiness is. Has it ever occurred to you that this is my standard of happiness?"
                    n_nvl "Keep telling yourself that, see if it gets you your gaming pc back."
                    e_nvl "I can get my stuff back myself, thank you very much."
                    e_nvl "I regret ever telling you anything, bozo."
                    
                    nvl_narrator "user1234 signs off"
                    
                "Encourage her to confront her mom":
                    n_nvl "Why not?"
                    e_nvl "Can you lay off with the questions? It's getting annoying."
                    n_nvl "I'm sorry, I'm just trying to help."
                    e_nvl "Well stop. You have no idea what my mom is like."
                    n_nvl "I may not know what your mom is like, but I do know how it feels to have a chip on your shoulder when it comes to your parents."
                    e_nvl "Yeah right..."
                    
            $ delete_replied("Lain Ending")

            pass
        "Ignore the message":
            pass 
            
    return