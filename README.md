### Prerequisities

* Python3 (other python verions may work too but I only ran with Python3)
* Working terminal to run command below

### Setup

1. Create input.txt file and add input
2. Create predefinedWords.txt file and add predefined words
3. Run the following command in this directory:
    ```
    python3 wordMatchCount.py input predefinedWords
    ```
NOTE: You can choose to name the input and predefinedWords files differently as well but make sure they reflect in command line args when running command above

Sentences generated using https://randomwordgenerator.com/sentence.php

### Assumptions
* Words are separated by space on each line
* apostrophe words will be counted as new words (poodle will not match to poodle's)
* empty lines will be ignored
* Only valid words (since requirement details said only English words)
* Only valid sentences (one space between each word per line)

### What Has Been Tested
* Testing lowercase and uppercase
* Testing with special characters or spaces or newlines at end of each line
* Testing combination of large/small input and predefined words
* NOTE: I did not attach large test inputs 

Author: Ben Ye<br>Date: Jul 3, 2024
