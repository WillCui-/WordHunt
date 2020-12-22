import unittest
import sys
import io

from src.game import Game
from src.trie import Trie

class TestGame(unittest.TestCase):
    def test_init_type(self):
        g = Game("aaaaaaaaaaaaaaaa")
        self.assertIsInstance(g, Game)


    def test_init_exception(self):
        output = io.StringIO()
        sys.stdout = output
        
        g = Game("")

        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "Needs 16 letters\n")


    def test_make_trie(self):
        g = Game("abcdefghijklmnop")
        g.make_trie("test_file.txt")

        self.assertIsInstance(g.trie, Trie)
        self.assertTrue(g.trie.search("beta"))
        self.assertFalse(g.trie.search("asdfghjkl"))
        self.assertTrue(g.trie.starts("al"))
        self.assertFalse(g.trie.starts("bets"))

    
    def test_serialize_and_store(self):
        g = Game("abcdefghijklmnop")
        store = "test_serialize.txt"
        g.serialize_and_store("test_file.txt", store)
        
        f = open(store, 'r')
        list_of_nodes = f.read().split(' ')
        self.assertIsInstance(list_of_nodes, list)
        if len(list_of_nodes) > 0:
            self.assertIsInstance(list_of_nodes[0], str)
        
    
    def test_deserialize_and_store(self):
        g = Game("abcdefghijklmnop")
        store = "test_serialize.txt"
        g.serialize_and_store("test_file.txt", store)
        g.deserialize_and_store(store)

        self.assertIsInstance(g.trie, Trie)
        self.assertTrue(g.trie.search("beta"))
        self.assertFalse(g.trie.search("asdfghjkl"))
        self.assertTrue(g.trie.starts("al"))
        self.assertFalse(g.trie.starts("bets"))


    def test_calculate_words(self):
        g = Game("betaefghijklmnop")
        g.deserialize_and_store("test_serialize.txt")
        word_list = g.calculate_words()
        
        self.assertIsInstance(word_list, list)
        if len(word_list) > 0:
            self.assertIsInstance(word_list[0], str)

        self.assertTrue('beta' in word_list)
        
