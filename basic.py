# comment
long_text = """multi line comment free s't"ring"""
print(long_text)

# if condition
if False:
    print('true')
elif False:
    print('false')
else:
    print('else')

# define function
def cordinate():
    return 5, 10
x, y = cordinate()
print('{}, {}'.format(x,y))

# input function
res = input('input: ')
print(res)

# list
list1 = [1, 2, 3]
list1.append(4)
print(list1[-1]) # last element
list2 = [5,6,7]
list3 = list1 + list2
print(list3)

print(4 in list1)
del list1[0]
print(list1)
list1.remove(2)
print(list1)

# for
for ele in list3:
    print(ele, end=' ')

for ele in range(len(list3)):
    print(ele)

state = ['a', 'b', 'c']
for i, ele in enumerate(state):
    print("""{}.'{}'""".format(i+1, ele))