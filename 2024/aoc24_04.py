def count_word_in_grid(grid, word):
    directions = [
        (0, 1),  # Right
        (0, -1),  # Left
        (1, 0),  # Down
        (-1, 0),  # Up
        (1, 1),  # Down-Right
        (-1, -1),  # Up-Left
        (1, -1),  # Down-Left
        (-1, 1)  # Up-Right
    ]
    rows, cols = len(grid), len(grid[0])
    word_len = len(word)
    count = 0

    def search_from(x, y, dx, dy):
        """Search for the word starting from (x, y) in direction (dx, dy)."""
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    def is_valid(x, y):
        """Check if a coordinate is within grid bounds."""
        return 0 <= x < rows and 0 <= y < cols

    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search_from(x, y, dx, dy):
                    count += 1

    return count


def count_pattern_in_grid(grid, patterns):
    rows, cols = len(grid), len(grid[0])
    p_rows, p_cols = len(patterns[0]), len(patterns[0][0])
    count = 0

    def matches_pattern(x, y):
        for pattern in patterns:
            match = True
            for i in range(p_rows):
                for j in range(p_cols):
                    # Only check non-empty pattern elements
                    if pattern[i][j] and pattern[i][j] != grid[x + i][y + j]:
                        match = False
                        break
                if not match:
                    break
            if match:
                return True
        return False

    for x in range(rows - p_rows + 1):
        for y in range(cols - p_cols + 1):
            if matches_pattern(x, y):
                count += 1

    return count


with open("demo4.txt") as file:
    crosswords = [word for line in file.readlines() for word in line.split()]
    target = "XMAS"
    patterns = [
       [
            ['M', None, 'S'],  # None indicates "any character"
            [None, 'A', None],
            ['M', None, 'S']
        ],
        [
            ['S', None, 'S'],  # None indicates "any character"
            [None, 'A', None],
            ['M', None, 'M']
        ],
        [
            ['M', None, 'M'],  # None indicates "any character"
            [None, 'A', None],
            ['S', None, 'S']
        ],
        [
            ['S', None, 'M'],  # None indicates "any character"
            [None, 'A', None],
            ['S', None, 'M']
        ],
    ]


    print(count_word_in_grid(crosswords, target))
    print(count_pattern_in_grid(crosswords, patterns))
