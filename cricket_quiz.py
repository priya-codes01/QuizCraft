
def run_cricket_quiz():
    quiz1 = [
        {"Question": "Who captained India to victory in the 2011 ICC Men's Cricket World Cup?",
         "answer": "ms dhoni"},
        {"Question": "Which Indian player holds the record for the highest individual score in a One Day International (ODI) match (264 runs)?",
         "answer": "rohit sharma"},
        {"Question": "Who is famously nicknamed 'The Wall'?",
         "answer": "rahul dravid"},
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

    if cricket_score == len(quiz1):
        print("You are a genius.We will make something better than this.")
    else:
        print("Better luck!Next time.")

    return cricket_score


if __name__ == "__main__":
    run_cricket_quiz()
