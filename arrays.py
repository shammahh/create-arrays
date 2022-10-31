import random
## 1
Jmonths = ["January", "June", "July"]
print(Jmonths)

## 2
joylist = []
for i in range(700):
    joylist.append("joy")
print(len(joylist))

## 3
sevenlist = []
for i in range(500):
    sevenlist.append(7)
print(len(sevenlist))

## 4
randomlist = []
for i in range(5000):
    randum = random.randint(0,100)
    fullnum = random.random() + randum
    randomlist.append(fullnum)
print(len(randomlist))

## 5
randomlist2 = []
for i in range(300):
    randum = random.randint(0,39)
    fullnum = random.random() + randum
    randomlist2.append(fullnum)
print(len(randomlist2))

## 6
fourslist = []
num = 20
while num < 100:
    num = num + 4
    fourslist.append(num)
print(fourslist)

## 7
evennums = []
num = 102
while num > 10:
    num = num - 2
    evennums.append(num)
print(len(evennums))
print(evennums)

## 8
colors_str = "red,orange,yellow,green,blue,indigo,violet"
colorlist = colors_str.split(',')
print(colorlist)

## 9
cities_str = "Edmonton;Calgary;Vancouver;Saskatoon;Winnipeg"
cities = cities_str.split(';')
print(cities)

## 10
namearr = []
loop = True
while loop:
    name = input("Please enter a name, or enter 'Done' when finished")
    if name == "Done":
        loop = False
        print(namearr)
    else:
        namearr.append(name)

