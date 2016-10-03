# coding: utf-8

# # <small>Part 2</small>
#
# ---
# <h3> FOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIME
# FOCUSTIME<br/>TIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUS
# TIMEFOCUSTIME<br/>FOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUS
# TIMEFOCUSTIMEFOCUSTIME<br/>TIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEF
# OCUSTIMEFOCUSTIMEFOCUSTIME<br/>FOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEF
# OCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIME<br/>TIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUST
# IMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIME<br/>FOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUST
# IMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIME<br/>TIMEFOCUSTIMEFOCUSTIMEFO
# CUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIME<br/>FOCUSTIMEFOCUSTIMEFO
# CUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIME<br/>~~SUCCESS~~
# TIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIMEFOCUSTIME<
# br/></h3>
#
# ---
#
# > “What we’re seeing is that by lowering that barrier and by producing a tool
# that is very close to the natural workflow, it makes it sort of easy to do
# the right thing,”

# In[1]:

if __name__ is '__main__':
    from utils import env, iframe, refs
else:
    from .utils import env, iframe, refs


from toolz.curried import *
from whatever import *
from IPython import display, get_ipython
import pandas
import requests

__all__ = ['get_']


# # [There are only two hard things in Computer Science: cache invalidation and
# naming things.](http://martinfowler.com/bliki/TwoHardThings.html)
#
# > Phil Karlton - former principal curmudgeon @ Netscape

# In[2]:

# pep 20
if __name__ is '__main__':
    import this


# In[35]:

get_ipython().run_cell_magic('display', 'HTML _',
                             '<iframe src="//www.slideshare.net/slideshow/embed_code/key/Mss7FQdY74pJvO?startSlide=3" width="595" height="485" frameborder="0" marginwidth="0" marginheight="0" scrolling="no" style="border:1px solid #CCC; border-width:1px; margin-bottom:5px; max-width: 100%;" allowfullscreen> </iframe> <div style="margin-bottom:5px"> <strong> <a href="//www.slideshare.net/doughellmann/an-introduction-to-the-zen-of-python" title="An Introduction to the Zen of Python" target="_blank">An Introduction to the Zen of Python</a> </strong> from <strong><a href="//www.slideshare.net/doughellmann" target="_blank">doughellmann</a></strong> </div>\n\n<hr/>\n<div class="row"><a href="{{refs[\'pep8\']}}">Pep 8</a></div>')


# In[24]:

# this??


# In[7]:

iframe(refs['torus'])


# In[8]:

get_ipython().run_cell_magic('display', 'Markdown _',
                             '{{pandas.read_html(\n    "<table>%s</table>" % \n    requests.get(refs[\'kernels\']).text.split(\'<table>\')[1].split(\'</table>\')[0]\n)[0].to_html()}}')


# In[9]:

# Model-View-Controller wiki
display.Image(refs['mvc'])


# In[10]:

display.Image(refs['workflow'])


# In[ ]:

iframe(refs['typography'])


# In[11]:

iframe(refs['pn_styleguide'])


# In[12]:

iframe(refs['fp_literate'])


# # in developing notebooks, you must be both the `author` and `reader`

# # Magics
#
# ---
#
# Anything you can do on the command line, you can do in the Notebook.  Python
# is just a scripting language.
#
# The `kernel` talks to client.

# In[13]:

# Kernel
ip = get_ipython()
# ip.magics_manager.magics['cell']
ip.user_ns.keys()


# # Create a line magic

# In[14]:

ip.register_magic_function(
    __x()[str.strip][requests.get].__,
    magic_name='request_no_cache',
)


# In[30]:

# %request_no_cache https://api.github.com/repos/nteract/nteract


# In[27]:

# if __name__ is '__main__' and _:
#     _.headers['X-RateLimit-Remaining']


# # Caching - <small>for personal consumption.</small>
#
# * As data grows, accessing it will take more time.
# * Download remote as infrequently as possible.
# * Sometimes accessing data has a cost, or limit.
# * _Keep your focus on the notebook._

# In[25]:

@memoize
def get_(url, *args):
    """A memoized request"""
    return requests.get(
        url,
        params=__x(args[::2], args[1::2]).zip.dict.__(),
    )

ip.register_magic_function(
    __x()[str.strip][get_].__,
    magic_name='request',
)


# In[18]:

# %request https://api.github.com/repos/nteract/nteract


# In[19]:

# __x(get_.__closure__).first[_this().cell_contents._].__()[
#     ('https://api.github.com/repos/nteract/nteract',)
# ].headers['X-RateLimit-Remaining']


# # Parallelism

# In[20]:

get_ipython().run_cell_magic('html', '', '<script async class="speakerdeck-embed" data-slide="4" data-id="983b21f06a070130c77d22000a91bfda" data-ratio="1.2994923857868" src="//speakerdeck.com/assets/embed.js"></script>')


# In[21]:

get_ipython().run_cell_magic('display', 'Markdown _',
                             "# A simple joblib example\n\n[Saving time with embarassingly parallel loops.]({{refs['tf_parallel']}})")


# In[33]:

iframe(refs['dask_overview'])


# In[32]:

get_ipython().run_cell_magic('display', 'Markdown _',
                             "# Functional Programming\n\nRecently, I started using functional programming approaches.  Functional programming reduces the cognitive load of name.  Write less to do more.\n\n> [My suspicion is that non-CS major programmers value understandability and \nfewer errors, over fewer keystrokes and more power.]({{refs['mg_functional']}})\n\n\n* [toolz]({{refs['toolz']}})\n* [whatever-forever]({{refs['wf']}})\n* {{refs['dm_functional']}}")


# # On Productivity
#
# * Many ~~computer~~ scientists before us have solved hard computing
# questions.  Producivity suffers by ignoring history.
# * Keep your focus
#
#     * less tabbing
#     * more caching
#     * parallelize if you can
#
#      * write parallizable code
#
#     * compartmentalize code & non-code cells
#
# * Automate redundant interactions: testing, deployment, documentation...

# In[ ]:
