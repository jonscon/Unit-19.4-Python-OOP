"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    """Machine to generate random word from provided text file.
            
    >>> wf = WordFinder("test.txt")
    5 words read.

    >>> wf.random() in ["hi", "my", "name", "is", "jon"]
    True

    >>> wf.random() in ["hi", "my", "name", "is", "jon"]
    True

    >>> wf.random() in ["hi", "my", "name", "is", "jon"]
    True
    """

    def __init__(self, path):
        """Read words and return number of words read."""

        dict_file = open(path)
        
        self.words = self.parse_file(dict_file)
        print(f"{len(self.words)} words read.")

    def parse_file(self, dict_file):
        """Parse lines of the file and return a list of the words."""

        return [word.strip() for word in dict_file]
    
    def random(self):
        """Return random word."""

        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
    
    >>> swf = SpecialWordFinder("special_test.txt")
    4 words read.

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True

    >>> swf.random() in ["kale", "parsnips", "apple", "mango"]
    True
    
    """

    def parse_file(self, dict_file):
        """Parse lines of the file and return a list of only the words, not comments/blank lines."""

        return [word.strip() for word in dict_file if word.strip() and not word.startswith('#')]