limit = int(input())
play = int(input())

if limit >= play:
    print("Congratulations, you are within the speed limit!")
elif (play-limit) <= 20:
    print("You are speeding and your fine is $100.")
elif ((play-limit) >= 21 ) and ((play-limit) <= 30 ):
    print("You are speeding and your fine is $270.")
elif ((play-limit) >= 31 ):
    print("You are speeding and your fine is $500.")