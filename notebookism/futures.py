# coding: utf-8

# # Putting it all together <small>Part 3</small>
#
# ---
#
# The notebook, my machine, and its many artifacts.

# In[5]:

if __name__ is '__main__':
    from notebookism import env, iframe, refs, get_
else:
    from .utils import env, iframe, refs
    from .currents import get_


from whatever import *
from toolz.curried import *
import envoy
import ipywidgets
import jinja2
import mistune
import nbconvert
import requests
import time
from IPython import get_ipython, display


# In[6]:

iframe(refs['workflow'])


# In[5]:

iframe(refs['format'])


# # Sharing is caring

# In[13]:

get_ipython().run_cell_magic('display', 'Markdown',
                             "## Gist, Nbviewer, Anaconda <small>no kernel</small>\n\n---\n\nSharing static files means that Javascript can be used for interactivity.\n\n* Github santizes javascript\n* `nbviewer` and `anaconda` embrace it.  Static webpages can be applications.\n    * [`anaconda-nb-extensions`]({{refs['nbext']}})\n    \nhttp://nbviewer.jupyter.org/github/tonyfast/notebookism-chicago/tree/master/")


# ## Binder, Travis <small>not my kernel</small>
#
# * [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/tonyfa
# st/notebookism-chicago)
# * [`travis-ci`](https://travis-ci.org/tonyfast/notebookism-chicago)

# ## I am a stateful machine <small>my kernel</small>
#
# > The work you do locally effects

# # How do you test notebooks?
#
# [`pytest-ipynb`]()

# # Applications and the notebook

# In[ ]:

from flask import Flask
from IPython import get_ipython
app = Flask(__name__)


@app.route("/")
@app.route("/<path:path>")
def hello(path=""):
    if path:
        repo.value = path
        return (__x(**get_ipython().user_ns)
                | repo_template.render
                > mistune.markdown
                )
    return "Hello New World!" + path

if __name__ == "__main__":
    app.run(port=5000)


# In[ ]:

get_ipython().run_cell_magic('file', 'app.py', 'from flask import Flask\nfrom IPython import get_ipython\napp = Flask(__name__)\n\n@app.route("/")\n@app.route("/<path:path>")\ndef hello(path=""):\n    if path:\n        repo.value = path\n        return (__x(**get_ipython().user_ns)\n                 | repo_template.render\n                 > mistune.markdown\n                )\n    return "Hello New World!" + path\n\nif __name__ == "__main__":\n    app.run(port=5000)')


# In[ ]:

# e = envoy.connect('python app.py')
# requests.get('http://localhost:5000/testing').text
# e.kill()


# In[11]:

get_ipython().run_cell_magic('script', 'python --bg', 'from flask import Flask\nfrom IPython import get_ipython\napp = Flask(__name__)\n\n@app.route("/")\n@app.route("/<path:path>")\ndef hello(path=""):\n    if path:\n        repo.value = path\n        return (__x(**get_ipython().user_ns)\n                 | repo_template.render\n                 > mistune.markdown\n                )\n    return "Hello New World!" + path\n\nif __name__ == "__main__":\n    app.run(port=5000)')


# In[8]:

get_ipython().magic('killbgscripts')


# # Conclusion
#
# * Notebooks have come to provide the same flexibility as many modern
# programming.
# * The workflow is ideal for science, or answering a question to gain insight.

# In[ ]:

# kill -15 $( lsof -i:5000 -t )
