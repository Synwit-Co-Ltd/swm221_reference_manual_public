# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SWM221 参考手册'
copyright = '2024, 广东华芯微特集成电路有限公司'
author = 'Synwit'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# tight-table
# https://knowyourtoolset.com/2018/02/controlling-the-width-of-a-table-with-read-the-docs/
def setup(app):
   app.add_css_file('css/custom.css')
   
extensions = ['sphinx.ext.autodoc',
    #'sphinx_markdown_tables',
    #'sphinx.ext.autosectionlabel',
    # 'sphinx.ext.doctest',
    # 'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    # 'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx_rtd_size',
    'linuxdoc.rstFlatTable',
    # 'docxbuilder',
    ]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'sphinx_rtd_theme'

html_show_sourcelink = True
html_static_path = ['_static']
html_css_files = ['css/custom.css', 'css/theme.css', 'css/theme_overrides.css']

# html_logo = '_static/logo.ico'

sphinx_rtd_size_width = "100%"

numfig = True
numfig_secnum_depth = 0
numfig_format = {'figure': '图 %s',
                 'table': '表格 %s',
                 'code-block': 'Listing %s',
                }

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
# 
# Add included files into the exclude_patterns array
# See https://github.com/sphinx-doc/sphinx/issues/9779
exclude_patterns = [
  '.vscode', 
  'system/存储器映射.rst',
  'blocks/*/functions.rst', 
  'blocks/*/regs_map.rst', 
  'blocks/*/regs_tables.rst', 
  'blocks/*/*tmp.rst',
  'blocks/*/ADC.rst',
  'blocks/*/CRC.rst',
  'blocks/*/DIV.rst',
  'blocks/*/DMA.rst',
  'blocks/*/MPU.rst',
  'blocks/*/QEI.rst',
  'blocks/*/WDT.rst',
  'blocks/*/USART.rst',
  'blocks/*/PWM.rst',
  'blocks/*/I2C.rst',
  'blocks/*/GPIO.rst',
  'blocks/*/PGA.rst',
  'blocks/*/NVIC.rst'
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# top-level file (index.rst)
# output file (manual.pdf)
rinoh_documents = [
  dict(doc='index', target='manual')  
]