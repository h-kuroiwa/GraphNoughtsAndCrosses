#!/usr/bin/env python3
# utf-8 tab space:2 

import math

def table2num(table):
  ans = 0
  for i in range(9):
    ans+=table[9-i-1]*(3**i)
  return ans

def num2table(num):
  table = []
  work = num
  for i in range(9):
    table +=[math.floor(work/(3**(9-i-1)))]
    work = work % (3**(9-i-1))  
  return table

def trans_table(table,trans):
  result = []
  for i in range(9):
    result +=[table[trans[i]]]  
  
  return result

def rotate_table(table):
  result = []
  trans=[6,3,0,7,4,1,8,5,2]
  for i in range(9):
    result +=[table[trans[i]]]  
  
  return result

def rotate2_table(table):
  result = []
  trans = [8, 7, 6, 5, 4, 3, 2, 1, 0]
  for i in range(9):
    result +=[table[trans[i]]]  
  
  return result

def rotate3_table(table):
  result = []
  trans = [2, 5, 8, 1, 4, 7, 0, 3, 6]
  for i in range(9):
    result +=[table[trans[i]]]  
  
  return result

def reverse_v_table(table):
  result = []
  trans=[6,7,8,3,4,5,0,1,2]
  for i in range(9):
    result +=[table[trans[i]]]  
  
  return result

def reverse_h_table(table):
  result = []
  trans=[2,1,0,5,4,3,8,7,6]
  for i in range(9):
    result +=[table[trans[i]]]  
  
  return result

if __name__ == '__main__':

  table=[2,0,0,
         0,0,0,
         0,0,1,]

  work_table = table 
  print(work_table)

  work_table = table
  work_table = rotate_table(work_table)
  print(work_table)

  work_table = table
  work_table = rotate2_table(work_table)
  print(work_table)

  work_table = table
  work_table = rotate3_table(work_table)
  print(work_table)

  work_table = table
  work_table = reverse_v_table(work_table)
  print(work_table)

  work_table = table
  work_table = reverse_h_table(work_table)
  print(work_table)