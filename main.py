import random

list = [34, 76, 23, 48, 19, 596, 48, 1, 34, 4, 80, 458, 600]

for i in range(13):
  if i > 0 and i < 12:
    list[i] = list[i-1] + list[i+1]
  else:
    list[i] = list[i] + random.randint(0, 100)
    
print("Done with Phase 1! Continuing to Phase 2...")

for i in range(13):
  if i > 0 and i < 12:
    list[i] = list[i-1] * list[i+1]
  else:
    list[i] = list[i] + random.randint(0, 100)
    
print("Done with Phase 2! Press enter to end the program.")
input()
