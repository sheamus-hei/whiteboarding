grid = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
]

def find_perimeter(grid, startX, startY):
  sizeX = len(grid[0]) 
  sizeY = len(grid)
  perimeter = 0
  color = grid[startY][startX]

  to_traverse = [(startX, startY)]
  visitedRow = [False] * sizeX 
  visited = []
  for col in range(sizeY):
    visited.append(visitedRow.copy())

  while len(to_traverse) > 0:
    X, Y = to_traverse.pop()
    if visited[Y][X]:
      continue
    visited[Y][X] = True
    # check all NESW
    neighbors = [(X, Y+1), (X+1, Y), (X, Y-1), (X-1, Y)]
    for nX, nY in neighbors:
      nX = (nX + sizeX) % sizeX
      nY = (nY + sizeY) % sizeY
      if grid[nY][nX] == color:
        to_traverse.append((nX, nY))
      else:
        perimeter += 1

  return perimeter

print(find_perimeter(grid, 0, 0))