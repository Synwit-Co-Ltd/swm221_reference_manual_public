# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SWM221 参考手册'
copyright = '2024, 广东华芯微特集成电路有限公司'
author = 'Synwit'
release = '1.0'

release = '0.1'
version = '0.1.0'

# -- General configuration

# tight-table
# https://knowyourtoolset.com/2018/02/controlling-the-width-of-a-table-with-read-the-docs/
def setup(app):
   app.add_css_file('css/custom.css')

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx_rtd_size',
    'linuxdoc.rstFlatTable',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

sphinx_rtd_size_width = "100%"

html_show_sourcelink = True
html_static_path = ['_static']
html_css_files = ['css/custom.css', 'css/theme.css', 'css/theme_overrides.css']

# -- Options for EPUB output
epub_show_urls = 'footnote'
