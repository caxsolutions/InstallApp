#!/usr/bin/env python
from zim.actions import toggle_action

from ejecutores.InstallTerminator import InstallTerminator

try:
    import pygtk, gobject
    pygtk.require('2.0')
except:
    pass
try:
    import gtk
    import gtk.glade
except:
    print('GTK not available')

class Buglump:
    def gtk_main_quit(self, menuitem):
        print "destruyendo aplicacion"
        gtk.main_quit()

    def on_window1_destroy(self, object, data=None):
        print "quit with cancel"
        gtk.main_quit()

    def on_gtk_quit_activate(self, menuitem, data=None):
        print "quit from menu"
        gtk.main_quit()

    def on_btnInstalar_clicked(self, widget, data=None):
        print "ejecutar boton instalador", self.chbTerminator.get_active()
        #self.current = self.chbTerminator.get_active()

        installTerm = InstallTerminator()
        print installTerm.installApp(self)

    def __init__(self):
        self.timer = 0
        self.gladefile = "glade/instalador.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")
        self.btnInstalar = self.builder.get_object("btnInstalar")

        self.chbTerminator = self.builder.get_object("chbTerminator")

        self.progressbar1 = self.builder.get_object('progressbar1')

        self.window.show()


if __name__ == "__main__":
    main = Buglump()
    gtk.main()