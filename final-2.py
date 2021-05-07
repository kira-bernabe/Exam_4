#!/usr/bin/env python3

#kmers are substrings of a string with kmer length of k, as in BANANA, kmer length k = 2: BA NA NA
#string slicing: getting multiple letters from a string at once, 
#for instance, s[2:4] will give a slice of the string, starting at index 2 and going up to, but not including, index 4.
#uses colon notation

#read = 'ATTTGGATT'

import pandas as pd

import argparse

#Q1: define a function to count kmers of size k, where k is specified as an argument
#first for observed kmers:

def count_kmers_observed(read, k):
    counts = {} #this needs to be empty in order to start bulding the dictionary
    num_kmers = len(read) - k + 1 #length of the read minus k size plus 1
    for i in range (num_kmers):
        kmer= read[i:i+k] #slicing the string
        if kmer not in counts:
          counts[kmer] = 0
        counts[kmer] +=1
    return counts
  
#second function for possible kmers
#because we only have 4 characters, the number of possible kmers is 4^k

def count_kmers_possible(read, k):
  num_kmers = {} #empty dictionary: start from nothing and add
  num_kmers1 = len(read) - k + 1 #number of kmers of length k
  num_kmers2 = 4**k #calculate possible kmers
  num_kmers = min(num_kmers1,num_kmers2) #can be either but the actual possible kmers is smaller value
  num_kmers3 = max(num_kmers,0) #so that k won't have negative value
  return(num_kmers3)

#Q2 define a function to create a pandas data frame containing all possible k
#and the associated number of observed and expected kmers

#need a loop to go through each k and as the dataframe is being built:
def create_pandas(read):
  k_values = [] #first column is number of k's, make an empty list to append to
  for i in range(1,len(read)+1): #loops through the length of the read, since len() doesn't include the last number in the range, add 1
    k_values.append(i) #add to the list
  observed_kmers = [] #second column is observed kmers, again make an empty list
  for i in k_values: #loops through each value of k and gets the observed kmers from count_kmers_observed 
    observed_kmers.append(len(count_kmers_observed(read, i))) #add to the list
  possible_kmers = [] #third column: possible kmers
  for i in k_values:#last loop
    possible_kmers.append(count_kmers_possible(read, i)) #add to the list
  df = pd.DataFrame(list(zip(k_values, observed_kmers, possible_kmers)), columns = ['k','Observed kmers','Possible kmers']) #actual data frame
  df.at['Total', 'Observed kmers'] = df['Observed kmers'].sum() #append rows and use sum function to compute the sum of each column
  df.at['Total', 'Possible kmers'] = df['Possible kmers'].sum() #same as above #at function accesses single value for row/column label pair
  return df
  
#Q3 define a function to calculate linguistic complexity (LC)
#linguistic complexity = o/p
#take totals from df and use them to calculate the LC
#start with the loop and the dataframe and then assign variables to observed and possible (x and y respectively)
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
  x = int(df.at['Total','Observed kmers']) ##int function converts the specified value into an integer; in this case total the observed kmers and assign it to a variable x
  y = int(df.at['Total','Possible kmers']) #same as above -> assign to variable y
  LC =  (x/y)
  return LC

#calculate_LC(read)

#Q4 Be sure that all your functions have appropriate docstrings

#Q5 Use the main function in your script to read in your file and output results to files

if __name__ == '__main__':
  def main():
    with open("ling_comp.txt",'a+') as f: #use a+ to create and open a file (if it doesn't already exist) and to append and read 
      f.seek(0) #sets the reference point at the beginning of the file 
      data = f.read() #read the contents of the file to see if it contains information
      if len(data) >0 :
        f.write("\n")  #if file is not empty, append output in a new line
      LingComp = calculate_LC(read)
      f.write(str(LingComp)) #append the LC value
    pandas = create_pandas(read)
    pandas.to_csv('dataframe.csv', mode ='a+') #open and append to pandas dataframe
    
  main()


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-read') #put the read value here when the proram is run
  parser.add_argument('-k') #put the k value here  
  args = parser.parse_args() 
  read = args.read #read value comes from what the user enters
  k = int(args.k) #k value is converted to an integer from what the user enters



