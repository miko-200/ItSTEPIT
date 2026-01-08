def generate_maze(width, height):
    # Ensure odd dimensions
    if width % 2 == 0:
        width += 1
    if height % 2 == 0:
        height += 1

    # Create grid full of walls
    maze = [[1 for _ in range(width)] for _ in range(height)]

    # Simple pseudo-random generator (LCG)
    seed = 123456

    def rand():
        nonlocal seed
        seed = (1103515245 * seed + 12345) % (2**31)
        return seed

    # Directions: (dx, dy)
    directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]

    def shuffle(lst):
        for i in range(len(lst) - 1, 0, -1):
            j = rand() % (i + 1)
            lst[i], lst[j] = lst[j], lst[i]

    def carve(x, y):
        maze[y][x] = 0
        shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1:
                if maze[ny][nx] == 1:
                    maze[y + dy // 2][x + dx // 2] = 0
                    carve(nx, ny)

    # Start carving from (1,1)
    carve(1, 1)

    return maze

maze = generate_maze(11,11)
print(maze)