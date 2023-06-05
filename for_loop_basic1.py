1.

for i in range(151):
    print(i)


2.

for i in range(5,1000,5):
    print(i)


3.

for i in range(1,100):
    if i % 5 == 0:
        print('Coding')
    if i % 10 == 0:
        print('Coding Dojo')


4.

sum = 0
for i in range(0, 500001, 3):
    sum += i
    print(sum)


5.

def count_down_four():
    num = 2018
    while num > 0:
        print(num)
        num = num - 4


6.

def flex(low, high ,mult):
    for i in range(low, high):
        if i % mult == 0:
            print(i)

flex(2, 9, 3)
