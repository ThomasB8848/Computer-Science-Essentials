import random

#Declaring Variables
answer = -1
user_guess = -1

#Welcome message
print("Welcome to the magic eight ball game.")
input("Ask a question to get a response from the magic eight ball.")

answer = random.randint(1,8)
print(answer)

if answer == 1:
    print("Yes, Most Definitely, your answer was", answer)
elif answer == 2:
    print("I think so, your answer was", answer)
elif answer == 3:
    print("Maybe, your answer was", answer)
elif answer == 4:
    print("Kinda, your answer was", answer)
elif answer == 5:
    print("Perhaps, your answer was", answer)
elif answer == 6:
    print("I dont think so, your answer was", answer)
elif answer == 7:
    print("Not quite, your answer was", answer)
elif answer == 8:
    print("ABSOLUTELY NOT!!, your answer was", answer)
else: 
    print("You have made an error")
      
