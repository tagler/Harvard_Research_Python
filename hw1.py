import string

def counter(sentence):
    alphabet = string.ascii_letters
    sentence = sentence.lower()
    count_letters = {}
    for x in sentence:
        if x in alphabet:
            if x in count_letters:
                count_letters[x] = count_letters[x] + 1
            else:
                count_letters[x] = 1
    return count_letters

def key_with_max_value(count_letters):
     v = list(count_letters.values())
     k = list(count_letters.keys())
     return k[v.index(max(v))]

address = 'Jim quickly realized that the beautiful gowns are expensive'
address_count = counter(address)
key_with_max_value(address_count)

import math
ans = math.pi / 4
print(ans)

import random
random.seed(1)
def rand():
   return random.uniform(-1,1)
rand()

import math
def distance(x, y):
    temp = (x[0]-y[0])**2 + (x[1]-y[1])**2
    return math.sqrt(temp)
x = (0,0)
y = (1,1)
print( distance(x,y) )

import random, math
random.seed(1)
def in_circle(x, origin = [0]*2):
    return distance(x, origin) < 1
in_circle(y)

R = 10000
x = []
inside = []
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    inside.append(in_circle(point))
print( (math.pi/4) - (inside.count(True)) / len(inside) )

import random
random.seed(1)
def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    running = []
    for q in range(0,n):
        temp_sum = sum( x[q:q+width] )
        temp_average = temp_sum / width
        running.append(temp_average)
    return running
x=[0,10,5,3,1,5]
print(moving_window_average(x, 1))

import random
random.seed(1)
R=1000
x = []
for q in range(R):
    x.append(random.random())
Y = []
for r in range(10):
    temp = moving_window_average(x,r)
    Y.append(temp)
ranges = []
for each in Y:
    max_val = max(each)
    min_val = min(each)
    diff = max_val - min_val
    ranges.append(diff)

    
