import phonenumbers
from phonenumbers import geocoder,timezone,carrier
number=input("Enter your mobile number with country code : ")
phone=phonenumbers.parse(number)
time=timezone.time_zones_for_number(phone)
car=carrier.name_for_number(phone,"en")
reg=geocoder.description_for_number(phone,"en")
print("The details are :\n",phone,"is :")
print("Timezone :",time)
print("Company name:",car)
print("Country :",reg)