print('IT calculator')
number = '01101010101010111'
def binToTen():
    values=[]
    result = 0
    index=1
    for num in reversed(number):
        values.append(num)
    for i in values:
        if i == '1':
            result+=index
            index*=2
        else:
            index*=2
    return result
#    print(values[-1])
x = binToTen()
print(x)




