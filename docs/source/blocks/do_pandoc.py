import os
import sys
import subprocess
import re
import shutil
import time

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('docx_filename', help='docx filename')
parser.add_argument('-o', '--out', dest='rst_filename', help='rst filename')

args = parser.parse_args()
print(args)

docx_filename = args.docx_filename
if args.rst_filename == None:
  rst_filename = docx_filename.split('.')[0] + '.rst'
else:
 rst_filename = args.rst_filename

# generate with list table, and with make file setup
# > rstfromdocx -lurg <docx filename>
#

# pandoc --list-tables -o output.rst <docx filename>.docx

print(f'Generate {rst_filename} from {docx_filename} with pandoc')
prog = ['pandoc', '--list-tables', '-o',  f'{rst_filename}', f'{docx_filename}']

retcode = subprocess.call(prog)
print('pandoc return code %d\n' % retcode)

if retcode != 0:
  print('Error, abort!')
  sys.exit(-1)