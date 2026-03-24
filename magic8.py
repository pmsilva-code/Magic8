import random


def answer_generator():

    name = "David"
    questions = ""
    answer = ""

    random_number = random.randint(1, 15)

    if name == "":
        answer = "Outlook not so good"
        print(f"asks: Will I win the lottery?")
        print(f"Magic 8-Ball's answer: {answer}")

    elif questions == "":
        answer = "Magic 8-Ball cannot provide a fortune, ask a question."
        print(f"Magic 8-Ball's answer: {answer}")

    elif random_number == 1:
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
    elif random_number == 10:
        answer = "As I see it, yes."
        print(f"{name} asks: {questions}")
        print(f"Magic 8-Ball's answer: {answer}")
    elif random_number == 11:
        answer = "You may rely on it."
        print(f"{name} asks: {questions}")
        print(f"Magic 8-Ball's answer: {answer}")
    elif random_number == 12:
        answer = "Concentrate and ask again."
        print(f"{name} asks: {questions}")
        print(f"Magic 8-Ball's answer: {answer}")
    elif random_number == 13:
        answer = "It is certain."
        print(f"{name} asks: {questions}")
        print(f"Magic 8-Ball's answer: {answer}")
    elif random_number == 14:
        answer = "It is decidedly so."
        print(f"{name} asks: {questions}")
        print(f"Magic 8-Ball's answer: {answer}")
    elif random_number == 15:
        answer = "Signs point to yes."
        print(f"{name} asks: {questions}")
        print(f"Magic 8-Ball's answer: {answer}")
    else:
        print(f"{name} asks: {questions}")
        print(f"Magic 8-Ball's answer: {answer}")


answer_generator()
