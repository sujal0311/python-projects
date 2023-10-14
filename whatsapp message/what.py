import pywhatkit as py
while(True):
    print('''Welcome to the bot :
      Press 1 to send a whatsapp message to a individual
      Press 2 to send a whatsapp message to a group
      Press 3 to play a youtube video
      Press 4 to search on Google
      Press 5 to exit''')
    choice=int(input("Enter your choice : "))
    if(choice==1):
        phone=input("Enter receiver's phone number with country code : ")
        message=input("Enter your message you want to send : ")
        hour=int(input("Enter the hour:  "))
        min=int(input("Enter the minute : "))
        py.sendwhatmsg(phone,message,hour,min)
        
    elif(choice==2):
        group=input("Enter Whatsapp Group ID : ")
        message=input("Enter your message you want to send : ")
        hour=int(input("Enter the hour:  "))
        min=int(input("Enter the minute : "))
        py.sendwhatmsg_to_group(group,message,hour,min)
        
    elif(choice==3):
        url=input("Enter the youtube url or topic to search : ")
        py.playonyt(url)

    elif(choice==4):
        topic=input("Enter the topic to search on Google : ")
        py.search(topic)
    else:
        exit(5)