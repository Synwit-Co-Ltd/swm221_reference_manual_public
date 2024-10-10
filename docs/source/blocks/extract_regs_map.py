from docx import Document
from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph
import re

from argparse import ArgumentParser


def iter_block_items(parent):
    """
    Generate a reference to each paragraph and table child within *parent*,
    in document order. Each returned value is an instance of either Table or
    Paragraph. *parent* would most commonly be a reference to a main
    Document object, but also works for a _Cell object, which itself can
    contain paragraphs and tables.
    """
    if isinstance(parent, _Document):
        parent_elm = parent.element.body
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    elif isinstance(parent, _Row):
        parent_elm = parent._tr
    else:
        raise ValueError("something's not right")
    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)

#--------------------------------------------------------------------------------------------------
parser = ArgumentParser()

parser.add_argument('docx_filename', help='filename of docx with tables')
parser.add_argument('rst_out_filename', help='rst output filename' )

args = parser.parse_args()
print(args)
doc = Document(args.docx_filename)
print(f'Number of tables = {len(doc.tables)}')

fid = open(args.rst_out_filename, 'w', encoding="utf-8")
table_caption = ""

doc_name = args.docx_filename.split('.')[0]

for block in iter_block_items(doc):
  if isinstance(block, Paragraph):
    table_caption = block.text
  elif isinstance(block, Table):
    table = block
    print(f'Processing {table_caption.strip()}')

    fid.write(f'.. ' + '-'*100 + '\n\n')

    section_name = f'{table_caption.strip()}'
    # if section_name != '':
    #  fid.write(f'{section_name}\n')
    #  fid.write('-'*int(2.5*len(section_name)) + '\n\n')  

    fid.write(f'.. flat-table::\n')
    fid.write(f'   :header-rows: 1\n') 
    fid.write(f'   :class: tight-table-reg-map\n')
    # fid.write(f'   :widths: 12 9 6 10 33\n')
    fid.write(f'\n')

    for row in table.rows:

      prev_cell_tc = None
      entry_indent = ''

      for cell in row.cells:

        tc = cell._tc
        if prev_cell_tc == None:
          entry_indent = f'   * '
        else:
          entry_indent = f'     '
          if tc.left == prev_cell_tc.left:
            continue

        prev_cell_tc = tc  

        text = cell.text.split('\n')
        
        cspan = ''
        col_span = tc.right - tc.left - 1
        if col_span > 0:
           cspan = f':cspan:`{col_span}` '

        if len(text) == 1:
          cell_text = entry_indent + '- ' + f'{cspan}{text[0].strip()}\n'
        else:
          if cspan != '': 
            cell_text = entry_indent + '- ' + f'{cspan}\n\n'
            entry_indent = ' '*len(entry_indent)
            for t in text:
              cell_text = cell_text + entry_indent + '  ' + f'{t}\n\n'
          else:
            cell_text = entry_indent + '- ' + f'{text[0].strip()}\n\n'
            entry_indent = ' '*len(entry_indent)
            for t in text[1:]:
              cell_text = cell_text + entry_indent + '  ' + f'{t}\n\n'

        fid.write(cell_text + '\n')        
        print(cell_text, end='')
       

    fid.write('\n\n')    
    # break

fid.close()