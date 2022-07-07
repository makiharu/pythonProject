# num_tuple = (10, 20)
# print(num_tuple)
#
# x,y = num_tuple
# print(x, y)
#
# x, y = 10, 20
# print(x, y)
#
# min, max = 0, 100
# print(min, max)
#
# a = 100
# b = 200
# tmp = 200
# b = a
# a = tmp
# print(a, b)
#
# # tuple
# a = 100
# b = 200
# print(a, b)
# a, b = b, a
# print(a, b)

# tupeの使い所
chose_from_two = ('A', 'B', 'C')

answer = []
# listだと起こりうるミスを排除できる
# chose_from_two.append('A')
# chose_from_two.append('C')

answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)


