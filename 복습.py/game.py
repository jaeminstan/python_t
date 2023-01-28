import random

answer = str(random.randint(100, 999))

while True:
    guess = input("Enter a 3-digit number: ")
    
    if guess == answer:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        strike, ball = 0, 0
        for i in range(3):
            if guess[i] in answer:
                if guess[i] == answer[i]:
                    strike += 1
                else:
                    ball += 1
        print(f"{strike} strike(s), {ball} ball(s).")