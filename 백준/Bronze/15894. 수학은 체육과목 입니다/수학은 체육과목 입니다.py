N = int(input())

# 각 층의 윗면들은 결국 언제나 1 이므로 층수 더하고,
# 각 층의 옆면들은 결국 언제나 2 이므로 2 * 층수 더하고,
# 가장 밑층의 밑면까지 더하기 위해 N을 한번 더 더한다.
sum = N + (2 * N) + N
print(sum)