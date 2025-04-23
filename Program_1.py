# Program 1
import random
max = 99
min = 0
# answer = random.randint(0, 99)
answer = 61

while True:
  print(f"({min},{max})?")
  n = input()
  if n.isdigit() == False or int(n) > max or int(n) < min:
    print("Out of range. Please try again!")
  elif int(n) == answer:
    print("Bingo.")
    break
  else:
    if int(n) < answer:
      min = int(n)+1
    else:
      max = int(n)-1
    if min == max:
      print("GG.")
      break
