# Here's the code for the phone!

define nvl_mode = "phone"  ##Allow the NVL mode to become a phone conversation
define MC_Name = "You" ##The name of the main character, used to place them on the screen
define C1_Name = "user1234"
define C2_Name = "feeling_jenerous"

init -1 python:
    phone_position_x = 0.5
    
    phone_position_y = 0.5

    def print_bonjour():
        print("bonjour")


transform phone_transform(pXalign=0.5, pYalign=0.5):
    xcenter pXalign
    yalign pYalign

transform phone_appear(pXalign=0.5, pYalign=0.5): #Used only when the dialogue have one element
    xcenter pXalign
    yalign pYalign

    on show:
        yoffset 1080
        easein_back 1.0 yoffset 0

    
transform message_appear(pDirection):
    alpha 0.0
    xoffset 50 * pDirection
    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 xoffset 0

transform message_appear_icon():
    zoom 1.0

    

transform message_narrator:
    alpha 0.0
    yoffset -50

    parallel:
        ease 0.5 alpha 1.0
    parallel:
        easein_back 0.5 yoffset 0
        
screen input(prompt, someText = ""):
    frame:
        xalign 0.5
        yalign 1.0
        padding (20,20)
        xysize (1000,120)
        has vbox
        
        text prompt style "input_prompt"
        input id "input" style "input_text" default someText
        
        
        
screen PhoneDialogue(dialogue, items=None):

    style_prefix "phoneFrame"
    frame at phone_transform(phone_position_x, phone_position_y):
        if len(dialogue) == 1:
            at phone_appear(phone_position_x, phone_position_y)
        viewport:
            draggable True
            mousewheel True
            # cols 1
            yinitial 1.0
            # scrollbars "vertical"
            vbox:
                null height 20
                use nvl_phonetext(dialogue)
                null height 100
        
        if len(items)==0: #If we don't have a menu
            button:
                padding (0,0)
                action RollForward()
                xysize (10,120)
                align(0.5,0.8)
                text "Next" style "nvl_button"
                
        else:
            # Phone Menu Choice
            frame:
                background Solid("#424242")
                foreground None
                align(0.5,1.0)
                xysize (1300,120)
                vbox:
                    yalign 0.5
                    for i in items: #For each choices...
                        button:
                            action i.action
                            xalign 0.5
                            frame:
                                background Solid("#424242")
                                foreground None
                                xysize (500,30)

                                text i.caption:
                                    align (0.5,0.5)
                                    text_align 0.5
                                    size 30
                                # style "nvl_button"

screen nvl_phonetext(dialogue):
    style_prefix None

    $ previous_d_who = None
    for id_d, d in enumerate(dialogue):
        if d.who == None: # Narrator
            text d.what:

                    italic True
                    size 28
                    slow_cps False
                    id d.what_id
                    if d.current:
                        at message_narrator
        else:
            if d.who == MC_Name:
                $ message_frame = "phone_send_frame.png"
            else:
                $ message_frame = "phone_received_frame.png"

            hbox:
                spacing 10
                
                #If this is the first message of the character, show an icon
                if previous_d_who != d.who:
                    if d.who == MC_Name:
                        $ message_icon = "player.png"
                    elif d.who == C1_Name:
                        $ message_icon = "C1.png"
                    elif d.who == C2_Name:
                        $ message_icon = "C2.png"
                    else:
                        $ message_icon = "phone_received_icon.png"

                    add message_icon:
                        if d.current:
                            at message_appear_icon()
                        
                else:
                    null width 107

                vbox:
                    yalign 1.0
                    if d.who != MC_Name and previous_d_who != d.who:
                        text d.who

                    frame:
                        padding (20,20)
                        

                        background Frame(message_frame, 23,23,23,23)
                        xsize 450

                        if d.current:
                                at message_appear(-1)

                        text d.what:
                            pos (0,0)

                            slow_cps False
                            

                            if d.who == MC_Name :
                                color "#FFF"
                            else:
                                color "#000"

                                
                            id d.what_id
        $ previous_d_who = d.who
                    
style phoneFrame is default

style phoneFrame_frame:
    background Frame("background.png", xcenter=0.5,yalign=0.5)
    foreground Frame("foreground.png", xcenter=0.5,yalign=0.5)
    
    ysize 815
    xsize 1300

style phoneFrame_viewport:
    yfill True
    xfill True

    yoffset -20

style phoneFrame_vbox:
    spacing 10
    xfill True

            
#######################
##Chat Room
## try to separate the conversation into a chat room but it cannot have the same reaction as the nvl kind 
## maybe it need to fix the screen phone dialogue to display the chat room?
## this is still in the experiment step so I will not implement it now at the script
#######################

init python:
    class Message:
        def __init__(self, sender, text):
            self.sender = sender
            self.text = text

    class ChatRoom:
        def __init__(self, name, participants):
            self.name = name
            self.participants = participants
            self.messages = []

        def add_message(self, sender, text):
            self.messages.append(Message(sender, text))

    # Dictionary to hold chat rooms
    chat_rooms = {
        "Friends": ChatRoom("Friends", [MC_Name, C1_Name, C2_Name]),
        "Jen": ChatRoom("Jen", [MC_Name, C2_Name])
    }
    
    # Function to send a message to a chat room
    def send_message_to_chat_room(room_name, sender, text):
        if room_name in chat_rooms:
            chat_rooms[room_name].add_message(sender, text)
            


screen chat_room_selection:
    style_prefix None
    frame at phone_transform(phone_position_x, phone_position_y):
        vbox:
            text "Select a Chat Room:" align (0.5, 0.0)  # Title
            for room_name, room in chat_rooms.items():
                textbutton room_name action [Show("chat_room_messages", room=room)]
            # Optionally, add a button to exit the chat room selection
            textbutton "Exit" action Return() align (1.0, 1.0)


screen chat_room_messages(room):
    style_prefix "phoneFrame"
    frame at phone_transform(phone_position_x, phone_position_y):
        vbox:
            text "Chat Room: ".format(room.name) align (0.5, 0.0)  # Chat room title
            for msg in room.messages:
                hbox:
                    # Display an icon next to the message if desired
                    if msg.sender == MC_Name:
                        add "player.png" at message_appear_icon()
                    elif msg.sender == C1_Name:
                        add "C1.png" at message_appear_icon()
                    elif msg.sender == C2_Name:
                        add "C2.png" at message_appear_icon()
                    else:
                        add "phone_received_icon.png" at message_appear_icon()
                    # Display the message text
                    
                    if msg.sender == MC_Name:
                         $ message_frame = "phone_send_frame.png"
                    else:
                        $ message_frame = "phone_received_frame.png"
                    vbox:
                        if msg.sender != MC_Name:
                            text msg.sender
                        frame:
                            yalign 1.0
                            padding (20,20)
                            xsize 800
                            ysize 100
                            background Frame(message_frame, 23,23,23,23)
                            text msg.text:
                                pos (0,0)
                                slow_cps False
                                if msg.sender == MC_Name :
                                    color "#FFF"
                                else:
                                    color "#000"
                                    
            # Add a button to go back to the chat room selection or exit
            textbutton "Back" action Return() align (1.0, 1.0)
            null height 20  # Some spacing at the bottom


        

        
#######################
##Basic Message System 
## inspired by the message system from the Ren'Py resources 
# maybe we can use it as the base for the phone message system
# it can be done to write the story but the ui is not that good
#######################

init python:
    import renpy.store as store
    
    reply_screen = False
    draft_screen = False

    class Mail(store.object):
        def __init__(self, subject, sender, body, reply_label=False, delay=False, view=True, read=False, replied = False):
            self.subject = subject
            self.sender = sender
            self.body = body
            self.reply_label = reply_label
            self.delay = delay
            self.view = view
            self.read = read
            self.replied = replied 
            if delay:
                self.queued()
            else:            
                self.deliver()  
                
        def mark_reply(self):
            self.replied = True
            renpy.restart_interaction()
                
        def delete(self):
            self.view = False
            renpy.restart_interaction()
            
        def deliver(self):
            if self in mail_queue:
                mail_queue.remove(self)
            mail.insert(0, self)
            
        def mark_read(self):
            self.read = True 
            renpy.restart_interaction()         
            
        def queued(self):
            mail_queue.append(self)        
            
        def reply(self):
            global reply_screen
            reply_screen = True
            renpy.call_in_new_context(self.reply_label, current_message=self)
            self.replied = True                
            reply_screen = False  
            if self in mail_queue:
                mail_queue.remove(self)   
                     
      

    class Contact(store.object):
        def __init__(self, name, draft_label):
            self.name = name
            self.draft_label = draft_label  
            self.add_contact()
            
        def add_contact(self):
            contacts.append(self)

        def draft(self):
            global draft_screen
            draft_screen = True
            renpy.call_in_new_context(self.draft_label, contact=self)            
            draft_screen = False
            
        def delete(self):
            contacts.remove(self)
            


    def add_message(subject, sender, body, reply_label=False, delay=False):
        message = Mail(subject, sender, body, reply_label, delay)
        
    def check(subject):
        for item in mail:
            if item.subject == subject:
                if item.read:
                    return True
                else:
                    return False
                    
    def deliver_all(): 
        mail.extend(mail_queue)
        mail_queue = list()          
        
    def deliver_next():
        if mail_queue:
            mail_queue[0].deliver()

    def mark_all_read():
        unread_messages = [x for x in mail if not x.read]
        for x in unread_messages:
            x.mark_read()                

    def message_count():
        visible_messages = [x for x in mail if x.view]
        return len(visible_messages)
        
    def new_message_count():
        unread_messages = [ x for x in mail if not x.read]
        return len(unread_messages)
    
    def delete_replied(subject):
        for item in mail:
            if item.subject == subject:
                    mail.remove(item)
    
    

screen message_overlay:
    hbox:
        xalign 0.5 yalign 0.0 
        if new_message_count() > 0:
            textbutton "Message (%d New)" % (new_message_count()) action Show("message")
        else:
            textbutton "Message" action Show("message")

screen message:
    tag menu
    modal True
    default current_message = None
    $ available_drafts = [i for i in contacts if i.draft_label]    
    frame:
        style_group "message"
        vbox:
            label "Inbox"
            if new_message_count() > 0:
                text ("Messages: %d (%d unread)") % (message_count(), new_message_count())
            else:
                text ("Messages: %d") % message_count()
            side "c r":
                area (0,0,800,300)
                viewport id "message_list":
                    draggable True mousewheel True
                    vbox:
                        for i in mail:
                            if i.view:
                                hbox:  # Use an hbox to place image and text side by side
                                    if not i.read:
                                        # Determine which icon to show
                                        if i.sender == C1_Name:
                                            $ icon_path = "C1.png"
                                        elif i.sender == C2_Name:
                                            $ icon_path = "C2.png"
                                        else:
                                            $ icon_path = "phone_received_icon.png"

                                        # Show the icon
                                        text ("New") color "#FF0000"
                                        imagebutton idle icon_path action [SetScreenVariable("current_message",i), i.mark_read]
                                        textbutton i.sender action [SetScreenVariable("current_message",i), i.mark_read] xfill True
                                    else:
                                        # Determine which icon to show
                                        if i.sender == C1_Name:
                                            $ icon_path = "C1.png"
                                        elif i.sender == C2_Name:
                                            $ icon_path = "C2.png"
                                        else:
                                            $ icon_path = "phone_received_icon.png"

                                        # Show the icon
                                        imagebutton idle icon_path action SetScreenVariable("current_message",i)  
                                        textbutton i.sender action SetScreenVariable("current_message",i) xfill True

                                    
                vbar value YScrollValue("message_list")
            hbox:
                null height 20
            side "c r":
                area (0,0,800,300)
                viewport id "view_message":
                    draggable True mousewheel True
                    vbox:
                        if current_message:
                            if current_message.sender == MC_Name:
                                text ("This is a group message")
                            else:
                                text ("This is a private message from " + current_message.sender)
                                
                vbar value YScrollValue("view_message")
            use message_commands

screen message_commands:
    hbox:
        if available_drafts:
            textbutton "Draft New" action Show("contacts")
        else:
            textbutton "Draft New" action None
        if current_message and current_message.reply_label:
            textbutton "Reply" action current_message.reply
        else:
            textbutton "Reply" action None
        if current_message:
            textbutton "Delete" action [current_message.delete, SetScreenVariable("current_message", None)]
        else:
            textbutton "Delete" action None
        if new_message_count() > 0:
            textbutton "Mark All Read" action mark_all_read
        else:
            textbutton "Mark All Read" action None
        
        textbutton "Exit" action Hide("message")
        
screen contacts:
    modal True
    frame:
        style_group "message"
        xsize 500
        vbox:
            label "Contacts"
            for name in contacts:
                if name.draft_label:
                    textbutton name.name action [name.draft, Hide("contacts")]
                else:
                    textbutton name.name action None
            textbutton "Close" action Hide("contacts")

init -2 python:
    style.message = Style(style.default)
    style.message_vbox.xalign = 0.5
    style.message_vbox.xfill = True
    style.message_hbox.xalign = 0.5
    style.message_label_text.size = 30
    style.message_label_text.xalign = 0.5
    style.message_label.xfill = True
    style.message_frame.xalign = 0.5
    style.message_frame.yalign = 0.5
    
# updated choice screen    
screen choice:

    if reply_screen or draft_screen:
        # this is the menu for message replies and drafts
        frame:
            style_group "message"

            vbox:
                label "Draft"

                for caption, action, chosen in items:

                    if action:
                        button:
                            action action
                            style "menu_choice_button" xalign 0.5

                            text caption text_align 0.5

                    else:
                        text caption style "menu_caption"
                        
    else:
        # this is the default choice menu
        window:
            style "menu_window"
            xalign 0.5
            yalign 0.5

            vbox:
                style "menu"
                spacing 2

                for caption, action, chosen in items:

                    if action:

                        button:
                            action action
                            style "menu_choice_button"

                            text caption style "menu_choice"

                    else:
                        text caption style "menu_caption"    