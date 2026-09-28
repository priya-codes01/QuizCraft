
def run_tv_quiz():
    quiz = [
        {"question": "What is the name of the fictional Virginia town where the series the vampire diaries takes place?",
         "answer": "mystic falls"},
        {"question": "What is the name of the alternate dimension that exists parallel to the human world in stranger things?",
         "answer": "upside down"},
        {"question": "What small animal did the science teacher use for his initial virus experiments in the lab in series all of us are dead?",
         "answer": "hamster"},
        {"question": "What is the player number of the main protagonist in Squid Game?",
         "answer": "456"},
        {"question": "What is the alias of the criminal mastermind who plans the heist on the Royal Mint of Spain in the series money heist?",
         "answer": "professor"},
        {"question": "What is the name of the boarding school for outcasts that Wednesday is sent to in the series Wednesday?",
         "answer": "nevermore"},
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

    if score == len(quiz):
        print("Wow! Amazing job.I am impressed.Would you like to attend some Indian cricket related questions.")
        reply = input().strip().lower()
        if reply == "yes":
            from cricket_quiz import run_cricket_quiz
            run_cricket_quiz()
        else:
            print("No worries!")
    else:
        print("no worries you can get better in other things would you like to attend some simple maths question")
        reply = input().strip().lower()
        if reply == "yes":
            from maths_quiz import run_maths_quiz
            run_maths_quiz()
        else:
            print("No worries!")

    return score


if __name__ == "__main__":
    run_tv_quiz()
