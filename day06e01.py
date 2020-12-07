def test_sum():
    assert count_answers("share/d06e01-test") == 11


def count_answers(test):
    input = open(test)
    answers = input.read().split("\n\n")
    counter = 0
    for a in answers:
        mylist = list(dict.fromkeys(list(a.replace('\n', ''))))
        counter += len(mylist)

    return counter




if __name__ == "__main__":
    test_sum()
    print(count_answers("share/d06e01-input"))