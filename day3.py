#Create a program that calculates a student's letter grade based on their score.

score = int(input("Enter the student's score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
elif score >= 0:
    print("Grade: F")
else:
    print("Invalid score")
