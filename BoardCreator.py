import random

words_coords = {}

def create_board(words, orientation='vertical'):
    words_size = [(w[0], len(w[0])) for w in words]
    longest_word = max(words_size, key=lambda w: w[1])
    if(longest_word[1] - len(words) >= longest_word[1]/2):
        rows = longest_word[1]
        cols = longest_word[1]
    else:
        rows = len(words)*2
        cols = len(words)*2
    words_to_add = len(words)
    completed_row_col = [0 for i in range(rows)]
    board = [[('', None) for h in range(cols)] for i in range(rows)]
    if(orientation == 'vertical'):
        while words_to_add > 0:
            random_col = random.randint(0, cols-1)
            if(not completed_row_col[random_col]):
                is_added = False
                while(not is_added):
                    random_row = random.randint(0, rows-1)
                    word = words[words_to_add-1][0]
                    if(rows - random_row >= len(word)):
                        words_coords[word] = []
                        h = 0
                        for row in range(random_row, len(word)+random_row):
                            board[row][random_col] = (word[h], words[words_to_add-1][1])
                            words_coords[word].append((row, random_col))
                            h += 1
                        is_added = True
                completed_row_col[random_col] = 1
                words_to_add -= 1
    elif(orientation == 'horizontal'):
        while words_to_add > 0:
            random_row = random.randint(0, rows-1)
            if(not completed_row_col[random_row]):
                is_added = False
                while(not is_added):
                    random_col = random.randint(0, cols-1)
                    word = words[words_to_add-1][0]
                    if(cols - random_col >= len(word)):
                        words_coords[word] = []
                        h = 0
                        for col in range(random_col, len(word)+random_col):
                            board[random_row][col] = (word[h], words[words_to_add-1][1])
                            words_coords[word].append((random_row, col))
                            h += 1
                        is_added = True
                completed_row_col[random_row] = 1
                words_to_add -= 1
    return board

def get_words_coords():
    return words_coords
