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

    INIT_SCRIPT = "<script>var stepUpdate = {t}*10;</script>"
    RUN_SCRIPT = """
        <script>
            var progress = 0;
            var timer = setInterval(updateProgressBar, stepUpdate);

            function updateProgressBar(){
                $(#pb_id).progressbar({
                    value: ++progress
                });
                if(progress == 100)
                    clearInterval(timer);
            }

            $(function () {
                $(#pb_id).progressbar({
                    value: progress
                });
            });
        </script>
        """

    def __init__(self, time, width=None, height=None):
        self.total_time = time
        self.width = width if width is not None else '50%'
        self.height = height if height is not None else '20px'

        html_init = '<div style="width: {w}, height: {h};" id="#pb_id"></div>'
        self.WIDGET = widgets.HTML( value=html_init.format(w=self.widgets, h=self.height) )
        self.WIDGET.visible = False

    def get_widget(self):
        return self.WIDGET

    def run(self):
        self.WIDGET.visible = True
        display( widgets.HTML(value=self.INIT_SCRIPT.format(t=self.total_time) + self.RUN_SCRIPT) )

    def hide(self):
        self.WIDGET.visible = False
