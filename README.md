## IPyProgressBar

[![saythanks](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/WillahScott)

A small package that provides an python-asynchronous progressbar widgets for use in Jupyter/IPython in conjunction with `ipywidgets`.


### Why

Many times, when building a small dashboard on IPython there are functions that take some time to be executed but cannot be split into chunks, in the middle of which we could update a progress bar.

Since we want to give the user feedback that we are actually doing something and now he has to wait for a little, we can simply display the prototypical `Loading...`.

However for some (most?) functions we may actually have a rough estimate of the time of wait and can make the wait a little more visual with a progressbar!


### "Python-Asynchronous"

The progressbar needs to be updated (filled) while python is working on other things. Therefore, we can use a python thread to update the value of the progressbar. That way, our main python process can take care of other code meanwhile.


### Usage

```python
# Create the progress bar object (not the widget)
my_progressbar = AsyncProgressBar(time=2, description='Loading dataset:')

# Return the widget for display
my_progressbar.display()

# ...

# Trigger the progressbar
my_progressbar.run()
```

The object also has a `close()` method (and its inverse `reopen()`), for hiding the progressbar whenever we want:

```python
my_progressbar.run()
function_that_takes_long()
my_progressbar.close(on_finish=True)  # or set close_on_finish=True on creating the progressbar object
```

However,for a typical use case in which we just want a temporal progressbar, we can specify the `close_on_finish` on creation:

```python
# Create the progress bar object (not the widget)
my_progressbar = AsyncProgressBar(time=2, description='Loading dataset:', close_on_finish=True)

# ...

# Trigger the progressbar
my_progressbar.run()  # when done the progress bar will hide
```



### Contact

Created by: [WillahScott](https://github.com/WillahScott/)
