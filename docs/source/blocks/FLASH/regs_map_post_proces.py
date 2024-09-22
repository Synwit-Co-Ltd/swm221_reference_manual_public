
import os
import sys
import subprocess
import re
import shutil
import time

shutil.copy('regs_map.rst', 'regs_map_tmp.rst')

with open('regs_map.rst', 'r', encoding='utf-8') as fin:
  lines = fin.readlines()

start_pos = None
stop_pos = None

for i, line in enumerate(lines):  
  # print(line, end='')
  search_item = 'CFG0'
  if search_item in lines[i].strip():
    print(f'Found: {search_item} at line {i}')
    start_pos = i

for i, line in enumerate(lines):  
  # print(line, end='')
  search_item = 'STAT'
  if search_item in lines[i].strip():
    print(f'Found: {search_item} at line {i}')
    stop_pos = i

with open('regs_map_tmp.rst', 'r', encoding='utf-8') as fin:
  lines = fin.readlines()

total_lines = len(lines)

with open('regs_map.rst', 'w', encoding='utf-8') as fout:
  for i in range(0, start_pos):
    fout.write(lines[i])

  for i in range(stop_pos, total_lines):
    fout.write(lines[i])
    