N, k = map(int, input().split())
num_list = list(map(int, input().split()))

num_list.sort(reverse=True)

print(num_list[k-1])