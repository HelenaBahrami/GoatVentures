import random
import string
import numpy as np
from collections import namedtuple
from itertools import product

# grid size width*h
width = 10
height = 10

grid_word_density = width*height
word_fill_percentage = 0.15
total_words_len = grid_word_density*word_fill_percentage


# Create the grid
grid =[[random.choice(string.ascii_lowercase) for i in range(0, width)]for j in range(0, height)]

# Place the word in  a random location in the grid, horizontally or vertically or diagonally with the placement probabilities


def place_word(word, grid):

    # Probability of word placement(pv+ph+pd)=1
    pv = 0.5
    ph = 0.3
    pd = 0.2
    horizontal = [1, 0]
    vertical = [0, 1]
    diagonal = [1, 1]

    direction_probability = np.random.choice(["horizontal", "vertical", "diagonal"], p=[pv, ph, pd])
    if direction_probability =="horizontal":
        d = horizontal
    elif direction_probability =="vertical":
        d = vertical
    elif direction_probability =="diagonal":
        d = diagonal
    # Check the coordinates to fit the world in the grid
    xsize = width if d[0] == 0 else width-len(word)
    ysize = height if d[1] == 0 else width-len(word)
    x = random.randrange(0, xsize)
    y = random.randrange(0, ysize)

    # Place a reverse word randomly
    word = random.choice([word, word[::-1]])
    for i in range(0, len(word)):
        grid[y+d[1]*i][x+d[0]*i] = word[i]
    return grid

##################################################################################################################

# # Generating random length words form the english alphabet lists
#
# list_size = 100
# min_len = 3
# max_len = 10
#
#
# def generate_words(min_len, max_len):
#     length = random.randint(min_len, max_len)
#     return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
#
#
# def generate_word_list(list_size):
#     result = []
#     for i in range(list_size):
#         result += [generate_words(min_len, max_len)]
#     return result
#
#
# generate_words(min_len, max_len)
# data = generate_word_list(list_size)

##################################################################################################################

# Reading english words from a text file


def words_file():
    # filename = 'n_words.txt'
    filename = 'n_wordstest.txt'
    with open(filename) as f:
        data = f.readlines()
    #  remove whitespace characters like `\n` at the end of each line
    data = [x.strip() for x in data]
    list_of_all_words = []
    for x in data:
        if len(x) < width and len(x) < height and len(x):
            list_of_all_words.append(x)
            data = list_of_all_words
    return data

data = words_file()
# Creating list for words for placement according to arbitrary percentage of grid's word density


def word_list_selection(data):
    min_len = 4
    total_take = 0
    word_list = []
    while total_take < total_words_len - min_len:
        item = np.random.choice(data, replace=False)
        if len(item) < total_words_len - total_take:
            word_list.append(item)
            total_take += len(item)
    return word_list


word_list = word_list_selection(data)
for word in word_list:
    grid = place_word(word, grid)

grid_view = "\n".join(map(lambda row: " ".join(row), grid))

# Output the words grid
print("**************************   The word grid   ************************** ")
print(grid_view)
print(71*'*')

# Defining direction for search
Direction = namedtuple('Direction', 'di dj name')
DIRECTIONS = [
    Direction(-1, -1, "diagonal direction to the left"),
    Direction(-1,  0, "horizontal direction to the left"),
    Direction(-1, +1, "diagonal up and to the right"),
    Direction(0, -1, "vertical direction to the left"),
    Direction(0, +1, "vertical direction to the right"),
    Direction(+1, -1, "diagonal down and to the left"),
    Direction(+1,  0, "horizontal direction to the right"),
    Direction(+1, +1, "diagonal direction to the right"),
]

# evoke letters from the grid to pass to search_word()


def grid_letters(grid, i, j, dir, length):

    if ( 0 <= i + (length - 1) * dir.di < len(grid) and
         0 <= j + (length - 1) * dir.dj < len(grid[i])):
        return ''.join(
            grid[i + n * dir.di][j + n * dir.dj] for n in range(length)
        )
    return None

# Search for word in the grid


def search_word(grid, s_word):

    word_len = len(s_word)
    for i, j, dir in product(range(len(grid)), range(len(grid[0])), DIRECTIONS):
        if s_word == grid_letters(grid, i, j, dir, word_len):
            return i, j, dir
    return None


for i_word in word_list:
    match = search_word(grid, i_word)
    if match is None:
        print("Didn't find a match.")
    else:
        i, j, dir = match
        print('"{}"'.format(i_word), "is found at ({0},{1}) in {2}".format(
                i + 1, j + 1, dir.name))




