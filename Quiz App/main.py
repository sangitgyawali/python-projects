questions = [
    {
        "question": "What is the capital of Nepal?",
        "options": ["A. Kathmandu", "B. Pokhara", "C. Butwal", "D. Biratnagar"],
        "answer": "A"
    },
    {
        "question": "Which language is used for Python programming?",
        "options": ["A. Java", "B. Python", "C. C++", "D. PHP"],
        "answer": "B"
    },
    {
        "question": "How many days are there in a leap year?",
        "options": ["A. 365", "B. 364", "C. 366", "D. 367"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. Dennis Ritchie", "B. James Gosling", "C. Guido van Rossum", "D. Elon Musk"],
        "answer": "C"
    }
]

score = 0

print("===== QUIZ APP =====")

for i, q in enumerate(questions, start=1):
    print(f"\nQuestion {i}: {q['question']}")

    for option in q["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").upper()

    if answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer is {q['answer']}.")

print("\n===== RESULT =====")
print(f"Your Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("Grade: A")
elif percentage >= 60:
    print("Grade: B")
elif percentage >= 40:
    print("Grade: C")
else:
    print("Grade: Fail")