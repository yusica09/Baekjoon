A = input()
num = A.split()
input_list = [int(i) for i in num]

corr_list = [1,1,2,2,2,8]

for i in range(len(corr_list)):
    res = corr_list[i] - input_list[i]
    print(res,end=' ')
print()
