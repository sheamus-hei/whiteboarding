
def detect_cake_collision(slices):
  cake_row = [0] * 10
  cake = []
  conflicts = 0
  for i in range(10):
    cake.append(cake_row.copy())
  for slice in slices:
    x = slice[0]
    y = slice[1]
    x2 = x + slice[2]
    y2 = y + slice[3]
    if x < 0:
      x = 0
    if y < 0:
      y = 0
    if x2 >= 10:
      x2 = 9
    if y2 >= 10:
      y2 = 9
    for j in range(x, x2):
      for k in range(y, y2):
        cake[j][k] += 1
        if cake[j][k] == 2:
          conflicts += 1
      
  return conflicts



slices = [
  [1, 1, 3, 4],
  [4, 1, 2, 2],
  [3, 3, 3, 100]
]
# slices[0][1]
print(detect_cake_collision(slices))


