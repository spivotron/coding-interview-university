def unique_in_order(iterable):
    letters = {}
    uniqLetters = []
    for ele in enumerate(iterable):
        print(ele)

    # for x in range(len(iterable)):
    #     subList = iterable[:x]
    #     print(subList)
    #
    #
    #
    #
    # print(uniqLetters)


print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order([1,2,2,3,3]))