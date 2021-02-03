from src.game import Game
from app import app
import time

# def main():
#     g = Game('rheatbinrsbdyeoo')
#     g.deserialize_and_store("serialized_trie.txt")
#     # g.make_trie('words_alpha.txt')
#     word_list = g.calculate_words()
    
#     for word in word_list[:50]:
#         print(word)


if __name__ == "__main__":
    app.run()
    start = time.time()
    # main()
    print("Runtime: %s seconds" % (time.time() - start))
