def run_quiz_advanced():
    question = "Столиця Іспанії:"
    answers = ["Рим", "Мадрид", "Барселона", "Лісабон"]
    correct_answer = 2

    print("Виберіть одну правильну відповідь")
    print(question)

    for i, answer in enumerate(answers, 1):
        print(f"{i}. {answer}")

    while True:
        user_input = input("Введіть номер відповіді: ")

        if user_input.isdigit():
            answer_num = int(user_input)
            if 1 <= answer_num <= 4:
                if answer_num == correct_answer:
                    print("✅ Правильно! Мадрид - столиця Іспанії.")
                else:
                    print(f"❌ Неправильно. Правильна відповідь: {answers[correct_answer - 1]}.")
                break

run_quiz_advanced()