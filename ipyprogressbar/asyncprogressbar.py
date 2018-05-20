# -*- coding: utf-8 -*-

"""Python-asynchronous progressbar widgets for use in Jupyter/IPython in conjunction with `ipywidgets<https://ipywidgets.readthedocs.io>`_

.. module:: ipyprogressbar.asyncprogressbar
   :platform: Unix, Windows
   :synopsis: Progressbar that executes asynchronous of python

.. |widget| replace:: `ipywidgets.widget<https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Basics.html>`_
"""

import random
import ipywidgets as widgets
from IPython.display import display

class AsyncProgressBar(object):
    """Progressbar that executes asynchronously (while other python code executes)

    Parameters
    ----------
    time : int
        Number of seconds the progressbar will take to complete
    description : str, optional
        Label to be shown next to the progressbar
    identifier : str, optional
        Identifier of this specific progressbar (to avoid collision with other progressbars)
        If no string is passed a random string of numbers will be used as suffix to 'pb_'
    width : int, optional
        Width of the progressbar
    height : int, optional
        Height of the progressbar
    """

    INIT_SCRIPT = "<script> var pbId = '#{i}'; var stepUpdate = {t}*10;</script>"
    RUN_SCRIPT = """
        <script>
            var progress = 0;
            var timer = setInterval(updateProgressBar, stepUpdate);

            function updateProgressBar(){
                $(pbId).progressbar({
                    value: ++progress
                });
                if(progress == 100)
                    clearInterval(timer);
            }

            $(function () {
                $(pbId).progressbar({
                    value: progress
                });
            });
        </script>
        """

    def __init__(self, time, description='', identifier=None, width=None, height=None):
        self._id = identifier if identifier is not None else 'pb_' + str(random.random()).replace('0.', '')
        self.total_time = time
        self.width = width if width is not None else '50%'
        self.height = height if height is not None else '20px'

        html_init = '{d}<div style="width: {w}, height: {h};" id="{i}"></div>'
        self.WIDGET = widgets.HTML( value=html_init.format(d=description, i=self._id, w=self.width, h=self.height) )
        self.WIDGET.visible = False

    def get_widget(self):
        """Returns the widget object to be displayed or included in a dashboard

        Returns
        -------
        `ipywidgets.widget<>`_
            Widget
        """
        return self.WIDGET

    def run(self, time=None):
        """Triggers the progressbar to start updating (like an animation)

        Parameters
        ----------
        time : int, optional
            Number of seconds the progressbar will take to complete
            If given overrides the time specified on instantiation
        """
        _time = time if time is not None else self.total_time
        self.WIDGET.visible = True
        display( widgets.HTML(value=self.INIT_SCRIPT.format(i=self._id, t=_time) + self.RUN_SCRIPT) )

    def hide(self):
        """Hides the progressbar (sets widget.visible to False)
        """
        self.WIDGET.visible = False
