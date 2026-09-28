
def run_maths_quiz():
    quiz = [
        {"question": "12*8=", "answer": "96", "correct_message": "correct", "wrong_message": "no the correct is 96"},
        {"question": "9*13=", "answer": "117", "correct_message": "correct", "wrong_message": "no the correct answer is 117"},
        {"question": "9*9=", "answer": "81", "correct_message": "Great job", "wrong_message": "Better luck! Next time."},
    ]

    score = 0

    for item in quiz:
        user_answer = input(item["question"] + " ")
        if user_answer.strip() == item["answer"]:
            print(item["correct_message"])
            score += 1
        else:
            print(item["wrong_message"])

    return score


if __name__ == "__main__":
    run_maths_quiz()
