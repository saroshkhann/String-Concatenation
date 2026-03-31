print("Welcome to the Quiz Game!")
print("-------------------------")

questions = [{
    "question": "What is the capaital of France",
    "a": "Paris",
    "b": "London",
    "c": "Rome",
    "d": "Berlin",
    "correct": "a"
},{
    "question": "Which planet is knwon as Red Planet?",
    "a": "Earth",
    "b": "Mars",
    "c": "Jupiter",
    "d": "Venus",
    "correct": "b"
},{
    "question": "Who wrote 'Hamlet'?",
    "a": "Charles Dickens",
    "b": "William Shakespeare",
    "c": "Mark Twain",
    "d": "Jane Austen",
    "correct": "b"
}]


is_on = True

score = 0
counter = 1
for question in questions:
    print(f"Question {counter}: {question['question']}")
    print(f"A. {question['a']}")
    print(f"B. {question['b']}")
    print(f"C. {question['c']}")
    print(f"D. {question['d']}")
    counter+=1

    answer = input("Enter your answer").lower()
    if answer == question['correct']:
        print("Correct! ✅")
        score+=1
        print("\n")
    else:
        print(f"Wrong! ❌ The correct answer is {question['correct']}")

print("-------------------------")
print("Quiz Completed!")
print(f"Your final score: {score} / {len(questions)}")
print("Good job! 👍")