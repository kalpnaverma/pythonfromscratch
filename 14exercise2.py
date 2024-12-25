

import time
curr = time.time()
print("Current time in seconds since epoch =", curr)



curr = time.ctime(1627908313.717886)
print("Current time:", curr) 

from time import gmtime, strftime
s = strftime("%a, %d %b %Y %H:%M:%S", 
             gmtime(1627987508.6496193))
print(s)

import time
obj = time.gmtime(1627987508.6496193)
print(obj)

print(s)
