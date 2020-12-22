from src.game import Game

def main():
    g = Game('tcedgwiaethlrnrg')
    g.deserialize_and_store('serialized_trie.txt')
    word_list = g.calculate_words()

    for word in word_list[:50]:
            print(word)


if __name__ == "__main__":
    main()
