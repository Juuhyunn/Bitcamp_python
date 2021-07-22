# example 1
def one_to_ten_sum_1():
    sum = 0
    for i in range(1, 11):
        sum += i
    print(sum)
    
#example 2
def one_to_ten_sum_2():
    print(sum(i for i in range(1, 11)))

#example 3
def one_to_ten_sum_3():
    print(sum(range(1, 11)))


if __name__ == '__main__':
    #one_to_ten_sum_1()
    #one_to_ten_sum_2()
    one_to_ten_sum_3()