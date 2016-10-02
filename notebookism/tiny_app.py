# coding: utf-8

# In[7]:

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
__all__ = [
    'get_', 'repo_template',
]


# In[8]:

repo = ipywidgets.Text("nteract/nteract")
repo


# In[9]:

@memoize
def get_(url, *args):
    """A memoized request"""
    return requests.get(
        url,
        params=__x(args[::2], args[1::2]).zip.dict.__(),
    )


# In[24]:

# %%time
__repo_information = (__x(repo.value)
                      | 'https://api.github.com/repos/{}'.format
                      | get_
                      | _this().json()._
                      )


# In[38]:

class GlobalTemplate(jinja2.Template):

    def render(self, *args, **kwargs):
        return super().render(
            *args, **merge(
                get_ipython().user_ns,
                kwargs
            ),
        )
env = jinja2.Environment()
env.template_class = GlobalTemplate


def parse_(line):
    return line.strip().split(' ')


@partial(
    get_ipython().register_magic_function,
    magic_name='display',
    magic_kind='cell'
)
def display_template(line, cell):
    display_method, var_name = parse_(line)
    template = env.from_string(cell)
    if var_name:
        globals()[var_name] = template
    if __name__ == "__main__":
        return getattr(
            display, display_method,
        )(template.render())


# In[39]:

repo_info = __repo_information.__()


# In[40]:

get_ipython().run_cell_magic('display', 'Markdown repo_template',
                             '{%- for key, value in repo_info.items() %}\n* __{{key}}__ - {{value}}\n{% endfor %}')


# In[56]:

get_ipython().run_cell_magic('file', 'app.py', 'from flask import Flask\nfrom IPython import get_ipython\napp = Flask(__name__)\n\n@app.route("/")\n@app.route("/<path:path>")\ndef hello(path=""):\n    if path:\n        repo.value = path\n        return (__x(**get_ipython().user_ns)\n                 | repo_template.render\n                 > mistune.markdown\n                )\n    return "Hello New World!" + path\n\nif __name__ == "__main__":\n    app.run(port=5000)')


# In[26]:

# e = envoy.connect('python app.py')

# requests.get('http://localhost:5000/testing').text

# e.kill()


# In[ ]:

# kill -15 $( lsof -i:5000 -t )
