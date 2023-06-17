# cars = ['audi','ferrari','ford focus','toyota sienna hybrid']

# def car_adder(car_to_add): 
#     if car_to_add[0].lower() in 'abcdefg':
#         print("This car starts with A-G")
#         cars.append(car_to_add)
#     else: print("This car not allowed")
#     for car in cars:
#         if len(car) <= 5:
#             cars.remove(car)


# car_adder("BMW")
# car_adder("Honda")
# car_adder('Chrysler')
# car_adder('jeep')

# print(cars)

# def is_prime(num):
#     for n in range(2,num):
#         if num % n == 0:
#             print ('not prime')
#             break
#         else: 
#             print ('prime')
# is_prime(25)

# def blue(lio, hello,final = "check"):
#     print(lio,hello,final)
# blue("a","b")


def afun(x):
    return x+5

def bfun(x):
    return x*2

print(afun(5)+bfun(5))