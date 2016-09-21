from ejecutores.Progressbar import Progressbar
import os

class InstallTerminator:

    def __init__(self):
        print ""

    def installApp(self, obj):

        print "instalando terminator"

        progressbar = Progressbar()
        progressbar.toggle_activity_mode(obj)

        self.ejecutarComando(obj)

    def ejecutarComando(self, obj):

        textbuffer = obj.textarearesumen.get_buffer()
        text = textbuffer.get_end_iter()
        textbuffer.insert(text, "\n The text to insert at the end")

        print os.uname()
        textbuffer.insert(text, "\n" + os.uname().__str__())