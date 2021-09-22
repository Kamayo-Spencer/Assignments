
"""Question 3: ALU Hangman
The program asks you 10 questions about ALU.

Every time you miss a question (you are hanging the man).

If you miss six questions (the man dies). 

And the game stops.

If you get all the questions right, your man lives, you get congratulated, and the game stops. 

If you finish all the questions with less than 6 mistakes, your man lives, and you are told the number of mistakes you made, and the game stops.

Questions to be asked:

When was ALU founded (2015)?
Who is the CEO of ALU (Fred Swaniker)?
Where are ALU campuses (Rwanda and Mauritius)?
How many campuses does ALU have (2)?
What is the name of ALU Rwanda’s Dean (Insert dean’s name)?
Who is in charge of Student Life (Sila Ogidi)?
What is the name of our Lab (Insert name here)?
How many students do we have in Year 2 CS(put the number of students)?
How many degrees does ALU offer (8)?
Where are the headquarters of ALU (Mauritius)?"""
import time
input("Welcome to ALU Hungman. Press enter to begin game..")
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
        if q8 == 96 :
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
            print("Sorry, you have failed the game.\nThe man ha died")
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