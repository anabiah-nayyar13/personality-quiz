print("               WELCOME TO PERSONALITY QUIZ")
print()
print("Answer the questions honestly!")
print("Choose: A, B, C, or D")
print()
# Scores
introvert = 0
extrovert = 0
logical = 0
emotional = 0
control = 0
strategic = 0

# Question 1
print("1. You feel most refreshed when:")
print("A. Alone for long time")
print("B. With close friend")
print("C. With many people")
print("D. Doing productive work alone")
answer = input("Enter your choice: ").upper()
if answer == "A":
    introvert +=2
    logical +=1
elif answer == "B":
    introvert +=1
    emotional +=1
elif answer == "C":
    extrovert +=2
elif answer == "D":
    control +=1
    logical +=1
print()

# Question 2
print("2. When making important decisions:")
print("A. I analyze facts deeply")
print("B. I follow my feelings")
print("C. I ask others first")
print("D. I go with flow")
answer = input("Enter your choice: ").upper()
if answer == "A":
    logical +=2
    control +=1
elif answer == "B":
    emotional +=2
elif answer == "C":
    emotional +=1
    extrovert +=1
elif answer == "D":
    introvert +=1
    control +=1
print()

# Question 3
print("3. In group situations you are:")
print("A. Silent observer")
print("B. Leader")
print("C. Entertainer")
print("D. Helper")
answer = input("Enter your choice: ").upper()
if answer == "A":
    introvert +=2
    logical +=1
elif answer == "B":
    extrovert +=2
    control +=1
elif answer == "C":
    emotional +=1
    extrovert +=2
elif answer == "D":
    emotional +=1
    strategic +=1
print()

# Question 4
print("4. If someone hurts you:")
print("A. I confront logically")
print("B. I feel deeply hurt")
print("C. I stay quiet but remember")
print("D. I cut off instantly")
answer = input("Enter your choice: ").upper()
if answer == "A":
    control +=1
    logical +=2
elif answer == "B":
    emotional +=2
elif answer == "C":
    strategic +=2
elif answer == "D":
    control +=1
    introvert +=1
print()

# Question 5
print("5. You prefer life to be:")
print("A. Planned and structured")
print("B. Free and flexible")
print("C. Successful and competitive")
print("D. Peaceful and emotional")
answer = input("Enter your choice: ").upper()
if answer == "A":
    control +=2
elif answer == "B":
    extrovert +=1
elif answer == "C":
    logical +=1
    control +=1
elif answer == "D":
    emotional +=2
print()

# Question 6
print("6. After social interaction:")
print("A. Energized")
print("B. Drained")
print("C. Neutral")
print("D. Depends on people")
answer = input("Enter your choice: ").upper()
if answer == "A":
    extrovert +=2
elif answer == "B":
    introvert +=2
elif answer == "C":
    logical +=1
elif answer == "D":
    strategic +=1
    emotional +=1
print()

# Question 7
print("7. You trust people:")
print("A. After observing logic")
print("B. Quickly if they feel right")
print("C. Rarely, very selective")
print("D. Based on experience")
answer = input("Enter your choice: ").upper()
if answer == "A":
    logical +=2
elif answer == "B":
    emotional +=2
elif answer == "C":
    strategic +=2
elif answer == "D":
    control +=1
    logical +=1
print()

# Question 8
print("8. You usually speak:")
print("A. Direct and blunt")
print("B. Emotionally expressive")
print("C. Funny and social")
print("D. Careful and selective")
answer = input("Enter your choice: ").upper()
if answer == "A":
    control +=1
    logical +=1
elif answer == "B":
    emotional +=2
elif answer == "C":
    extrovert +=2
elif answer == "D":
    strategic +=2
print()

# Question 9
print("9. You prefer:")
print("A. Safe life")
print("B. Risky exciting life")
print("C. Balanced risk")
print("D. Avoid risk")
answer = input("Enter your choice: ").upper()
if answer == "A":
    control +=2
elif answer == "B":
    emotional +=2
elif answer == "C":
    logical +=1
    control +=1
elif answer == "D":
    introvert +=1
    emotional +=1
print()

# Question 10
print("10. You are driven by:")
print("A. Success")
print("B. Love & emotions")
print("C. Freedom")
print("D. Power/control")
answer = input("Enter your choice: ").upper()
if answer == "A":
    control +=2
    logical +=1
elif answer == "B":
    emotional +=2
elif answer == "C":
    introvert +=1
    extrovert +=1
elif answer == "D":
    strategic +=2
print()


print("           QUIZ RESULT")

# Finding highest score
highest = max(introvert, extrovert, logical, emotional, control, strategic)

if highest == introvert:
    print("You have an INTROVERT!")
    print("You recharge by spending time alone or with a few close people. You are thoughtful, observant, and prefer deep conversations over constant social interaction.")
    
elif highest == extrovert:
    print("You are an EXTROVERT!")
    print("You gain energy from people, excitement, and social environments. You are expressive, outgoing, and enjoy being around others most of the time.")
    
elif highest == logical:
    print("You are a LOGICAL PERSON!")
    print("You make decisions using reason, analysis, and facts rather than emotions. You prefer clarity, practicality, and solving problems efficiently.")
    
elif highest == emotional:
    print("You are an EMOTIONAL PERSON!")
    print("You are deeply connected to feelings, empathy, and emotional experiences. You value emotional bonds and are sensitive to people's moods and actions.")

elif highest == control:
    print("You are a CONTROL-DRIVEN PERSON!")
    print("You like structure, planning, and knowing what's happening around you. You feel comfortable when things are organized and under control.")

elif highest == strategic:
    print("You are a STRATEGIC PERSON!")
    print("You observe people carefully and think before acting or speaking. You adapt to situations well and often focus on long-term outcomes rather than immediate emotions.")

print()

print("Your Scores:")
print("Introvert:", introvert)
print("Extrovert:", extrovert)
print("Logical:", logical)
print("Emotional:", emotional)
print("Control-driven:", control)
print("Strategic:", strategic)

print()
print("Thanks for playing!")