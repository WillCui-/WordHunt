import unittest
from src.utils import serialize, deserialize
from src.trie import Trie

class TestUtils(unittest.TestCase):
    def test_serialize_deserialize(self):
        trie = Trie()
        trie.insert('h')
        trie.insert('hh')
        trie.insert('he')
        ser = serialize(trie.root)

        self.assertEqual(len(ser), 14)

        de = deserialize(serialize(trie.root))
        self.assertIsInstance(de, Trie)
        self.assertEqual(trie.root.keys(), de.root.keys())
        self.assertEqual(trie.root['h'].keys(), de.root['h'].keys())