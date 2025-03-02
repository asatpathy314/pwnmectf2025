
import binascii

grid = """. . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . . .
. . . . . . . . 0 . . . . . 1 1
. 1 1 . . 1 . 1 . . . 1 . . . .
1 . . 0 . . . . . . . 1 . . . .
. . . . . . . 1 . 0 . . 0 . 0 .
0 . . . . . . . . . . . . . 0 0
. . 0 0 . . . . . . 1 1 . . . .
. . . . . . 0 . 1 . . . . . . 0
. . 1 . . 1 . . . 1 . . . . 1 .
. 1 1 . . . . . . . . 0 . . . .
. . . . . . 1 . . . . . 1 . 1 1
. . . . . . . . . . . . . . . .
. . . . . . 0 . . 1 . . . . . 0
. . . . . . . . . . . . . . . ."""

beginning = "100101010011010101011001101010100110101001010101"
end = "00110010"
encrypted_bytes = "c56217e72f2ee27f0ec1f00f06956493ab02a2f8072159f3a27e79d399a4924f"

# Convert grid to a list of characters (strings are immutable)
grid = list(grid.replace("\n", "").replace(" ", "").replace(".", "*"))
print(grid)

print(len(grid))

# Modify specified sections (adjust indices as needed)
grid[:len(beginning)] = list(beginning)  # Replace beginning section
grid[len(grid)-len(end):] = list(end)             # Replace end section

# Create 16x16 grid view
grid_2d = [grid[i*16:(i+1)*16] for i in range(16)]

# Display formatted grid
print('\n'.join(''.join(row) for row in grid_2d))

solved_grid = """1 0 0 1 0 1 0 1 0 0 1 1 0 1 0 1 
0 1 0 1 1 0 0 1 1 0 1 0 1 0 1 0 
0 1 1 0 1 0 1 0 0 1 0 1 0 1 0 1 
1 0 0 1 0 1 1 0 0 1 0 0 1 0 1 1 
0 1 1 0 0 1 0 1 1 0 1 1 0 1 0 0 
1 0 1 0 1 0 1 0 0 1 0 1 1 0 1 0 
0 1 0 1 1 0 0 1 1 0 1 0 0 1 0 1 
0 0 1 1 0 1 1 0 1 1 0 0 1 1 0 0 
1 1 0 0 1 0 0 1 0 0 1 1 0 0 1 1 
1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 
0 0 1 1 0 1 1 0 0 1 0 1 0 0 1 1 
0 1 1 0 1 0 0 1 1 0 1 0 1 1 0 0 
1 0 0 1 0 0 1 1 0 1 0 0 1 0 1 1 
0 0 1 0 0 1 1 0 1 0 1 1 0 1 0 1 
1 1 0 0 1 1 0 0 1 1 0 0 1 0 1 0 
1 0 1 1 0 0 1 1 0 0 1 1 0 0 1 0"""

solved_grid = solved_grid.replace("\n", " ").replace(" ", "")
print(solved_grid)