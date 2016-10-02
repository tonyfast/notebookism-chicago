
# coding: utf-8

# In[9]:

from glob import glob
from toolz.curried import *
import nbformat
from whatever import *


# In[52]:

the_tests = {
    the_test: nbformat.read(the_test, nbformat.NO_CONVERT)
    for the_test in glob('tests/*.ipynb')
}


# In[60]:

for the_notebook in glob('notebookism/*.ipynb'):
    notebook = nbformat.read(the_notebook, nbformat.NO_CONVERT)
    the_test = the_notebook.replace('notebookism/', 'tests/test-')
    if not (the_test in the_tests):
        the_tests[the_test] = notebook.copy()
        the_tests[the_test]['cells'] = []
        del the_tests[the_test]['metadata']['anaconda-cloud']

    tests = (__x(notebook['cells']).pluck('source')
             + _this().startswith('"""')._
             > list
             )
    new_cells = __x(tests).filter(
        complement(
            lambda x: x in __x(the_tests[the_test][
                'cells']).pluck('source').__()
        )
    ).map(nbformat.v4.new_code_cell) > list
    if new_cells:
        the_tests[the_test]['cells'].extend(new_cells)
        nbformat.write(the_tests[the_test], the_test)
