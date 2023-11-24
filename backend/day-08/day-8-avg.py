def avg(numlist):
    sum = 0
    vg = 0

    for num in my_list:
        sum += num

    avg = sum / len(my_list)
    return avg

my_list = [5, 9, 2, 3, 1]
my_avg = avg(my_list)
print(my_avg)
