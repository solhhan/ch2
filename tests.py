import unittest
from ch2 import sortLexicographically, compareWords

class TestLexicographicSort(unittest.TestCase):
	# Run some tests
	def testSortLexicographically(self):
		self.assertEqual(["cat", "bat"], ["cat", "bat"])
		self.assertEqual(1, 1)

		test_seq = ["acb", "abc", "bca"]
		test_order = "abc"
		sortLexicographically(test_seq, test_order)
		self.assertEqual(test_seq, ['abc', 'acb', 'bca'])

		test_seq = ["acb", "abc", "bca"]
		test_order = "cba"
		sortLexicographically(test_seq, test_order)
		self.assertEqual(test_seq, ['bca', 'acb', 'abc'])

		test_seq = ["aaa", "aa", ""]
		test_order = "a"
		sortLexicographically(test_seq, test_order)
		self.assertEqual(test_seq, ['', 'aa', 'aaa'])

		test_seq = []
		test_order = "a"
		sortLexicographically(test_seq, test_order)
		self.assertEqual(test_seq, [])

		test_seq = ["", ""]
		test_order = ""
		sortLexicographically(test_seq, test_order)
		self.assertEqual(test_seq, ['', ''])

		test_seq = ["apple", "banana", "pineapple", "bananaphone"]
		test_order = "abcdefghijklmnopqrstuvwxyz"
		sortLexicographically(test_seq, test_order)
		self.assertEqual(test_seq, ['apple', 'banana', 'bananaphone', 'pineapple'])

		test_seq = ["edcba", "", "abcde", "edcb", "abcde", "", "e", "eeeee"]
		test_order = "edcba"
		sortLexicographically(test_seq, test_order)
		self.assertEqual(test_seq, ['', '', 'e', 'eeeee', 'edcb', 'edcba', 'abcde', 'abcde'])

	# test compareWords(), which is called as a comparator function in sortLexicographically()
	def testCompareWords(self):
		testStr1 = ""
		testStr2 = ""
		testOrder = ""
		self.assertEqual(compareWords(testStr1, testStr2, testOrder), 0)

		testStr1 = ""
		testStr2 = "abc"
		testOrder = "abc"
		self.assertEqual(compareWords(testStr1, testStr2, testOrder), -1)

		testStr1 = "abc"
		testStr2 = "abcde"
		testOrder = "abcde"
		self.assertEqual(compareWords(testStr1, testStr2, testOrder), -1)

		testStr1 = "abcde"
		testStr2 = "abc"
		testOrder = "abcde"
		self.assertEqual(compareWords(testStr1, testStr2, testOrder), 1)

		testStr1 = "za"
		testStr2 = "az"
		testOrder = "za"
		self.assertEqual(compareWords(testStr1, testStr2, testOrder), -1)

		testStr1 = "cat"
		testStr2 = "dog"
		testOrder = "dcoagt"
		self.assertEqual(compareWords(testStr1, testStr2, testOrder), 1)

if __name__ == "__main__":
	unittest.main()
