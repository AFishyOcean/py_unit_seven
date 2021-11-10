def half_slice(word):
    x = len(word) // 2
    word2 = word[x:] + word[:x]
    return word2


def no_first_last(word):
    word = word.replace(word[0], '')
    word = word.replace(word[-1], '')
    return word

def longest(phrase):
    pass


def title_case(sentence):
    pass

def main():
    word = 'Something'
    print(half_slice(word))
    print(no_first_last(word))
    # print(longest(phrase))
    # print(title_case(sentence))

if __name__ == '__main__':
    main()