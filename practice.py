print("Hello world")
print(2 + 1)
print(2 % 2)
print(2 ** 2)
a = 5
a=10
print(a)
print(a+a)
print(type(a))


name = "Jyoti Shinde, "
city = "DE "
zipcode = 19702
state = "US"

print(name[-1])
print(name[-3][-1])
print(name[2:])
print(name[:5])
print(name[1:5])
print(name[::])
print(name[::3])
#step size of 2 from index 1 to index 6(excludes 6)
print(name[1:6:2])
#reverse string
print(name[::-1])

#string concatnation
print(name + city)

#multiple string concatnation
print(city * 19)

#string methods
print(name.split(" "))
print(name.split())
print(name.split('i'))
print(name.lower( ))
print(name.upper( ))

print('My name is {}'.format('Jyoti Shinde'))

#based on index
print('The {1} {2} {0}'.format('brown', 'fox', 'is'))

#based on variable name
print('The {f} {i} {b}'.format(b ='brown', f ='fox', i ='is'))

result = 20/100
result1 = 206/400

print('The result is {}'.format(result))
print('The result is {r}'.format(r =result1))
print('The result is {r: 1.2f}'.format(r=result1))

#f string
print(f'Hello, my name is {name}')

print(f'Hello, my name is {name}, lives in {city}')
