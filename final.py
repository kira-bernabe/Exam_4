#!/usr/bin/env python3

#kmers are substrings of a string with kmer length of k, as in BANANA, kmer length k = 2: BA NA NA
#string slicing: getting multiple letters from a string at once, 
#for instance, s[2:4] will give a slice of the string, starting at index 2 and going up to, but not including, index 4.
#uses colon notation
import pandas as pd

import argparse

#Q1: define a function to count kmers of size k, where k is specified as an argument
#first for observed kmers:

def count_kmers_observed(read, k):
    counts = {}
    num_kmers = len(read) - k + 1 #length of the read minus k size plus 1
    for i in range (num_kmers):
        kmer= read[i:i+k] #slicing the string
        if kmer not in counts:
          counts[kmer] = 0
        counts[kmer] +=1
    return counts
  
  #read = 'ATTTGGATT'
  #k = args.k
  
 # print(len(count_kmers_observed(read, 9)))
  
def count_poss(read, k):
  counts = {}
  num_kmers1 = len(read) - k + 1
  num_kmers2 = 4**k
  num_kmers = min(num_kmers1,num_kmers2)
  print(num_kmers)

read = 'ATTTGGATT'

count_poss(read, 9)

read = input("Enter read: ")
print(read)

k= int(input("Enter k: "))


def count_kmers_observed(read, k):
  counts = {}
  num_kmers = len(read) - k + 1
  for i in range (num_kmers):
    kmer= read[i:i+k]
  if kmer not in counts:
    counts[kmer] = 0
  counts[kmer] +=1
  return counts
  
#print(len(count_kmers_observed(read, k)))

#second function for possible kmers
#because we only have 4 characters, the number of possible kmers is 4^k

def count_kmers_possible(read, k):
  num_kmers = {} #empty dictionary start from nothing and add
  num_kmers1 = len(read) - k + 1 #number of kmers of length k
  num_kmers2 = 4**k #calculate possible kmers
  num_kmers = min(num_kmers1,num_kmers2) #can be either but actual possible kmers is smaller value
  num_kmers3 = max(num_kmers,0) #so that k won't be less than 1
  return(num_kmers3)

#Q2 define a function to create a pandas data frame containing all possible k
#and the associated number of observed and expected kmers

def create_panda(read):
  k_values = [] #first column is number of k's, make an empty list to append to
  for i in range(1,len(read)+1): #loops through the length of the read, since len() doesn't include the last number in the range, add 1
    k_values.append(i)
  observed_kmers = [] #second column is observed kmers, empty list
  for i in k_values: #loops through each value of k and get the observed kmers from the count_kmers_observed function
    observed_kmers.append(len(count_kmers_observed(read, i)))
  possible_kmers = [] #third column: possible kmers
  for i in k_values:
    possible_kmers.append(count_kmers_possible(read, i))#another loop
  df = pd.DataFrame(list(zip(k_values, observed_kmers, possible_kmers)), columns = ['k','Observed kmers','Possible kmers'])
  df.at['Total', 'Observed kmers'] = df['Observed kmers'].sum() #add total observed kmer value
  df.at['Total', 'Possible kmers'] = df['Possible kmers'].sum() #add total possible kmer value
  return df
  
  #Q3 define a function to calculate linguistic complexity
  #linguistic complexity = o/p
#take totals from df and use them to calculate the LC
def calculate_LC(read):
  k_values = [] 
  for i in range(1,len(read)+1): 
    k_values.append(i) 
  observed_kmers = [] 
  for i in k_values: 
    observed_kmers.append(len(count_kmers_observed(read, i)))
  possible_kmers = [] 
  for i in k_values:
    possible_kmers.append(count_kmers_possible(read, i))
  df = pd.DataFrame(list(zip(k_values, observed_kmers, possible_kmers)), columns = ['k','Observed kmers','Possible kmers'])
  df.at['Total', 'Observed kmers'] = df['Observed kmers'].sum()
  df.at['Total', 'Possible kmers'] = df['Possible kmers'].sum()
  x = int(df.at['Total','Observed kmers']) #isolate the total for observed kmers and assign it to a variable x
  y = int(df.at['Total','Possible kmers']) #isolate the total for possible kmers and assign it to a variable y
  LC =  (x/y)
  return LC

#calculate_LC(read)

#Q4 Be sure that all your functions have appropriate docstrings

#Q5 Use the main function in your script to read in your file and output results to files


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('filename', type = str)
  args = parser.parse_args()
  main(args)


#Q6 Write a script to thoroughly test each of your functions

