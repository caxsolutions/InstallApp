#!/usr/bin/env python

from ejecutores.InstallTerminator import InstallTerminator
from ejecutores.Progressbar import Progressbar

try:
    import pygtk, gobject, pango
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
        gtk.main_quit()

    def on_window1_destroy(self, object, data=None):
        gtk.main_quit()

    def on_gtk_quit_activate(self, menuitem, data=None):
        gtk.main_quit()

    def on_btnlimpiar_clicked(self, widget, data=None):
        self.chbTerminator.set_active(0)
        self.chbHtop.set_active(0)
        self.chbMoc.set_active(0)
        self.chbVirtualbox.set_active(0)
        self.chbKazam.set_active(0)
        self.chbPgadmin.set_active(0)
        self.chbGooglechrome.set_active(0)
        self.chbAngryScanner.set_active(0)
        self.chbMegasync.set_active(0)
        self.chbReproVlc.set_active(0)
        self.chbFuentesWindows.set_active(0)
        self.chbMicp.set_active(0)

    def on_button4_clicked(self, widget, data=None):
        self.chbTerminator.set_active(1)
        self.chbHtop.set_active(1)
        self.chbMoc.set_active(1)
        self.chbVirtualbox.set_active(1)
        self.chbKazam.set_active(1)
        self.chbPgadmin.set_active(1)
        self.chbGooglechrome.set_active(1)
        self.chbAngryScanner.set_active(1)
        self.chbMegasync.set_active(1)
        self.chbReproVlc.set_active(1)
        self.chbFuentesWindows.set_active(1)
        self.chbMicp.set_active(1)

    def on_btnInstalar_clicked(self, widget, data=None):
        print "ejecutar boton instalador", self.chbTerminator.get_active()

        #instalando terminator
        if self.chbTerminator.get_active():

            #cambia el texto del boton para indicar que se esta ejecutando el evento.
            self.btnInstalar.set_label("Instalando");

            installTerm = InstallTerminator()
            installTerm.installApp(self)

    def on_btnCancelar_clicked(self, widget, data=None):
        progressbar = Progressbar()
        progressbar.destroy_progress(self)

    def __init__(self):
        self.timer = 0
        self.gladefile = "glade/instalador.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")

        self.btnTodos = self.builder.get_object("btnTodos")
        self.btnlimpiar = self.builder.get_object("btnlimpiar")
        self.btnInstalar = self.builder.get_object("btnInstalar")
        self.btnCancelar = self.builder.get_object("btnCancelar")

        self.chbTerminator = self.builder.get_object("chbTerminator")
        self.chbHtop = self.builder.get_object("chbHtop")
        self.chbMoc = self.builder.get_object("chbMoc")
        self.chbVirtualbox = self.builder.get_object("chbVirtualbox")
        self.chbKazam = self.builder.get_object("chbKazam")
        self.chbPgadmin = self.builder.get_object("chbPgadmin")
        self.chbGooglechrome = self.builder.get_object("chbGooglechrome")
        self.chbAngryScanner = self.builder.get_object("chbAngryScanner")
        self.chbMegasync = self.builder.get_object("chbMegasync")
        self.chbReproVlc = self.builder.get_object("chbReproVlc")
        self.chbFuentesWindows = self.builder.get_object("chbFuentesWindows")
        self.chbMicp = self.builder.get_object("chbMicp")

        self.textarearesumen = self.builder.get_object("textarearesumen")
        self.textarearesumen.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse('#000000'))
        self.textarearesumen.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse('#00FF00'))
        self.textarearesumen.modify_font(pango.FontDescription('Monospace 7'))

        self.progressbar1 = self.builder.get_object('progressbar1')

        self.window.show()


if __name__ == "__main__":
    main = Buglump()
    gtk.main()