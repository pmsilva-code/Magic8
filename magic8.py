import random


def answer_generator():

    name = "David"
    questions = "David go to the store today?"
    answer = ""

    random_number = random.randint(1, 9)

    if random_number == 1:
        answer = "Yes - definitely."
        print(f"{name} asks: {questions}")
        print(f"Magic 8-Ball's answer: {answer}")
    elif random_number == 2:
        answer = "It is decidedly so."
        print(f"{name} asks: {questions}")
        print(f"Magic 8-Ball's answer: {answer}")
    elif random_number == 3:
        answer = "Without a doubt."
        print(f"{name} asks: {questions}")
        print(f"Magic 8-Ball's answer: {answer}")
    elif random_number == 4:
        answer = "Reply hazy, try again."
        print(f"{name} asks: {questions}")
        print(f"Magic 8-Ball's answer: {answer}")
    elif random_number == 5:
        answer = "Ask again later."
        print(f"{name} asks: {questions}")
        print(f"Magic 8-Ball's answer: {answer}")
    elif random_number == 6:
        answer = "Better not tell you now."
        print(f"{name} asks: {questions}")
        print(f"Magic 8-Ball's answer: {answer}")
    elif random_number == 7:
        answer = "My sources say no."
        print(f"{name} asks: {questions}")
        print(f"Magic 8-Ball's answer: {answer}")
    elif random_number == 8:
        answer = "Outlook not so good."
        print(f"{name} asks: {questions}")
        print(f"Magic 8-Ball's answer: {answer}")
    elif random_number == 9:
        answer = "Very doubtful."
        print(f"{name} asks: {questions}")
        print(f"Magic 8-Ball's answer: {answer}")
    else:
        answer = "Error"
        print(f"Magic 8-Ball's answer: {answer}")


answer_generator()
