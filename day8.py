def convert(minutes):
    return minutes * 60

minutes = int(input("Enter minutes: "))
seconds = convert(minutes)
print("Seconds:", seconds)
