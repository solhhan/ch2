Challenge #2: Sort Lexicographically

The function is sortLexicographically() in ch2.py. It implements a custom variation of quicksort to sort the list, giving it an average time complexity of O(nlogn). In the worst case (when the elements are ordered), it runs in O(n^2) time. The comparator it uses is compareWord(), which inspects the two given strings, character-by-character.

If we anticipate that input word lists have generally short words and contain many words, consider using radix sort instead for O(wn) time.
