def questions():
    input1 = str(input("Enter sentence:"))
    input2 = int(input("What is the shift:"))
    input3 = input("Are you encoding(y/n)")
    if input3 == "n":
        input2 = -input2
    inputs = [input1, input2, input3]
    return inputs


def coding(answers):
    alphBET = 'abcdefghijklmnopqrstuvwxyz'
    sentence = answers[0]
    shift = answers[1]
    coded_sentence = ''
    for x in range(len(sentence)):
        letter = sentence[x]
        if letter in alphBET:
            value = alphBET.index(letter)
            value_shifted = value + shift
            value_sized_shifted = value_shifted % 26
            new_letter = alphBET[value_sized_shifted]
            coded_sentence = coded_sentence + new_letter
        else:
            coded_sentence = coded_sentence + letter
    return coded_sentence


def main():
    answers = questions()
    if answers[2] == "y":
        print("Your encoded message is,", coding(answers))
    else:
        print("Your decoded message is,", coding(answers))


if __name__ == '__main__':
    main()
