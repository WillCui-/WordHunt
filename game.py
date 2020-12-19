from trie import Trie
from wordfreq import zipf_frequency
import copy

class Game:
    """
    Initalize Game
    """
    def __init__(self, letters):
        self.board = []
        self.set_board(list(letters))
        
        print("Making Trie...")
        self.trie = Trie()
        self.make_trie('words_alpha.txt')
        print("Trie complete!")

        self.calculate_words()


    def make_trie(self, lexicon):
        f = open(lexicon, 'r')
        words = f.read().split('\n')
        for word in words:
            if len(word) > 2 and len(word) < 17:
                self.trie.insert(word)


    def set_board(self, letters):
        if len(letters) is not 16:
            raise Exception("Need 16 letters")

        self.board = []
        for i in range(0, 4):
            arr = []
            for j in range(0 + i * 4, 4 + i * 4):
                arr.append(letters[j])
            self.board.append(arr)


    def calculate_words(self):
        word_list = set()
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                word_list |= set(self.traverse((x, y), [], ''))

        word_list = list(word_list)
        word_list.sort(key=lambda word: (-len(word), word))
        word_list = list(filter(lambda word: zipf_frequency(word, 'en') > 0, word_list))
        for word in word_list[:50]:
            print(word)


    def traverse(self, current, seen, word):
        output = set()

        x, y = current
        new_word = word + self.board[x][y]
        if not self.trie.starts(new_word):
            return output

        if self.trie.search(new_word):
            output.add(new_word)
            
        seen.append(current)
        neighbors = self.find_valid_neighbors(current, seen)

        if not neighbors:
            return output

        for neighbor in neighbors:
            copied_seen = copy.deepcopy(seen)
            asdf = self.traverse(neighbor, copied_seen, new_word)
            output |= asdf

        return output

                
    def find_valid_neighbors(self, current, seen):
        x_pos, y_pos = current
        candidates = []

        for x in range(x_pos - 1, x_pos + 2):
            for y in range(y_pos - 1, y_pos + 2):
                if x >= 0 and y >= 0 and x < 4 and y < 4 and (x, y) not in seen:
                    candidates.append((x, y))

        return candidates