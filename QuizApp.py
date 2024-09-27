questions = [
    {
        "prompt" : "What is the capital of India?",
        "options" : ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Guwahati"],
        "answer" : "B"
    },
    {
        "prompt" : "Which language is primarily spoken in india?",
        "options" : ["A. Hindi", "B. Marathi", "C. Assamese", "D. Tamil"],
        "answer" : "A"
    },
    {
        "prompt" : "What is the smallest prime number?",
        "options" : ["A. 1", "B. 2", "C. 0", "D. 5"],
        "answer" : "B"
    },
    {
        "prompt" : "Who wrote 'The Formation'",
        "options" : ["A. Carl Segan", "B. Albert Einstein", "C. Stephen Howkins", "D. Manjeet Barman"],
        "answer" : "D"
    }
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answers (A, B, C, D): ")
        if answer == question["answer"]:
            print("Horray!!, Your answer is Correct\n")
            score += 2
        else:
            print("Oops!!, Your answer is not correct, The correct answer was", question["answer"], "\n")

    print("Yeh!!, You are completing the quiz")
    print("You got", score, "out of", 2*(len(questions)),)


run_quiz(questions)