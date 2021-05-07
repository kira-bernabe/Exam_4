#!/usr/bin/env python3

#Q6 Write a script to thoroughly test each of your functions

'''
Begin with a test to make sure the appropriate characters are in the string
'''
#give erros if the parameters are not met
read = "ATTTGGATT"
k = 9  

import re
import sys
if not re.match("^[c('A','C','T','G')]*$", read):
    print("Error: character not recognized")
    sys.exit()
    
if k > len(read):
    print("Error: k is longer than read length")
    sys.exit()
    
    
'''
Test the function that outputs the observed kmers 
'''
#use the assert function to test of the condition will return as "true"
read = "ATTTGGATT"
k = 9  

def test_count_kmers_observed()    
  actual_result = count_kmers_observed(read, k)
  expected_result = 1
  assert actual_result == expected_result
  
'''
Test the function that outputs the possible kmers 
'''

read = "ATTTGGATT"
k = 9  

def test_count_kmers_possible()
  actual_result = count_kmers_possible(read, k)
  expected_result = 1
  assert actual_result = expected_result

'''
Test to comnpare the data frame that was created with pandas to the original table in the assignment
'''

#cannot use assert function for data frames, must use .eq to compare tables 

read = "ATTTGGATT"
k = 9  

def test_create_pandas_df()
  actual_result = create_pandas(read)
  expected_result = pd.DataFrame(list(zip([1,2,3,4,5,6,7,8,9], [3,5,6,6,5,4,3,2,1], [4,8,7,6,5,4,3,2,1])), columns = ['k','Observed kmers','Possible kmers']) #original table
  expected_result.at['Total', 'observed kmers'] = expected_result['observed kmers'].sum() #dataframe created with pandas
  expected_result.at['Total', 'possible kmers'] = expected_result['possible kmers'].sum() #same as above
  create_panda(read).eq(expected_result) 
  
  '''
  Test the function to calculate linguistic complexity 
  '''

def test_calculate_LC():
  actual_result = calculate_LC(read) 
  expected_result = 0.875
  assert actual_result == expected_result 
 
