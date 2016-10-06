#!/usr/bin/env python

from ejecutores.InstallApplications import InstallApplications
from ejecutores.Progressbar import Progressbar

try:
    import pygtk, gobject, pango, vte, threading
    pygtk.require('2.0')
except:
    pass
try:
    import gtk
    import gtk.glade
except:
    print('GTK not available')

class Buglump:

    def on_btnInstalar_clicked(self, widget, data=None):

        threadExec = threading.Thread(target=Progressbar().toggle_activity_mode,args=(self,))
        threadExec.start()

        if threadExec.is_alive:

            InstallApplications().installAppUpdate(self)
            InstallApplications().installAppGdebi(self)

            if self.chbTerminator.get_active():
                InstallApplications().installAppTerminator(self)

            if self.chbHtop.get_active():
                InstallApplications().installAppHtop(self)

            if self.chbMidComm.get_active():
                InstallApplications().installAppMidComm(self)

            if self.chbPgadmin.get_active():
                InstallApplications().installAppPgadmin3(self)

            if self.chbKazam.get_active():
                InstallApplications().installAppKazam(self)

            if self.chbVirtualbox.get_active():
                InstallApplications().installAppVirtualbox(self)

            if self.chbGooglechrome.get_active():
                InstallApplications().installAppGooglechrome(self)

            if self.chbAngryScanner.get_active():
                InstallApplications().installApAngryScanner(self)

            if self.chbMegasync.get_active():
                InstallApplications().installApMegasync(self)

            if self.chbMoc.get_active():
                InstallApplications().installAppMoc(self)

            if self.chbFuentesWindows.get_active():
                InstallApplications().installAppFuentesWindows(self)

            if self.chbReproVlc.get_active():
                InstallApplications().installAppReproVlc(self)

            if self.chbPencilProject.get_active():
                InstallApplications().installAppPencilProject(self)

    def on_btnAbout_clicked(self, widget, data=None):
        self.aboutdialog1.show()

    def on_aboutdialog1_button_press_event(self, widget, data=None):
        print 123

    def on_btnInstalar_clicked_test(self, widget, data=None):
        print 123

        #threadExec = threading.Thread(target=Progressbar().toggle_activity_mode,args=(self,))
        #threadExec.start()

        #if threadExec.is_alive:
        #    print "se esta ejecutando progressbar"
            #instalando terminator
        #    if self.chbTerminator.get_active():
        #        InstallTerminator().installApp()
                #Progressbar().destroy_progress(self)


    def gtk_main_quit(self, menuitem):
        gtk.main_quit()

    def on_window1_destroy(self, object, data=None):
        gtk.main_quit()

    def on_gtk_quit_activate(self, menuitem, data=None):
        gtk.main_quit()

    def on_btnlimpiar_clicked(self, widget, data=None):
        self.chbTerminator.set_active(0)
        self.chbHtop.set_active(0)
        self.chbMidComm.set_active(0)
        self.chbVirtualbox.set_active(0)
        self.chbKazam.set_active(0)
        self.chbPgadmin.set_active(0)
        self.chbGooglechrome.set_active(0)
        self.chbAngryScanner.set_active(0)
        self.chbMegasync.set_active(0)
        self.chbReproVlc.set_active(0)
        self.chbFuentesWindows.set_active(0)
        self.chbMoc.set_active(0)
        self.chbPencilProject.set_active(0)

    def on_button4_clicked(self, widget, data=None):
        self.chbTerminator.set_active(1)
        self.chbHtop.set_active(1)
        self.chbMidComm.set_active(1)
        self.chbVirtualbox.set_active(1)
        self.chbKazam.set_active(1)
        self.chbPgadmin.set_active(1)
        self.chbGooglechrome.set_active(1)
        self.chbAngryScanner.set_active(1)
        self.chbMegasync.set_active(1)
        self.chbReproVlc.set_active(1)
        self.chbFuentesWindows.set_active(1)
        self.chbMoc.set_active(1)
        self.chbPencilProject.set_active(1)

    def on_btnCancelar_clicked(self, widget, data=None):
        Progressbar().destroy_progress(self)

    def on_btnSalir_clicked(self, widget, data=None):
        self.on_window1_destroy(widget, None)

    def __init__(self):
        self.timer = 0
        #self.threadExec = None
        self.gladefile = "glade/instalador.glade"
        self.builder = gtk.Builder()
        self.builder.add_from_file(self.gladefile)
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("window1")

        #self.vbox1 = self.builder.get_object("vbox1")
        #self.scroll = gtk.ScrolledWindow()

        #self.shell = vte.Terminal()
        #self.shell.connect("child-exited", gtk.main_quit)
        #self.shell.fork_command()
        #self.scroll.add(self.shell)
        #self.vbox1.add(self.scroll)

        self.txtPassword = self.builder.get_object("txtPassword")
        self.btnAbout = self.builder.get_object("btnAbout")
        self.btnTodos = self.builder.get_object("btnTodos")
        self.btnlimpiar = self.builder.get_object("btnlimpiar")
        self.btnInstalar = self.builder.get_object("btnInstalar")
        self.btnCancelar = self.builder.get_object("btnCancelar")
        self.btnSalir = self.builder.get_object("btnSalir")

        self.chbTerminator = self.builder.get_object("chbTerminator")
        self.chbHtop = self.builder.get_object("chbHtop")
        self.chbMidComm = self.builder.get_object("chbMidComm")
        self.chbVirtualbox = self.builder.get_object("chbVirtualbox")
        self.chbKazam = self.builder.get_object("chbKazam")
        self.chbPgadmin = self.builder.get_object("chbPgadmin")
        self.chbGooglechrome = self.builder.get_object("chbGooglechrome")
        self.chbAngryScanner = self.builder.get_object("chbAngryScanner")
        self.chbMegasync = self.builder.get_object("chbMegasync")
        self.chbReproVlc = self.builder.get_object("chbReproVlc")
        self.chbFuentesWindows = self.builder.get_object("chbFuentesWindows")
        self.chbMoc = self.builder.get_object("chbMoc")
        self.chbPencilProject = self.builder.get_object("chbPencilProject")

        self.textarearesumen = self.builder.get_object("textarearesumen")
        self.textarearesumen.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse('#000000'))
        self.textarearesumen.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse('#00FF00'))
        self.textarearesumen.modify_font(pango.FontDescription('Monospace 7'))

        self.progressbar1 = self.builder.get_object('progressbar1')

        self.aboutdialog1 = self.builder.get_object('aboutdialog1')

        self.window.show_all()


if __name__ == "__main__":
    main = Buglump()
    gtk.main()