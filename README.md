## IPyProgressBar

[![saythanks](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/WillahScott)

A small package that provides an python-asynchronous progressbar widgets for use in Jupyter/IPython in conjunction with `ipywidgets`.

### Why

Many times, when building a small dashboard on IPython there are functions that take some time to be executed but cannot be split into chunks, in the middle of which we could update a progress bar.

Since we want to give the user feedback that we are actually doing something and now he has to wait for a little, we can simply display the prototypical `Loading...`.

However for some (most?) functions we may actually have a rough estimate of the time of wait and can make the wait a little more visual with a progressbar!

### "Python-Asynchronous"

The progressbar needs to be updated (filled) while python is working on other things. (Yes we could parallelize it, but it seems a little of overkill).

We will create an HTML object with the progressbar and then let python trigger a small javascript snippet that during a specific interval time regularly updates the progressbar, while python goes on working on other tasks (like loading a dataset). That way, the task of rendering and updating the progressbar is fully delegated to the browser.

### Usage

```python
# Create the progress bar object (not the widget)
my_progressbar = AsyncProgressBar(time=2, description='Loading dataset:')

# Return the widget for display
display( my_progressbar.get_widget() )

# ...

# Trigger the progressbar
my_progressbar.run()
```

The object also has a `hide()` method, for a typical use case in which we just want a temporal progressbar:

```python
my_progressbar.run()
function_that_takes_long()
my_progressbar.hide()
```

### Contact

Created by: [WillahScott](https://github.com/WillahScott/)
