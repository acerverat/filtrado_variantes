#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Dec 2021

@author: cerverat

"""

import pandas as pd
import numpy as np
import argparse
import textwrap
import copy
import json
import csv
import sys 
import os

def parse_sections(my_file):
  header = ''
  genes = []
  my_positions = []
  is_header_line = True
  is_position_line = False
  is_gene_line = False
  is_sample_line = False
  sample_section_line = '], "samples":['
  gene_section_line = '],"genes":['
  end_line = ']}'
  pos = 0

  with open(my_file) as json_file:
    position_count = 0
    gene_count = 0
    for line in json_file:
      trim_line = line.strip()
      if is_header_line:
        ## only keep the "header" field content from the line
        header = trim_line[10:-14]
        is_header_line = False
        is_position_line = True
        continue
      if trim_line == gene_section_line:
        is_gene_line = True
        is_position_line = False
        continue
      else:
        if is_position_line:
          ## remove the trailing ',' if there is
          my_positions.append(trim_line.rstrip(','))
          position_count += 1
        if is_gene_line:
          ## remove the trailing ',' if there is
          genes.append(trim_line.rstrip(','))
          gene_count += 1

  #print ('header object:', header)
  sample = header.split('"samples":[')[1].strip(']}').strip('"')
  print ('number of positions:', position_count)
  print ('number of genes:', gene_count)
  print ("sample name:", sample)

  return(my_positions,sample,position_count)


def get_canonical(transcripts,col):
  myList = []
  for t in transcripts:
    if (t['source']=="RefSeq"):
      if 'isCanonical' in t:
        myList.append(t)
  #print(len(myList),myList)
  return(myList)

def order_columns(myColname,columns,pos,columnPos):
  #global pos 
  if myColname in columns:
    if columnPos[myColname] <= pos:
      columnPos[myColname] = pos
  else:
    columnPos[myColname] = pos 
    columns.append(myColname)
  pos=pos+1
  #print(myColname,pos)

def get_string(x):
  if type(x)==bool:
    if x:
      return "true"
    else:
      return "false"
  else:
    return str(x)

def un_nest(nested,col,myRow,my_dict,columns,pos,columnPos):
  new_dict = {}
  for f in nested:
    new_dict.update(f)
  for n in new_dict:
    colname=(col+"_"+n)

    if (colname=="v_gnomad"):
      myRow=un_nest([new_dict[n]],colname,myRow,my_dict,columns,pos,columnPos)
      
    elif (colname=="v_regulatoryRegions"):
      myRow=un_nest(new_dict[n],colname,myRow,my_dict,columns,pos,columnPos)
    
    elif (colname=="v_clinvar"):
      myRow=un_nest(new_dict[n],colname,myRow,my_dict,columns,pos,columnPos)
    
    elif (colname=="v_transcripts"):
      saved_row=copy.deepcopy(my_dict[myRow])
      refseq_list=get_canonical(new_dict[n],colname)
      for i in range(len(refseq_list)):
        my_dict[myRow]=copy.deepcopy(saved_row)
        myRow=un_nest([refseq_list[i]],colname,myRow,my_dict,columns,pos,columnPos)
        myRow=myRow+1
    
    else:
      my_dict[myRow].append({colname:get_string(new_dict[n])})
      #print(colname,get_string(new_dict[n]),type(get_string(new_dict[n])))
      order_columns(colname,columns,pos,columnPos)
  return myRow


def parse_positions(my_positions,my_dict,row):      

  columnPos={}
  columnPos={"Rows":0}

  for position in my_positions:
    my_dict[row]=[]
    #print(position)
    position_dict = json.loads(position)
    pos = 1
    for field in position_dict:
      if field=='samples':
        row=un_nest(position_dict[field],'s',row,my_dict,columns,pos,columnPos)
      else:
        if field=='variants':
          tmp=row
          row=un_nest(position_dict[field],'v',row,my_dict,columns,pos,columnPos)
        else:
          #print(field,row,len(my_dict))
	  #error en esta linea cuando no se corre con python3
          my_dict[row].append({field:get_string(position_dict[field])})
          order_columns(field,columns,pos,columnPos)
    row=row+1

  sorted_columns=dict(sorted(columnPos.items(), key=lambda item: item[1]))
  return(sorted_columns)

def write_outfile(sample,cols,my_dict,my_filename):

  a_file = open(my_filename, "w",newline='')
  writer = csv.writer(a_file,delimiter='\t',lineterminator=os.linesep)

  my_cols=list(cols.keys())
  my_cols.insert(1,"muestra")
  writer.writerow(my_cols[0:])

  df = pd.DataFrame(columns = my_cols)

  for key, value in my_dict.items():
    line=[]
    for c in my_cols: 
      a=[d[c] for d in value if c in d]
      if (len(a)>0):
        line.append(*a)
      else:
        line.append(np.nan)
    line.insert(1,sample)
    writer.writerow(line)

  a_file.close()
  return a_file


if __name__ == "__main__":
  
  positions = []
  columns = []
  row = 0
  pos_dict={}
  sample=""

  #not necessary can be extracted from header 
  #sampleId = sys.argv[1]
  input_file = sys.argv[1]
  outDir = sys.argv[2]
  
  #extract from the file the section with the variants and the sample name
  positions,sample,count = parse_sections(input_file)

  if (count<1): 
      print("No se detectaron variantes en ",sample)
      exit
  else:
    #transform the json format to dictionary format and get the columns for the final file
    colnames = parse_positions(positions,pos_dict,row)

    #write the variants in tab delimited format
    out_filename = outDir+"/"+sample+"_full.tsv"
    print("Output file:",out_filename)

    write_outfile(sample,colnames,pos_dict,out_filename)
