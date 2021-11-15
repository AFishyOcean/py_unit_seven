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
    coded_sentence = ' '
    for x in range(len(alphBET)):
        letter = sentence[x]
        if letter in alphBET:
            value = alphBET.index(letter)
            value_shifted = value + shift
            valueSIZEDshifted = value_shifted % 26
            new_letter = alphBET[valueSIZEDshifted]
        coded_sentence = coded_sentence + new_letter
    return coded_sentence

def main():
    answers = questions()
    if answers[2] == "y":
        print("Your encoded message is,", coding(answers))
    else:
        print("Your decoded message is,", coding(answers))


if __name__ == '__main__':
    main()