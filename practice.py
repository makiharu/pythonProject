# 1行 1文字
# s = input()
# print(s)

# 1行 n文字 abc def ghi
# a, b, c = input().split()
# print(a)
# print(b)
# print(c)

# str_list = list(input().split())  # n個の文字列がリストに格納される
# print(str_list[0])

# 1行n数字 1 2 3
# a, b, c = map(int, input().split())
# print(a, b, c)

# n行1文字
# 3
# aa
# a
# aaa
# n = int(input())  # nは入力回数
# str_list = [input() for _ in range(n)]
# print(str_list)   # 出力を確認

# n行1数字
# 4
# 2
# 3
# 4
# 5
# n = int(input())  # nは入力回数
# num_list = [int(input()) for _ in range(n)]
# print(num_list)   # 出力を確認

# n = int(input())
# num_list = [int(input()) for _ in range(n)]
# print(num_list)

# n行n文字
# 3
# aaa b cc
# d ee fff
# gg hhh i
n = int(input())  # nは入力回数
str_list = []
for i in range(n):
    str_list.append(list(input().split()))
print(str_list)

# n = int(input())  # nは入力回数
# str_list = [list(input().split()) for _ in range(n)]
# print(str_list)