import math
test_length = 1000000
total_squariness = 0

for i in range(test_length):
    j = i +1
    p = math.floor(math.sqrt(j))
    #Becuase p is the smalle factor the largest value that p can be is the square root of your value j. It will also be the largest such value, so it is easier to start at the
    # square root and decrement from there stopping at the first value that works, than it would be to start at 1 and increment up to the largest value. 
    while j % p != 0:
        p += -1
        # This means (j) = p*q, which can be rearranged as q = (j)/p. Therefore p/q = p/((j)/p) = (p^2)/j.
    total_squariness += ((p)**2)/(j)

average_squariness = total_squariness/test_length

print(average_squariness)
