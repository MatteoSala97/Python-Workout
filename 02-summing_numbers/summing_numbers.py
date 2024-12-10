def myownsum(*numbers):
    output = 0
    for i in numbers:
        output += i
    return output

print(myownsum(10,20,30,40,50))