def primeNumbers(num):
    prime_list = []
    if num <= 0:
        return prime_list
    else:
        for i in range(1, num + 1):
            if i > 1:
                for x in range(2, i):
                    if  i % x == 0:
                        break
                else:
                    prime_list.append(i)

    return prime_list
