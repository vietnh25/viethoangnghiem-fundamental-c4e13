#in 0 - 100
# for i in range(100):
    # print(i, end = ' ')
#print(*range(101))
#in 0 - 100 (chi co so chan) 
# for i in range(0, 101, 2):
    # print(i)
# print(*range(0, 101, 2))
# in 100 - 0
# print(*range(100, -1, -1))
# cal the sum
n = int(input('enter a number '))
sum = 0
for num in range(0, n+1, 1):
    sum = sum+num
print("SUM of first ", n, "numbers is: ", sum )
