# Program 1
import random
# 初始範圍是(0, 99)
max = 99
min = 0
# answer可以隨機或固定
# answer = random.randint(0, 99)
answer = 61

while True:
  print(f"({min},{max})?")
  n = input()
  # 若猜的數字超出範圍或不是整數就讓玩家重猜
  if n.isdigit() == False or int(n) > max or int(n) < min:
    print("Out of range. Please try again!")
  # 若猜到answer就結束遊戲
  elif int(n) == answer:
    print("Bingo.")
    break
  else:
    # 若猜的數字小於answer，則更新min
    if int(n) < answer:
      min = int(n)+1
    # 若猜的數字大於answer，則更新max
    else:
      max = int(n)-1
    # 若只剩下一個整數(即min等於max)就結束遊戲
    if min == max:
      print("GG.")
      break
