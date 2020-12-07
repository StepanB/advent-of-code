def test_sum():
    assert count_answers("share/d06e01-test") == 6


def count_answers(param):
    input = open(param)
    answers = input.read().split("\n\n")
    # print(answers)
    counter = 0
    for a in answers:
        mylist = a.split("\n")
        intersection = list(mylist[0])
        for a_list in mylist:
            intersection = list(set(intersection) & set(a_list))
        print(intersection)
        counter += len(intersection)


    # print(counter)

    return counter


if __name__ == "__main__":
    test_sum()
    print(count_answers("share/d06e01-input"))