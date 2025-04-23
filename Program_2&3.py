# Program 2、3
import random
NaiveWinCntP2 = 0
NaiveWinCntP3 = 0
BSWinCntP2 = 0
BSWinCntP3 = 0

for _ in range(0,1000):
  answer = random.randint(0, 99)
  # Program 2 Naive
  max = 99
  min = 0
  Cnt = 0
  while min < max:
    # print(f"({min},{max})?")
    n = random.randint(min, max)
    Cnt = Cnt + 1
    # print(n)
    if n == answer:
      # print("Bingo.")
      if Cnt <= 7:
        NaiveWinCntP3 = NaiveWinCntP3 + 1
      NaiveWinCntP2 = NaiveWinCntP2 + 1
      break
    else:
      if n < answer:
        min = n+1
      else:
        max = n-1
  # Program 2 Binary Search
  max = 99
  min = 0
  Cnt = 0
  while min < max:
    # print(f"({min},{max})?")
    n = (min + max) // 2
    Cnt = Cnt + 1
    # print(n)
    if n == answer:
      # print("Bingo.")
      if Cnt <= 7:
        BSWinCntP3 = BSWinCntP3 + 1
      BSWinCntP2 = BSWinCntP2 + 1
      break
    else:
      if n < answer:
        min = n+1
      else:
        max = n-1

print("Program 2")
print(f"Naive AI ({NaiveWinCntP2/1000})")
print(f"Binary Search AI ({BSWinCntP2/1000})")
print("\nProgram 3")
print(f"Naive AI ({NaiveWinCntP3/1000})")
print(f"Binary Search AI ({BSWinCntP3/1000})")
