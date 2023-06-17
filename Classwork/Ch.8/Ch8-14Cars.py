def car_data(manufacturer, model, **other):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in other.items():
        car[key]=value
    return car

my_car=car_data('Suburu', 'Mirage', color= 'blue', wheels= '4')
print(my_car)

