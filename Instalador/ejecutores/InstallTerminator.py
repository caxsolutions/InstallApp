from ejecutores.Progressbar import Progressbar

class InstallTerminator:

    def __init__(self):
        print ""

    def installApp(self, obj):

        progressbar = Progressbar()
        progressbar.toggle_activity_mode(obj)

        return "instalando terminator"