# coding: utf-8

# > Utilities for the presentation

# In[7]:

from toolz.curried import *  # Functional programming
# Pythonic unctional programming syntax
from whatever import __x, _this, callables
from IPython import display, get_ipython

import envoy
import jinja2
import pandas
import requests
import yaml

__all__ = ['iframe', 'env', 'refs', 'toggler']


# In[2]:

iframe = partial(display.IFrame, width=800, height=600)


# In[3]:

with open("../links.yaml.md") as f:
    refs = __x(f.read())[yaml.safe_load] * callables.Dispatch({
        str: lambda s: {s: s}, dict: identity,
    })
    refs = refs > (lambda x: merge(*x))


# In[4]:

class GlobalTemplate(jinja2.Template):

    def render(self, *args, **kwargs):
        return super().render(
            *args, **merge(
                globals(),
                get_ipython().user_ns,
                kwargs,
            ),
        )
env = jinja2.Environment(loader=jinja2.DictLoader({}))
env.template_class = GlobalTemplate


# In[ ]:

def parse_(display_and_template_name):
    """
    """
    display, name = "", ""
    tokens = display_and_template_name.strip().split(' ')
    if len(tokens) is 2:
        display, name = tokens
    else:
        display = first(tokens)
    return display, name


# In[ ]:

@partial(
    get_ipython().register_magic_function,
    magic_name='display',
    magic_kind='cell'
)
def display_template(line, cell):
    display_method, var_name = parse_(line)
    template = env.from_string(cell)
    if var_name:
        env.loader.mapping[var_name] = template
    return getattr(display, display_method,)(template.render())


# In[6]:

toggler = partial(
    display.Javascript,
    """$('#maintoolbar-container').append(
        '<div class="btn-group"><button class="btn btn-default" title="Toggle cells" id="toggle_magic"><i class="fa-eye-slash fa"></i></button></div>'
    )
    $('#toggle_magic').click(
        function(){
            $('.code_cell .input_area').filter(
                function(){
                    return this.innerText.trim().startsWith('%%')
                }
            ).toggle()
        }
    )"""
)
