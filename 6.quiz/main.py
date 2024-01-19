from questions import questions as q

# Initialize the score variable
score = 0

# Iterate through each question in the quiz
for key, value in q.quiz.items():
    # Print the question
    print(value["question"])
    
    # Take user input for the answer
    answer = input("> Answer? ")

    # Check if the answer is correct
    if answer.capitalize() == value["answer"]:
        print("Correct")
        score += 1
        print(f"Your score is: {score}")
        print("")
        print("")
    else:
        # Display the correct answer for incorrect responses
        print("Wrong!!")
        print(f"The correct answer is {value['answer']}")
        print(f"Your score is: {score}")
        print("")
        print("")

# Print the final score
print(f"You got {score} answers correct")
