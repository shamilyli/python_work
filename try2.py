""" introduction for []"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized'] 
print(bicycles) #['trek', 'cannondale', 'redline', 'specialized']

print(bicycles[0]) #trek

print(bicycles[1].title()) #Cannondale

print(bicycles[-1]) #specialized

message = "My first bicycle wa a " + bicycles[0].title() +"."
print(message)


motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)#['honda', 'yamaha', 'suzuki'] 

motorcycles[0] = 'ducati' 
print(motorcycles)#['ducati', 'yamaha', 'suzuki'] 

motorcycles.append('ducati')
print(motorcycles)#['ducati', 'yamaha', 'suzuki', 'ducati']

motorcycles = []
motorcycles.append('jimmy')
motorcycles.append('bb')
motorcycles.append('cc')
print(motorcycles) #['jimmy', 'bb', 'cc']

del motorcycles[2]
print(motorcycles) #['jimmy', 'bb']

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)#['honda', 'yamaha', 'suzuki']

popped_motorcycle = motorcycles.pop()
print(motorcycles)#['honda', 'yamaha']
print(popped_motorcycle)#suzuki

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('suzuki')
print(motorcycles)#['honda', 'yamaha'] remove by knowing the name

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)#['audi', 'bmw', 'subaru', 'toyota']

cars.sort(reverse=True)
print(cars)#['toyota', 'subaru', 'bmw', 'audi']

print(cars) #original list
print(sorted(cars)) # sorted list
print(cars) # original list

print(len(cars)) # 4