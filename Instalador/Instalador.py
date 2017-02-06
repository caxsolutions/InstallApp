#!/usr/bin/env python

from ejecutores.InstallApplications import InstallApplications
from ejecutores.Progressbar import Progressbar
from ejecutores.CompilarProyecto import CompilarProyecto

try:
    import pygtk, gobject, pango, vte, threading, os
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

        #threadExec = threading.Thread(target=Progressbar().toggle_activity_mode,args=(self,))
        #threadExec.start()

        #if threadExec.is_alive:

        InstallApplications().installAppUpdate(self)
        InstallApplications().installApp(self, "gdebi", "Gdebi paquetes de debian")

        if self.chbTerminator.get_active():
            InstallApplications().installApp(self, "terminator", "Terminator")

        if self.chbHtop.get_active():
            InstallApplications().installApp(self, "htop", "Htop")

        if self.chbMidComm.get_active():
            InstallApplications().installAppMidComm(self)

        if self.chbPgadmin.get_active():
            InstallApplications().installApp(self, "pgadmin3", "Pgadmin3")

        if self.chbKazam.get_active():
            InstallApplications().installApp(self, "kazam", "kazam")

        if self.chbVirtualbox.get_active():
            InstallApplications().installApp(self, "virtualbox", "VirtualBox")

        if self.chbGooglechrome.get_active():
            InstallApplications().installAppDescargar(self, "https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb", "Google chrome")

        if self.chbAngryScanner.get_active():
            InstallApplications().installAppDescargar(self, "https://github.com/angryziber/ipscan/releases/download/3.4.2/ipscan_3.4.2_amd64.deb", "Angry Ip Scanner")

        if self.chbMegasync.get_active():
            InstallApplications().installAppDescargar(self, "https://mega.nz/linux/MEGAsync/xUbuntu_16.04/amd64/megasync-xUbuntu_16.04_amd64.deb", "Megasync")

        if self.chbMoc.get_active():
            InstallApplications().installApp(self, "moc", "Music on consol")

        if self.chbFuentesWindows.get_active():
            InstallApplications().installAppFuentesWindows(self)

        if self.chbReproVlc.get_active():
            InstallApplications().installApp(self, "vlc", "Reproductor de musica VLC")

        if self.chbPencilProject.get_active():
            InstallApplications().installAppDescargar(self, "https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/evoluspencil/evoluspencil_2.0.5_all.deb", "Pencil project")

        if self.chbAntCompilerJava.get_active():
            InstallApplications().installApp(self, "ant", "ant compilador de java")

        if self.chbGladeGtk.get_active():
            InstallApplications().installApp(self, "glade", "Glade gtk")

        if self.chbNetbeans.get_active():
            InstallApplications().installAppDescargar(self, "http://download.netbeans.org/netbeans/8.2/final/bundles/netbeans-8.2-linux.sh", "Netbeans IDE")

        # if self.chbPycharmIDE.get_active():
        #     InstallApplications().installAppPycharmIDE(self)
        #
        # if self.chbDebeaver.get_active():
        #     InstallApplications().installAppDebeaver(self)
        #
        if self.chbHaroopad.get_active():
            InstallApplications().installApp(self, "haroopad", "haroopad")

        if self.chbQtQr.get_active():
            InstallApplications().installApp(self, "qtqr", "QtQr code")

        if self.chbSkype.get_active():
            InstallApplications().installAppDescargar(self, "https://get.skype.com/go/getskype-linux-beta-ubuntu-64", "Skype")

        # if self.chbTeamViewer.get_active():
        #     InstallApplications().installAppTeamViewer(self)

    def on_btnAbout_clicked(self, widget, data=None):
        self.aboutdialog1.show()

    #############################################################################################
    #################### tab de compilacion #####################################################
    def on_btnSeleccProjectComp_clicked(self, widget, data=None):
        self.filechooserdialog1.show()

    def on_btnAceptarBuildProject_clicked(self, widget, data=None):
        ruta = self.filechooserdialog1.get_filename()

        self.filechooserdialog1.hide()

        if ruta != None:
            self.lblRutaProyectoCompilar.set_text(ruta)
            self.dialogConfirmCompilar.show()
            self.rutaCompilacionProyecto = ruta

    def on_btnCancelarBuildProject_clicked(self, widget, data=None):
        self.filechooserdialog1.hide()

    def on_btnAceptarConfirmCompilar_clicked(self, widget, data=None):

        if self.rutaCompilacionProyecto != None:
            CompilarProyecto().compilarProyectoWebRfast9(self, self.rutaCompilacionProyecto)
            self.dialogConfirmCompilar.hide()

    def on_btnCancelarConfirmCompilar_clicked(self, widget, data=None):
        self.dialogConfirmCompilar.hide()
    #############################################################################################

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
        self.chbAntCompilerJava.set_active(0)
        self.chbGladeGtk.set_active(0)
        self.chbNetbeans.set_active(0)
        self.chbPycharmIDE.set_active(0)
        self.chbHaroopad.set_active(0)
        self.chbDebeaver.set_active(0)
        self.chbQtQr.set_active(0)
        self.chbSkype.set_active(0)
        self.chbTeamViewer.set_active(0)

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
        self.chbAntCompilerJava.set_active(1)
        self.chbGladeGtk.set_active(1)
        self.chbNetbeans.set_active(1)
        self.chbPycharmIDE.set_active(1)
        self.chbHaroopad.set_active(1)
        self.chbDebeaver.set_active(1)
        self.chbQtQr.set_active(1)
        self.chbSkype.set_active(1)
        self.chbTeamViewer.set_active(1)

    def on_btnCancelar_clicked(self, widget, data=None):
        Progressbar().destroy_progress(self)

    def on_btnSalir_clicked(self, widget, data=None):
        self.on_window1_destroy(widget, None)

    def __init__(self):

        #if not os.geteuid() == 0:

        self.timer = 0
        #self.threadExec = None
        self.gladefile = "/exp/PYTHON_DEV/InstallApp/Instalador/glade/instalador.glade"
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
        self.chbAntCompilerJava = self.builder.get_object("chbAntCompilerJava")

        self.chbGladeGtk = self.builder.get_object("chbGladeGtk")
        self.chbNetbeans = self.builder.get_object("chbNetbeans")
        self.chbPycharmIDE = self.builder.get_object("chbPycharmIDE")
        self.chbHaroopad = self.builder.get_object("chbHaroopad")
        self.chbDebeaver = self.builder.get_object("chbDebeaver")
        self.chbQtQr = self.builder.get_object("chbQtQr")
        self.chbSkype = self.builder.get_object("chbSkype")
        self.chbTeamViewer = self.builder.get_object("chbTeamViewer")

        self.textarearesumen = self.builder.get_object("textarearesumen")
        self.textarearesumen.modify_base(gtk.STATE_NORMAL, gtk.gdk.color_parse('#000000'))
        self.textarearesumen.modify_text(gtk.STATE_NORMAL, gtk.gdk.color_parse('#00FF00'))
        self.textarearesumen.modify_font(pango.FontDescription('Monospace 7'))

        self.progressbar1 = self.builder.get_object('progressbar1')

        ##############################################################
        ################## tab compilardor ###########################
        self.rutaCompilacionProyecto = None
        self.btnSeleccProjectComp = self.builder.get_object('btnSeleccProjectComp')
        self.filechooserdialog1 = self.builder.get_object('filechooserdialog1')
        self.btnAceptarBuildProject = self.builder.get_object("btnAceptarBuildProject")
        self.btnCancelarBuildProject = self.builder.get_object("btnCancelarBuildProject")

        self.dialogConfirmCompilar = self.builder.get_object('dialogConfirmCompilar')
        self.lblRutaProyectoCompilar = self.builder.get_object('lblRutaProyectoCompilar')
        self.btnCancelarConfirmCompilar = self.builder.get_object('btnCancelarConfirmCompilar')
        self.btnAceptarConfirmCompilar = self.builder.get_object('btnAceptarConfirmCompilar')

        ##############################################################
        ################## dialog del about ##########################
        self.aboutdialog1 = self.builder.get_object('aboutdialog1')

        self.window.show_all()

if __name__ == "__main__":
    main = Buglump()
    gtk.main()