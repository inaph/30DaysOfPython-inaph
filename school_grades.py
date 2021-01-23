score = int(input("Please enter your score to Check your grade: "))
if score > 100 or score < 0:
    print("Please enter a valid score")
elif  80 <= score <= 100:
    print("You have secured 'A- Grade'") 
elif 70 <= score <= 89:
    print("You have secured 'B- Grade'")
elif 60  <= score <= 69:
    print("You have secured 'C- Grade'")
elif 50 <= score <= 59:
    print("You have secured 'D- Grade'")
elif 0 <= score <= 49:
    print("You have secured 'F- Grade'")