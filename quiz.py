quiz=[
    {"question":"What is the name of the fictional Virginia town where the series the vampire diaries takes place?",
     "answer":"mystic falls"},
    {"question":"What is the name of the alternate dimension that exists parallel to the human world in stranger things?",
     "answer":"upside down"},
    {"question":"What small animal did the science teacher use for his initial virus experiments in the lab in series all of us are dead?",
     "answer":"hamster"},
    {"question":"What is the player number of the main protagonist in Squid Game?",
     "answer":"456"},
    {"question":"What is the alias of the criminal mastermind who plans the heist on the Royal Mint of Spain in the series money heist?",
     "answer":"professor"},
    {"question":"What is the name of the boarding school for outcasts that Wednesday is sent to in the series Wednesday?",
     "answer":"nevermore"},
]  

score = 0

for item in quiz:
    user_answer = input(item["question"] + " ")
    if user_answer.strip().lower() == item["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong. The answer was:", item["answer"])

print("You scored", score, "out of", len(quiz))



if score==len(quiz):
    print("Wow! Amazing job.I am impressed.Would you like to attend some Indian cricket related questions.")
    reply=input()
    if reply=="yes":
        quiz1=[
            {"Question":"Who captained India to victory in the 2011 ICC Men's Cricket World Cup?",
             "answer":"ms dhoni"},
             {"Question":"Which Indian player holds the record for the highest individual score in a One Day International (ODI) match (264 runs)?",
              "answer": "rohit sharma"},
              {"Question": "Who is famously nicknamed 'The Wall'?",
               "answer":"rahul dravid"},
        ]

        cricket_score = 0

        for item in quiz1:
              user_answer = input(item["Question"] + " ")
              if user_answer.strip().lower() == item["answer"].lower():
                print("Correct!")
                cricket_score += 1
              else:
                 print("Wrong. The answer was:", item["answer"])

        print("You scored", cricket_score, "out of", len(quiz1))


        if cricket_score==len(quiz1):
            print("You are a genius.We will make something better than this.")

        else:
            print("Better luck!Next time.")     

    else:
        print("No worries!")    

else:
    print("no worries you can get better in other things would you like to attend some simple maths question")
    reply=input()
    if reply=="yes":
        user_answer=input("12*8=")
        if user_answer=="96":
            print("correct")
        else:
            print("no the correct is 96")    
        user_answer = input("9*13=")
        if user_answer=="117":
                print("correct")
        else:
                print("no the correct answer is 117")   
        
            
        user_answer=input("9*9=")
        if user_answer=="81":
            print("Great job") 
        else:
                    print("Better luck! Next time.")    
            
    else:
        print("No worries!")

            