import random 

def generate_math_question(num1,num2):
    try:
        num1 = random.randint(num1,num2)
        num2 = random.randint(num1,num2)
    except:
        num1 = random.randint(num2,num1)
        num2 = random.randint(num2,num1)

    operators = ["+", "-", "*", "/"]
    operator = random.choice(operators)
    result = str(num1) + " " + operator + " " + str(num2)
    return result 




def check_answer(example, user_answer):
    try:
        correct_answers = eval(example)
        if correct_answers == float(user_answer):
            return True
        else:
            return False
    except ValueError:
        return False 



def math_quiz(number_of_questions=5):
    print("Добро пожаловать в математический тест!")
    correct_answers = 0

    for i in range(number_of_questions):
        question = generate_math_question(1, 10)

        print(question)

        user_answer = input()

        if check_answer(question, user_answer):
            correct_answers += 1

    print("Тест завершен.")



    print(f"Вы правильно решили {correct_answers} из {number_of_questions} вопросов.")



    if int((correct_answers * 100)/ number_of_questions) >= 80:
        print("Отлично! Вы получаете оценку A.")

    elif int((correct_answers * 100)/ number_of_questions) >= 60:
        print("Хорошо! Вы получаете оценку B.")

    else:
        print("Попробуйте еще раз. Вы получаете оценку C.")


math_quiz(7)