Keshav Malhotra 
NETID : kmalhtr3

Problem 1:
- change the variable cwd in line 41 to contain the working directory
- cd into the directory containing the file and run "python letterLangId.py"
- The accuracy will be printed on the console and is calculated by checking output file against the test file
- The output is written to wordLanId.out

Problem 2:
- change the variable cwd in line 31 to contain the working directory
- cd into the directory containing the file and run "python wordLangId.py"
- The accuracy will be printed on the console and is calculated by checking output file against the test file
- The output is written to wordLanId.out


Analysis 

The accuracy for letter bigram model was caculated to be 89.7% and that of word bigram model with add one smooothing was calculated to be 98.67%. Based on the 2 values, the word bigram model is a clear winner.
The 2 models can be used for different purposes. The letter bigram model uses less storage space so it can be used when there's a shortage of memory. But if there's a limited set of training data, then word bigram will be more useful, even though it uses more memory.

For spelling correction purposes, the letter n gram model would be more useful since it's robust to spelling differences.
The simples explanation for why the word bigram model works better in this case is that the three languages share the same script(similar alphabet), so they will contain common bigrams, but do not share many words(mostly share some nouns), so the word bigram model results in a near perfect accuracy and beats the letter bigram model with a good margin.