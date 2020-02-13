#!/usr/bin/env python3
# utf-8 tab space:2  
#%matplotlib inline
import matplotlib.pyplot as plt
import math
import numpy as np
import copy
from graphviz import Digraph

import draw
import trans

def add_mark(table, mark):
  tables = []
  for i in range(9):
    #work_table = table
    work_table = copy.deepcopy(table)
    if work_table[i] == 0:
      work_table[i] = mark
      tables += [work_table]
      continue
  return tables

#https://note.nkmk.me/python-list-unique-duplicate/
def get_unique_list(seq):
  seen = []
  return [x for x in seq if x not in seen and not seen.append(x)]

def add_mark(table, mark):
  tables = []
  fin_tables = []
  for i in range(9):
    #work_table = table
    work_table = copy.deepcopy(table)
    if work_table[0][i] == 0:
      work_table[0][i] = mark
      tables += [work_table]
      if check_fin(work_table[0])==3-2*mark:
        fin_tables += [work_table]
      continue

  if len(fin_tables)==0:
    return tables
  else :
    return fin_tables

def add_mark2(table, mark):
  tables = []
  fin_tables = []
  for i in range(9):
    #work_table = table
    work_table = copy.deepcopy(table)
    if work_table[0][i] == 0:
      work_table[0][i] = mark
      tables += [work_table]
      if check_fin(work_table[0])==3-2*mark:
        fin_tables += [work_table]
      continue

  if len(fin_tables)==0:
    fined_tables = []
    
    if mark == 1:
      a_mark = 2
    else :
      a_mark = 1

    for i in range(9):
      work_table = copy.deepcopy(table)
      if work_table[0][i] == 0:
        work_table[0][i] = a_mark
        if check_fin(work_table[0]) == 3-2*a_mark:
          work_table = copy.deepcopy(table)
          work_table[0][i] = mark
          fined_tables += [work_table]
    
    if len(fined_tables)==0:
      return tables
    else :
      return fined_tables
  else:
    return fin_tables

def add_mark3(table, mark):
  tables = []
  fin_tables = []
  for i in range(9):
    #work_table = table
    work_table = copy.deepcopy(table)
    if work_table[0][i] == 0:
      work_table[0][i] = mark
      tables += [work_table]
      if check_fin(work_table[0]) == 3-2*mark:
        fin_tables += [work_table]
      continue

  if len(fin_tables)==0:
    fined_tables = []
    
    if mark == 1:
      a_mark = 2
    else :
      a_mark = 1

    for i in range(9):
      work_table2 = copy.deepcopy(table)
      if work_table2[0][i] == 0:
        work_table2[0][i] = a_mark
        if check_fin(work_table2[0])==3-2*a_mark:
          work_table3 = copy.deepcopy(table)
          work_table3[0][i] = mark
          fined_tables += [work_table3]
    
    if len(fined_tables)==0:
      will_fin_tables = []

      for i in range(9):
        work_table4 = copy.deepcopy(table)
        if work_table4[0][i] == 0:
          work_table4[0][i] = mark
          for j in range(9):
            work_table5 = copy.deepcopy(work_table4)
            if work_table5[0][j] == 0:
              work_table5[0][j] = mark
              if check_fin(work_table5[0])==3-2*mark:
                #print(table[0],"=>",work_table5[0])
                work_table6 = copy.deepcopy(table)
                work_table6[0][i] = mark
                will_fin_tables += [work_table6]
      
      if len(will_fin_tables)==0:
        return tables
      else :
        #print(will_fin_tables)
        return will_fin_tables
    else :
      return fined_tables
  else:
    return fin_tables

def add_mark4(table, mark):
  tables = []
  fin_tables = []
  for i in range(9):
    #work_table = table
    work_table = copy.deepcopy(table)
    if work_table[0][i] == 0:
      work_table[0][i] = mark
      tables += [[work_table[0],work_table[1]]]
      if check_fin(work_table[0])==3-2*mark:
        fin_tables += [[work_table[0],work_table[1]]]
      continue

  if len(fin_tables)==0:
    fined_tables = []
    
    if mark == 1:
      a_mark = 2
    else :
      a_mark = 1

    for i in range(9):
      work_table2 = copy.deepcopy(table)
      if work_table2[0][i] == 0:
        work_table2[0][i] = a_mark
        if check_fin(work_table2[0])==3-2*a_mark:
          work_table3 = copy.deepcopy(table)
          work_table3[0][i] = mark
          fined_tables += [[work_table3[0],work_table3[1]]]
    
    if len(fined_tables)==0:
      will_fin_tables = []
      will_2fin_tables = []

      if mark == 1:
        a_mark = 2
      else :
        a_mark = 1

      for i in range(9):
        work_table4 = copy.deepcopy(table)
        if work_table4[0][i] == 0:
          work_table4[0][i] = mark
          for j in range(9):
            work_table5 = copy.deepcopy(work_table4)
            if work_table5[0][j] == 0:
              work_table5[0][j] = mark
              if check_fin(work_table5[0]) == 3-2*mark:
                #print(table[0],"=>",work_table5[0])
                work_table6 = copy.deepcopy(table)
                work_table6[0][i] = mark
                will_fin_tables += [[work_table6[0],work_table6[1]]]
              
              work_table5[0][j] = a_mark
              for k in range(9):
                work_table7 = copy.deepcopy(work_table5)
                if work_table7[0][k] == 0:
                  work_table7[0][k] = mark
                  if check_fin(work_table7[0]) == 3-2*mark:
                    work_table8 = copy.deepcopy(table)
                    work_table8[0][i] = mark
                    will_2fin_tables += [[work_table8[0],work_table8[1]]]
      
      if len(will_2fin_tables)==0 and len(will_fin_tables)==0:
        return tables
      elif len(will_2fin_tables)==0:
        #print(will_fin_tables)
        return will_fin_tables
      else :
        return will_2fin_tables
    else :
      return fined_tables
  else:
    return fin_tables

def add_mark5(table, mark):
  tables = []
  fin_tables = []
  for i in range(9):
    #work_table = table
    work_table = copy.deepcopy(table)
    if work_table[0][i] == 0:
      work_table[0][i] = mark
      tables += [[work_table[0],work_table[1]]]
      if check_fin(work_table[0])==3-2*mark:
        fin_tables += [[work_table[0],work_table[1]]]
      continue

  if len(fin_tables)==0:
    fined_tables = []
    
    if mark == 1:
      a_mark = 2
    else :
      a_mark = 1

    for i in range(9):
      work_table2 = copy.deepcopy(table)
      if work_table2[0][i] == 0:
        work_table2[0][i] = a_mark
        if check_fin(work_table2[0])==3-2*a_mark:
          work_table3 = copy.deepcopy(table)
          work_table3[0][i] = mark
          fined_tables += [[work_table3[0],work_table3[1]]]
    
    if len(fined_tables)==0:
      will_fin_tables = []
      will_2fin_tables = []

      if mark == 1:
        a_mark = 2
      else :
        a_mark = 1

      for i in range(9):
        work_table4 = copy.deepcopy(table)
        if work_table4[0][i] == 0:
          work_table4[0][i] = mark
          for j in range(9):
            work_table5 = copy.deepcopy(work_table4)
            if work_table5[0][j] == 0:
              work_table5[0][j] = mark
              if check_fin(work_table5[0])==3-2*mark:
                #print(table[0],"=>",work_table5[0])
                flag = 1
                #check enemy double reach 
                for k in range(9):
                  work_table9 = copy.deepcopy(work_table5)
                  work_table9[0][j] = a_mark
                  if work_table9[0][k] == 0:
                    work_table9[0][k] = a_mark
                    if check_fin(work_table9[0])==3-2*a_mark:
                      work_table9[0][k] = mark
                      for l in range(9):
                        if work_table9[0][l] == 0:
                          work_table9[0][l] = a_mark
                          if check_fin(work_table9[0])==3-2*a_mark:
                            print(work_table9[0])
                            flag = 0
                
                if flag == 1:
                  work_table6 = copy.deepcopy(table)
                  work_table6[0][i] = mark
                  will_fin_tables += [[work_table6[0],work_table6[1]]]
              
              work_table5[0][j] = a_mark
              for k in range(9):
                work_table7 = copy.deepcopy(work_table5)
                if work_table7[0][k] == 0:
                  work_table7[0][k] = mark
                  if check_fin(work_table7[0])==3-2*mark:
                    work_table8 = copy.deepcopy(table)
                    work_table8[0][i] = mark
                    will_2fin_tables += [[work_table8[0],work_table8[1]]]
              


      
      if len(will_2fin_tables)==0 and len(will_fin_tables)==0:
          return tables
      elif len(will_2fin_tables)==0:
        return will_fin_tables
      else :
        return will_2fin_tables
    else :
      return fined_tables
  else:
    return fin_tables

def add_mark5b(table, mark):
  tables = []
  fin_tables = []
  for i in range(9):
    #work_table = table
    work_table = copy.deepcopy(table)
    if work_table[0][i] == 0:
      work_table[0][i] = mark
      tables += [[work_table[0],work_table[1]]]
      if check_fin(work_table[0]):
        fin_tables += [[work_table[0],work_table[1]]]
      continue

  if len(fin_tables)==0:
    fined_tables = []
    
    if mark == 1:
      a_mark = 2
    else :
      a_mark = 1

    for i in range(9):
      work_table2 = copy.deepcopy(table)
      if work_table2[0][i] == 0:
        work_table2[0][i] = a_mark
        if check_fin(work_table2[0]):
          work_table3 = copy.deepcopy(table)
          work_table3[0][i] = mark
          fined_tables += [[work_table3[0],work_table3[1]]]
    
    if len(fined_tables)==0:
      will_fin_tables = []
      will_2fin_tables = []

      if mark == 1:
        a_mark = 2
      else :
        a_mark = 1

      for i in range(9):
        work_table4 = copy.deepcopy(table)
        if work_table4[0][i] == 0:
          work_table4[0][i] = mark
          for j in range(9):
            work_table5 = copy.deepcopy(work_table4)
            if work_table5[0][j] == 0:
              work_table5[0][j] = mark
              if check_fin(work_table5[0]):
                #print(table[0],"=>",work_table5[0])
                work_table6 = copy.deepcopy(table)
                work_table6[0][i] = mark
                will_fin_tables += [[work_table6[0],work_table6[1]]]
              
              work_table5[0][j] = a_mark
              for k in range(9):
                work_table7 = copy.deepcopy(work_table5)
                if work_table7[0][k] == 0:
                  work_table7[0][k] = mark
                  if check_fin(work_table7[0]):
                    work_table8 = copy.deepcopy(table)
                    work_table8[0][i] = mark
                    will_2fin_tables += [[work_table8[0],work_table8[1]]]
      
      if len(will_2fin_tables)==0 and len(will_fin_tables)==0:
        will_2fined_tables = []

        if mark == 1:
          a_mark = 2
        else :
          a_mark = 1

        for i in range(9):
          work_table9 = copy.deepcopy(table)
          if work_table9[0][i] == 0:
            work_table9[0][i] = a_mark
            for j in range(9):
              work_table10 = copy.deepcopy(work_table9)
              if work_table10[0][j] == 0:
                work_table10[0][j] = a_mark
                if check_fin(work_table10[0]):
                  work_table10[0][j] = mark
                  for k in range(9):
                    work_table11 = copy.deepcopy(work_table10)
                    if work_table11[0][k] == 0:
                      if check_fin(work_table11[0]):
                        work_table11 = copy.deepcopy(table)
                        work_table11[0][i] = mark
                        will_2fined_tables += [[work_table11[0],work_table11[1]]]
          
          if len(will_2fined_tables)==0:
            return tables
          else:
            return will_2fined_tables

      elif len(will_2fin_tables)==0:
        return will_fin_tables
      else :
        return will_2fin_tables
    else :
      return fined_tables
  else:
    return fin_tables

def check_fin(table):
  
  tableline = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  
  for line in tableline:
    for value in range(1,3):
      #print(value,",",table[line[0]],",",table[line[1]],",",table[line[2]])
      if table[line[0]] == value and table[line[1]] == value and table[line[2]] == value:
        return 3-2*value
  return 0


if __name__ == '__main__':

  mode = 0

  if mode == 0:
    first_table = [[0,0,0,0,0,0,0,0,0],0,0]
    #first_table = [[0,0,0,0,1,0,0,0,2],trans.table2num([0,0,0,0,1,0,0,0,2]),0]
    #first_table = [[1,0,0,0,1,0,2,0,2],trans.table2num([1,0,0,0,1,0,2,0,2]),0]
  elif mode == 1:
    first_table = [[0,0,0,0,1,0,0,0,0],trans.table2num([0,0,0,0,1,0,0,0,0]),0]
    #first_table = [[0,0,0,0,0,0,0,0,1],trans.table2num([0,0,0,0,0,0,0,0,1]),0]

  l=[]
  map_link = []
  tables = []
  tables = add_mark(first_table,1+mode)
  #print("first:",tables)
  fin_tables = []
  history_tables = [] 
  history_tables += [[first_table[0],1,0,0]]

  fig = plt.figure(figsize=(1,1),dpi=50)
  num = trans.table2num(first_table[0])
  draw.draw_board(fig,1,1,1,num)
  name = format("figure"+str(num)+".png")
  #print(name)
  plt.savefig(name)
  plt.clf()
  plt.close()

  for i in range(mode,9):
    l = []
    for table in tables:
      
      work_rotate = trans.rotate_table(table[0])
      work_rotate2 = trans.rotate2_table(table[0])
      work_rotate3 = trans.rotate3_table(table[0])

      transs = [table[0],
            work_rotate,
            work_rotate2,
            work_rotate3,
            trans.reverse_v_table(table[0]),
            trans.reverse_v_table(work_rotate),
            trans.reverse_v_table(work_rotate2),
            trans.reverse_v_table(work_rotate3),
            trans.reverse_h_table(table[0]),
            trans.reverse_h_table(work_rotate),
            trans.reverse_h_table(work_rotate2),
            trans.reverse_h_table(work_rotate3)]

      min_t = 123456
      for tra in transs:  
        num = trans.table2num(tra)
        if min_t > num:
          min_t = num

      map_link += [[min_t,table[1]]]
      l+=[min_t]

    print(i+1," turn end:",set(l))

    result_tables = []
    for tab in set(l):
      fig = plt.figure(figsize=(1,1),dpi=50)
      draw.draw_board(fig,1,1,1,tab)
      name = format("figure"+str(tab)+".png")
      #print(name)
      plt.savefig(name)
      plt.clf()
      plt.close()
      work = trans.num2table(tab)
      
      won = check_fin(work)
      if  won != 0:
        fin_tables += [[tab,i,won]]
        count_up=1
      else:
        result_tables += [[work,tab]]
        count_up=0

      history_tables += [[work,i,won,count_up]]

    #print("result_tables => ",result_tables)
    #print("fin_tables(len=",len(fin_tables),") => ",fin_tables)
    
    tables = []
    for result_table in result_tables:
      tables += add_mark(result_table,(i+1)%2+1)
      #tables += add_mark3(result_table,(i)%2+1)
      
    #history_tables += tables

  #print(map_link)    

  print("num:",len(history_tables))

  for i in range(9, 0, -1):
    for node in history_tables:
      if node[1] == i: 
        tab = trans.table2num(node[0])
        for link in get_unique_list(map_link):
          if link[0] == tab:
            for target in history_tables:
              tab2 = trans.table2num(target[0])
              if tab2 == link[1]:
                target[2] += node[2] 
                target[3] += 1
    
    for node in history_tables:
      if node[1] == i-1 and node[3] !=0:
        node[2] = node[2] / node[3]


  targets=[]

  for node in history_tables:
      if node[1] == 1:
        targets += [node]

  for i in range(1, 8):
    min_p = 10
    max_p =-10
    min_target =[]
    max_target =[]

    for node in targets: 
      tab = trans.table2num(node[0])
      for link in get_unique_list(map_link):
        if link[1] == tab:
          for target in history_tables:
            tab2 = trans.table2num(target[0])
            if tab2 == link[0]:

              if i%2==(mode+1)%2 and min_p > target[2]:
                min_target = target
                min_p = target[2]

              if i%2==mode%2 and max_p < target[2]:
                max_target = target
                max_p = target[2]

    if i%2==(mode+1)%2:
      targets = [min_target]
    else :
      targets = [max_target]
    print(targets)
    
    if len(targets)==0:
      break


  #for target in fin_tables:
  #  wp = target[2]/2.0
  #  for link in get_unique_list(map_link):
  #    if(link[0] == target[0]):
  #      for nodes in history_tables:
  #        tab = trans.table2num(nodes[0])
  #        if tab == link[1]:
  #          nodes[2] += wp



  #fig = plt.figure(figsize=(4,4),dpi=50)
  #for i in range(15):
  #  draw_board(fig,4,4,i+1,table2num(result_tables[i]))

  # Create Digraph object
  dot = Digraph()

  dot.attr('node', shape='box')
  dot.attr('node', width='1.0')
  dot.attr('node', height='1.0')
  #dot.attr('graph', layout='circo')

  # Add nodes

  for nodes in history_tables:
    #print(nodes)
    tab = trans.table2num(nodes[0])
    name = format("figure"+str(tab)+".png")
    #print(nodes)
    dot.node(str(tab),label=str(nodes[2]),image=name)
    #dot.node(str(tab))

  # Add edges
  work_list = get_unique_list(map_link)

  for link in work_list:
    #print(str(link[1]),",",str(link[0]))
    dot.edge(str(link[1]),str(link[0]))

  # Visualize the graph
  dot

  dot.format = 'png'

  dot.view()