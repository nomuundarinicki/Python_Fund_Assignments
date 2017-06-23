def even_odd(count):
    for num in range(1, count +1):
        if num  % 2 == 0:
            print ("{0} is Even".format(num))
        else:
            print ("{0} is Odd".format(num))

even_odd(200)
