import smtplib as smt

ob = smt.SMTP('smtp.gmail.com', 587)
ob.ehlo()
ob.starttls()

gmail = input("Enter your gmail: ")
password = input("Enter your password: ")
password=""   
'''create and add app passsword here to access the gmail acccout'''
ob.login(gmail, password)

subject = input("Enter the subject of your mail: ")
body = input("Enter the body of your mail: ")
message = "Subject:{}\n\n{}".format(subject, body)

add = []
users_count = int(input("Enter the number of users: "))

for i in range(users_count):
    usergmail = input("Enter the recipient gmail id: ")
    add.append(usergmail)

to_addrs = ', '.join(add)

ob.sendmail(gmail, add, message)
print("Email successfully sent")
ob.quit()
