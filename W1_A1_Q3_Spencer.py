
''' The program asks you 10 questions about ALU.
If you miss six questions you have failed the game. 
And the game stops.
If you get all the questions right, you get congratulated and the game stops
;If you finish all the questions with less than 6 mistakes, you are shown your score, and you are told the number of mistakes you made, and the game stops.
When was ALU founded (2015)
Who is the CEO of ALU (Fred Swaniker)
Where are ALU campuses (Rwanda and Mauritius)
How many campuses does ALU have (2)
What is the name of ALU Rwandaâ€™s Dean (Gaidi Faraj)
Who is in Charge of Student Life (Sila Ogidi)
What is the name of our Lab (Nigeria)
How many students do we have in year 2 Cs (put the number of students)
How many degrees does ALU offer (8)
Where are the headquarters of ALU (Mauritius)
Handle user input well eg: Fred Swaniker , FRed Swaniker , fred swaniker and FRED SWANIKER are the right answer , meaning you ignore the case (upper or lower) while dealing with the strings here )
'''
import time
input("Welcome to ALU Trivia. Press enter to begin game..")
wrong =0
right =0

try:

    def questions():
        global wrong , right
    
        q1 = int(input("When was ALU founded? : "))
        if q1 == 2015:
            right += 1
            print(f"right1 = {right}")
        else :
            wrong += 1
            print(f"wrong = {wrong}")

        q2 = (input("Who is the CEO of ALU? : " )).casefold()
        if q2 == ("Fred Swaniker").casefold():
            right += 1
            print(f"right2 = {right}")
        else :
            wrong += 1

        q3 = (input("Where are ALU campases?? :")).casefold()   
        if q3 == ("Rwanda and Mauritius").casefold():
            right += 1
            print(f"right3 = {right}")
        else:   
            wrong += 1

        q4 = int(input("How many campuses does ALU have? : " ))
        if q4 == 2 :
            right += 1
            print(f"right4 = {right}")
        else:
            wrong += 1

        q5 = (input("What is the name of ALU Rwandaâ€™s Dean :")).casefold()
        if q5 == ("Gaidi Faraj").casefold()  :
            right += 1
            print(f"right5 = {right}")
        else:
            wrong += 1

        q6 = (input("Who is in Charge of Student Life : ")).casefold()
        if q6 == ("Sila Ogidi").casefold() :
            right += 1
            print(f"right6 = {right}")
        else:
            wrong += 1
            fail()
           
        q7 = (input("What is the name of our Lab : ")).casefold() 
        if q7 == ("Nigeria").casefold() :
            right += 1
            print(f"right7 = {right}")

        else:
            wrong += 1
            fail()   

        q8 = int(input("How many students do we have in year 2 Cs : "))
        if q8 == 200 :
            right += 1
            print(f"right8 = {right}")
        else:
            wrong += 1
            fail()
    
        q9 = int(input("How many degrees does ALU offer :"))
        if q9 == 8 :
            right += 1
            print(f"right9 = {right}")
        else:
            wrong += 1
            fail()

        q10 = (input("Where are the headquarters of ALU : ")).casefold()
        if q10 == ("Mauritius").casefold() :
            right += 1
            print(f"right10 = {right}")
            finish()
        else:
            wrong += 1
            fail()    
            finish()
    def fail():
        if wrong == 6 :
            print("Sorry, you have failed the game.")
            exit()
        
        else:
            pass

    def finish():        
        if right == 10:
            print("Calculating your score...")
            time.sleep(2)
            print("You have completed the game successfully.")
            print(f"Your score is : {right}")
            exit()             
        else:
            print(f"Congratulations, you have finished the game with a score of {right}")
            exit()
    

except ValueError:
    print("Please put in the correct values.")
    print("Remember to follow instructions next time.")
    questions()

questions()