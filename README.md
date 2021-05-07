# Exam_4
A string is a sequence of characters that can be divided into substrings of length k, called k-mers. The linguistic complexity of the string is defined as observed k-mers divided by possible k-mers.  The following script assesses the number of observed and possiblek-mers for a string of any length that only contains the characters "A,T,G, and C", and its linguistic complexity. 

Run the script as python3 final.py -read ATTTGGATT -k 9 in the command line. The first two functions will count the observed k-mers and the possible k-mers. The next function will generate a data frame that organizes the data into a table with 3 columns: k, observed k-mers, and possible k-mers. The final function will calculate the linguistic complexity. Running the script will generate a text file for the linguistic complexity and a csv for the data frame. 

This script can be used to assess a string of any length as long as the user specifies the sequence (-read) and the length of the k-mer (-k). 

The script can be tested with py.test (test_final.py).

