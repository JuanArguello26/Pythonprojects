print("Access verification")

age_user=int(input("Enter your age: "))

if age_user<18 and age_user>0 :  #AND= Y
    print("You are not allowed to do that")

elif age_user<=0 or age_user>=100: # OR= O
    print("Please insert a valid age")
else :
    print("You are allowed to do that")

print("Access verification")

#we can concatenate a conditional using and / or

note=int(input("Enter your note: "))

if note<5:
    print("Your note is too low")
elif note>5 and note<=10:
    print("Your note is good enough")
else:
    print("Your note is too high")

print("Have a good day.")
