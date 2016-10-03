
``notebookism``
===============

A talk for the PyData Chicago meetup

Installation
------------

``pip install notebookism-chicago``

|Binder|

.. |Binder| image:: http://mybinder.org/badge.svg
   :target: http://mybinder.org:/repo/tonyfast/notebookism-chicago

Links
=====

-  `Github <https://github.com/tonyfast/notebookism-chicago>`__
-  `Binder <http://mybinder.org/repo/tonyfast/notebookism-chicago>`__
-  `NbViewer <http://nbviewer.jupyter.org/github/tonyfast/notebookism-chicago/tree/master/>`__
-  Anaconda.org

   -  `notebook <https://anaconda.org/tonyfast/test-readme/notebook>`__
   -  `presentation <https://anaconda.org/tonyfast/test-readme/notebook/format/presentation>`__

-  `travis-ci <https://travis-ci.org/tonyfast/notebookism-chicago>`__
-  `pypi <https://pypi.python.org/pypi/notebookism-chicago>`__

Development
===========

Running the Build and Tests
---------------------------

.. code:: bash

    pip install -r requirements-dev.txt
    python setup.py develop
    watchmedo tricks tricks.yaml

The ``watchmedo`` script will convert your notebooks to scripts and html
files. ``py.test-ipynb`` will test all notebooks matching
``test-*.ipynb``.

Running the docs
----------------

.. code:: bash

    jekyll serve docs -wit

Docs are hosted at ``http://localhost:4000/notebookism-chicago/``.

License
-------

``notebookism`` is released as free software under the `BSD 3-Clause
license <https://github.com/tonyfast/whatever-forever/blob/master/LICENSE>`__.
