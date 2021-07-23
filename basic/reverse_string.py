def str_to_list(payload) -> []:
    return [i.lower() for i in payload if i.isalnum()]


def reverse_string(ls: []) -> []:
    #print(type(ls))
    #print(type(ls[::-1]))
    return ls[::-1]


def list_to_str(ls) -> str:
    return "".join([i for i in ls])


def total(payload) -> str:
    return "".join([i for i in [i.lower() for i in payload if i.isalnum()][::-1]])


if __name__ == '__main__':
    '''
    ls = str_to_list(['a', 'apple', 'is', 'good'])
    reversed_ls = reverse_string(ls)
    print(list_to_str(reversed_ls))
    print(total(input("total?")))
    '''
    print(reverse_string('a apple is good'))
    print('*'*100)
    print(type(reverse_string()))
