x = int(input('Enter a number: '))
result = ''

if x % 3 == 0:
    result += 'Fizz'
if x % 5 == 0:
    result += 'Buzz'
if result == '':
    result = x

print(result)