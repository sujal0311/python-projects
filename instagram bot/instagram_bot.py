from instabot import Bot

user = input("Enter your instagram username or phone number or email: ")
password_ = input("Enter your password: ")
bot = Bot()
bot.login(username=user, password=password_)


while True:
    print("""0) To exit
1) For follow
2) For unfollow
3) For uploading a photo
4) For sending a message""")
    choice = int(input("Enter your choice: "))

    if choice == 0:
        break

    if choice == 1:
        follow_user = input("Enter the username to follow: ")
        bot.follow(follow_user)
    elif choice == 2:
        user_name=input("Enter the username to unfollow: ")
        bot.unfollow(user_name)
    elif choice == 3:
        path=input("Enter the path of the photo: ")
        cap=input("Enter the caption you want to add: ")
        bot.upload_photo(path,caption=cap)
    elif choice == 4:
        text=input("Enter the text: ")
        user_name=input("Enter the username to send the message: ")
        bot.send_message(text,[user_name])
    else:
        print("Invalid choice. Please try again.")
bot.logout()
print("Exiting. Goodbye!")
