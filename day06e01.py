def test_cum():
    assert count_answers("share/d06-e01-test") == 11


def count_answers(test):
    input = open(test)
    answers = input.read().split("\n\n")
    counter = 0
    for a in answers:
        mylist = list(dict.fromkeys(list(a.replace('\n', ''))))
        counter += len(mylist)

    return counter




if __name__ == "__main__":
    test_cum()
    print(count_answers("share/d06-e01-input"))