def questions():
    input1 = str(input("Enter sentence:"))
    input2 = int(input("What is the shift:"))
    input2 = input2 % 25
    input3 = input("Are you encoding(y/n)")
    if input3 == "n":
        input2 = -input2
    inputs = [input1, input2]
    return inputs

def coding():
    pass


def main():
    answers = questions()
    x = answers[0]
    y = answers[1]
    print(x)
    print(y)

if __name__ == '__main__':
    main()