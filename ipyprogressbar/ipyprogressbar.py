# -*- coding: utf-8 -*-

"""Python-asynchronous progressbar widgets for use in Jupyter/IPython in conjunction with `ipywidgets<https://ipywidgets.readthedocs.io>`_

.. module:: ipyprogressbar.asyncprogressbar
   :platform: Unix, Windows
   :synopsis: Progressbar that executes asynchronous of python

.. |widget| replace:: `ipywidgets.widget<https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Basics.html>`_
"""

import random
import time as tm
import threading
import ipywidgets as widgets
from IPython.display import display

class AsyncProgressBar(object):
    """Progressbar that executes asynchronously in a thread, while other python code executes

    Parameters
    ----------
    time : int
        Number of seconds the progressbar will take to complete
    description : str, optional
        Label to be shown next to the progressbar
    close_on_finish : bool, optional
        Automatically close the progressbar upon completion
    """

    def __init__(self, time, description='', identifier=None, close_on_finish=False):
        self._id = identifier if identifier is not None else 'pb_' + str(random.random()).replace('0.', '')
        self.total_time = time
        self.close_on_finish = close_on_finish
        self.__widget = widgets.IntProgress(value=0, min=0, max=100)
        self.__widget.description = description
        self.__last_value = None
        self.__last_description = description


    @property
    def widget(self):
        """Returns the widget object to be displayed or included in a dashboard

        Returns
        -------
        `ipywidgets.widget<>`_
            Widget
        """
        return self.__widget


    def display(self):
        display(self.widget)


    def __fill_bar(self, time):
        while self.__widget.value < 100:
            tm.sleep(time / 20)
            self.__widget.value += 5

        # Close if on_finish option was specified
        if self.close_on_finish:
            self.__widget.close()


    def run(self, time=None):
        """Triggers the progressbar to start updating (like an animation)

        Parameters
        ----------
        time : int, optional
            Number of seconds the progressbar will take to complete
            If given overrides the time specified on instantiation
        """
        _time = time if time is not None else self.total_time
        thread = threading.Thread(target=self.__fill_bar, args=(_time,)) 
        thread.start()


    def reset(self, percent=0):
        """Reset the progressbar to the specified percent (defaults to zero)

        Parameters
        ----------
        percent : int [0,100], optional
            Int between 0 (empty) and 100 (full) to reset the progressbar to
        """
        self.__widget.value = percent


    def close(self, on_finish=True):
        """Close the widget

        Parameters
        ----------
        on_finish : bool, optional
            Should the widget close when it reaches 100% (default), if not
            the widget will close automatically (even if it's still running)
        """
        if on_finish:
            self.close_on_finish = True
        else:
            self.__last_value = self.__widget.value
            self.__widget.close()


    def reopen(self):
        """Reopen the widget after closing, with the previous last value"""
        self.__widget = widgets.IntProgress(value=0, min=0, max=100)
        self.__widget.value = self.__last_value if self.__last_value else 0
        self.__widget.description = self.__last_description
