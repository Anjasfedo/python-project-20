quiz = {
    "question1": {
        "question": "What is the capital of Indonesia?",
        "answer": "Jakarta"
    },
    "question2": {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    "question3": {
        "question": "What is the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What is the capital of Germany?",
        "answer": "Berlin"
    }
}

score = 0

for key, value in quiz.items():
    print(value["question"])
    answer = input("> Answer? ")

    if answer.capitalize() == value["answer"]:
        print("Correct")
        score += 1
        print(f"Your scores is: {score}")
        print("")
        print("")
    else:
        print("Wrong!!")
        print(f"The answer is {value["answer"]}")
        print(f"Your scores is: {score}")
        print("")
        print("")

print(f"You got {score} answer correct")
print