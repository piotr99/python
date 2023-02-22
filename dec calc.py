number=7543
binary=[4096,2048,1024,512,256,128,64,32,16,8,4,2,1]
result = ''
for i in binary:
    if i > number:
        result+='0'
    if i <= number:
        number -= i
        result+='1'
print(result) 