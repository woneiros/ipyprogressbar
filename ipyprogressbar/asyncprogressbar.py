# -*- coding: utf-8 -*-

"""Implementation of different distances to use for a geometry

Note
----
The following are in fact _similarities_ and not distances (a score of 1 means very similar, a score of 0 means very different)

.. module:: nlp.geometry.dist
   :platform: Unix, Windows
   :synopsis: Distances between message representations

.. |message| replace:: :class:`nlp.text.message.Message`
.. |tokenizer| replace:: :class:`nlp.text.grammar.tokenizer`
.. |sentgram| replace:: :class:`nlp.text.grammar.grammar_analyzer`

"""

import random
import ipywidgets as widgets
from IPython.display import display

class AsyncProgressBar(object):
    """docstring for AsyncProgressBar"""

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
        self._id = identifier if identifier is not None else str(random.random()).replace('0.', '')
        self.total_time = time
        self.width = width if width is not None else '50%'
        self.height = height if height is not None else '20px'

        html_init = '{d}<div style="width: {w}, height: {h};" id="{i}"></div>'
        self.WIDGET = widgets.HTML( value=html_init.format(d=description, i=self._id, w=self.widgets, h=self.height) )
        self.WIDGET.visible = False

    def get_widget(self):
        return self.WIDGET

    def run(self, time=None):
        _time = time if time is not None else self.total_time
        self.WIDGET.visible = True
        display( widgets.HTML(value=self.INIT_SCRIPT.format(i=self._id, t=_time) + self.RUN_SCRIPT) )

    def hide(self):
        self.WIDGET.visible = False
