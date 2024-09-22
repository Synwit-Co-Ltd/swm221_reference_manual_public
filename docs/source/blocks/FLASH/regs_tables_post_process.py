
import os
import sys
import subprocess
import re
import shutil
import time

shutil.copy('regs_tables.rst', 'regs_tables_tmp.rst')

with open('regs_tables.rst', 'r', encoding='utf-8') as fin:
  lines = fin.readlines()

start_pos = None
stop_pos = None

for i, line in enumerate(lines):  
  # print(line, end='')
  search_item = 'CFG0寄存器'
  if search_item == lines[i].strip() and '^^^^^^^^^^' in lines[i+1].strip():
    print(f'Found: {search_item} at line {i}')
    start_pos = i

for i, line in enumerate(lines):  
  # print(line, end='')
  search_item = 'STAT寄存器'
  if search_item == lines[i].strip() and '^^^^^^^^^^' in lines[i+1].strip():
    print(f'Found: {search_item} at line {i}')
    stop_pos = i

with open('regs_tables_tmp.rst', 'r', encoding='utf-8') as fin:
  lines = fin.readlines()

total_lines = len(lines)

if start_pos == None or stop_pos == None:
  print('Unable to find lines to be removed')
else:  
  with open('regs_tables.rst', 'w', encoding='utf-8') as fout:
    for i in range(0, start_pos):
      fout.write(lines[i])

    for i in range(stop_pos, total_lines):
      fout.write(lines[i])
    