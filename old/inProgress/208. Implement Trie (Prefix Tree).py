class TrieNode:
    def __init__(self):
        self.childNodes = {}
        self.isWordEnd = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        we will start with root node and check for the first character
        if there is already a node present for the character we will fetch that node, else we will create a new node
        then we will iterate to next character
        """
        currNode = self.root
        for ch in word:
            node = currNode.childNodes.get(ch , TrieNode())
            currNode.childNodes[ch] = node
            currNode = node

        # after all the characters are traversed, mark the last node as end of word
        currNode.isWordEnd = True



    def search(self, word: str) -> bool:
        """
        we will start from root node and check for all the characters
        if we could not find a node for a character we will return False there
        once we iterate through all character we will check if that is a word end
        """

        currNode = self.root
        for ch in word:
            node = currNode.childNodes.get(ch)
            if  not node:
                return False
            currNode = node

        return currNode.isWordEnd


    def startsWith(self, prefix: str) -> bool:
        """
        starts with is similar to search except here we don't have to check whether the last character is end of word
        """
        currNode = self.root
        for ch in prefix:
            node = currNode.childNodes.get(ch)
            if not node:
                return False
            currNode = node

        return True


## FAster solution from leetcode

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curNode = self.node
        for char in word:
            if char not in curNode:
                curNode[char] = {}
            curNode = curNode[char]
        curNode['#'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curNode = self.node
        for char in word:
            if char not in curNode:
                return False
            curNode = curNode[char]
        return '#' in curNode

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curNode = self.node
        for char in prefix:
            if char not in curNode:
                return False
            curNode = curNode[char]
        return True