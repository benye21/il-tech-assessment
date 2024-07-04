import sys
from collections import deque

# Author: Ben Ye
# GitHub: benye21
# Date: Jul 3, 2024

# We will leverage the trie (prefix tree, reference: https://en.wikipedia.org/wiki/Trie) for building out our solution
# Prefix trees are generally used for word search or autocomplete and I think this data structure would be useful for this problem
class WordMatchUtils:
    def __init__(self, inputFileName, predefinedWordsName):
        inputFile = open('{inputFileName}.txt'.format(inputFileName=inputFileName), 'r')
        inputFileLines = inputFile.readlines()
        self.inputTrie = self.createTrie(inputFileLines, True)
        inputFile.close()

        predefinedWordsFile = open('{predefinedWordsName}.txt'.format(predefinedWordsName=predefinedWordsName), 'r')
        predefinedWordsFileLines = predefinedWordsFile.readlines()
        self.predefinedWordsTrie = self.createTrie(predefinedWordsFileLines)
        predefinedWordsFile.close()

    def createTrie(self, inputLines, toDebug=False):
        trie = {}

        for line in inputLines:
            # if empty or newline, ignore
            if not line or line == '\n':
                continue
            
            # remove special characters, spaces, and newlines at the end (i.e. ".", "?")
            index = len(line) - 1

            while not line[index].isalnum():
                index -= 1

            line = line[:index + 1]

            for word in line.split(' '):
                currTrieIterator = trie
                
                for c in word.lower():
                    if c not in currTrieIterator:
                        currTrieIterator[c] = {}
                    currTrieIterator = currTrieIterator[c]
                currTrieIterator['$wordCount$'] = currTrieIterator.get('$wordCount$', 0) + 1
                currTrieIterator['$word$'] = word

        return trie
    
    # I will be leveraging queue/bfs to check every single valid path in predefinedWordsTrie and see if there is a corresponding path in inputTrie
    def calculateWordMatchCount(self):
        inputTrieIterator = self.inputTrie
        predefinedWordsTrieIterator = self.predefinedWordsTrie
        queue = deque()
        matchCount = {}

        for char in predefinedWordsTrieIterator:
            if char in inputTrieIterator:
                if char != '$wordCount$' and char != '$word$':
                    queue.append((inputTrieIterator[char], predefinedWordsTrieIterator[char]))

        while queue:
            currInputIterator, currPredefinedWordsIterator = queue.popleft()

            if '$word$' in currInputIterator and '$word$' in currPredefinedWordsIterator:
                matchCount[currPredefinedWordsIterator['$word$']] = matchCount.get(currPredefinedWordsIterator['$word$'], 0) + currInputIterator['$wordCount$']

            for char in currPredefinedWordsIterator:
                if char != '$wordCount$' and char != '$word$' and char in currInputIterator:
                    queue.append((currInputIterator[char], currPredefinedWordsIterator[char]))

        return matchCount

if len(sys.argv) != 3:
    print('Please run python script as follows: python3 wordMatchCount.py yourInputFileName yourPredefinedWordsFileName')
    print('Note that yourInputFileName and yourPredefinedWordsFileName must be in same directory as python3 and when passing in command line args, do not include .txt at end')
    exit(1)

inputFileName = sys.argv[1]
predefinedWordsFileName = sys.argv[2]

wordMatchUtils = WordMatchUtils(inputFileName, predefinedWordsFileName)
wordMatchCount = wordMatchUtils.calculateWordMatchCount()
sortedWordMatchCount = sorted([(word, count) for word, count in wordMatchCount.items()], key = lambda x: -x[1])
formatterString = '{word:<50}\t{count:<25}'

print(formatterString.format(word='Predefined word', count='Match count'))

for word, count in sortedWordMatchCount:
    print(formatterString.format(word=word, count=wordMatchCount[word]))