numbers = [1,2,3,4,5,6,7,8,9]
numbers.append(15) #single value
numbers.extend([12,27])#multiple values
print(numbers)
# output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 12, 27]


numbers.append("Joseph")
print(numbers)

#ouput:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 12, 27]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 12, 27, 'Joseph']

print(len(numbers))# 13
