import copy
# from wordfreq import zipf_frequency

from src.trie import Trie
from src.utils import serialize, deserialize

class Game:
    """
    Initalize Game
    """
    def __init__(self, letters):
        try:
            self.set_board(list(letters))
        except Exception:
            print("Needs 16 letters")


    def make_trie(self, lexicon):
        f = open(lexicon, 'r')
        words = f.read().split('\n')
        for word in words:
            if len(word) > 2 and len(word) < 17:
                self.trie.insert(word)
        f.close()


    def serialize_and_store(self, lexicon, store):
        self.make_trie(lexicon)
        open(store, 'w').close()
        s = serialize(self.trie.root)
        f = open(store, 'a')
        for node in s:
            f.write(node + " ")
        f.close()

    
    def deserialize_and_store(self, store):
        f = open(store, 'r')
        nodes = f.read().split(' ')
        print("constructing trie...")
        self.trie = deserialize(nodes)
        print("done!")
        f.close()


    # TODO: Make tests 
    def set_board(self, letters):
        if letters is None or len(letters) != 16:
            raise Exception("Needs 16 letters")

        self.board = []
        for i in range(0, 4):
            arr = []
            for j in range(0 + i * 4, 4 + i * 4):
                arr.append(letters[j])
            self.board.append(arr)


    def get_board(self):
        return [x for row in self.board for x in row if x != ' ']


    def calculate_words(self):
        word_list = set()
        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                word_list |= set(self.__traverse((x, y), [], ''))

        word_list = list(word_list)
        word_list.sort(key=lambda word: (-len(word), word))
        # word_list = list(filter(lambda word: zipf_frequency(word, 'en') > 0, word_list))
        
        return word_list


    def __traverse(self, current, seen, word):
        output = set()

        x, y = current
        new_word = word + self.board[x][y]
        if not self.trie.starts(new_word):
            return output

        if self.trie.search(new_word):
            output.add(new_word)
            
        seen.append(current)
        neighbors = self.__find_valid_neighbors(current, seen)

        for neighbor in neighbors:
            copied_seen = copy.deepcopy(seen)
            asdf = self.__traverse(neighbor, copied_seen, new_word)
            output |= asdf

        return output

                
    def __find_valid_neighbors(self, current, seen):
        x_pos, y_pos = current
        candidates = []

        for x in range(x_pos - 1, x_pos + 2):
            for y in range(y_pos - 1, y_pos + 2):
                if x >= 0 and y >= 0 and x < 4 and y < 4 and (x, y) not in seen:
                    candidates.append((x, y))

        return candidates