# Program 2
import random
NaiveWinCnt = 0
BSWinCnt = 0

for _ in range(0,1000):
  answer = random.randint(0, 99)
  # Program 2 Naive
  max = 99
  min = 0
  while min < max:
    # print(f"({min},{max})?")
    n = random.randint(min, max) # 玩家猜數字的部分用取隨機整數(範圍內)取代
    # print(n)
    if n == answer:
      # print("Bingo.")
      NaiveWinCnt = NaiveWinCnt + 1 # 將猜中answer的次數記錄下來以計算勝率
      break
    else:
      if n < answer:
        min = n+1
      else:
        max = n-1
  # Program 2 Binary Search
  max = 99
  min = 0
  while min < max:
    # print(f"({min},{max})?")
    n = (min + max) // 2 # 玩家猜數字的部分用取中間整數(範圍內)取代
    # print(n)
    if n == answer:
      # print("Bingo.")
      BSWinCnt = BSWinCnt + 1 # 將猜中answer的次數記錄下來以計算勝率
      break
    else:
      if n < answer:
        min = n+1
      else:
        max = n-1

print(f"Naive AI ({NaiveWinCnt/1000})")
print(f"Binary Search AI ({BSWinCnt/1000})")
