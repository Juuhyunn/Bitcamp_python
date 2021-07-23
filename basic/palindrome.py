import pprint


def str_to_list(payload : str) -> []:
    '''strs = []
    for char in payload:
        if char.isalnum():
            strs.append(char.lower())
    return strs
    '''
    return [i for i in payload if i.isalnum()]


def isPalindrome(ls: [])->bool:
    '''
        while len(ls) > 1:
        if ls.pop(0) != ls.pop():
            return False
        else:
            return True
    '''
    while len(ls) > 1:
        return [False if ls.pop(0) != ls.pop() else True]


if __name__ == '__main__':
    ls = str_to_list("A man, a plan, a canal : Panama")
    print(ls)
    isPal = isPalindrome(ls)
    print(isPal)

