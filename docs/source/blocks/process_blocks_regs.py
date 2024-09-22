import os
import sys
import subprocess
import re
import shutil
import time


blocks = [
  'ADC',
  'BTIMER',
  'CAN',
  'CMP',
  'CRC',
  'DIV',
  'DMA',
  'FLASH',
  'GPIO',
  'I2C',
  'MPU',
  'PGA',
  'PORTCON',
  'PWM',
  'QEI',
  'QSPI',
  'SPI',
  'SYSCON',
  'TIMER',
  'UART',
  'USART',
  'WDT',
]

for i, block_name in enumerate(blocks):
  docx_filename = f'{block_name}\{block_name}_regs_map.docx'
  rst_filename = f'{block_name}\\regs_map.rst'
  prog = ['python', 'extract_regs_map.py', docx_filename, rst_filename]

  retcode = subprocess.call(prog)
  print('return code %d\n' % retcode)

  if retcode != 0:
    print('Error, abort!')
    sys.exit(-1)

  docx_filename = f'{block_name}\{block_name}_regs_tables.docx'
  rst_filename = f'{block_name}\\regs_tables.rst'
  prog = ['python', 'extract_regs_tables.py', docx_filename, rst_filename]

  retcode = subprocess.call(prog)
  print('return code %d\n' % retcode)

  if retcode != 0:
    print('Error, abort!')
    sys.exit(-1)
  