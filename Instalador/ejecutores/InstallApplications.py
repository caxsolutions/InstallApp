from numpy.lib.function_base import select

from ejecutores.Progressbar import Progressbar
import subprocess, os, sys

class InstallApplications:

    def installAppUpdate(self, obj):

        proceso8 = subprocess.Popen('apt-get update', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole("Actualizando el sistema", obj)
        self.addConsole(salida8, obj)

    def installAppGdebi(self, obj):
        proceso8 = subprocess.Popen('apt-get install gdebi', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole("Instalando Gdebi paquetes de debian", obj)
        self.addConsole(salida8, obj)

    def installAppTerminator(self, obj):

        self.addConsole("Instalando Terminator console", obj)

        proceso8 = subprocess.Popen('apt-get install terminator -y', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole(salida8, obj)

    def installAppHtop(self, obj):

        self.addConsole("Instalando Htop console", obj)

        proceso8 = subprocess.Popen('apt-get install htop -y', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole(salida8, obj)

    def installAppMidComm(self, obj):

        self.addConsole("Agregando repositorio Midnigth commander", obj)
        proceso = subprocess.Popen('add-apt-repository ppa:eugenesan/ppa -y', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida = proceso.stdout.read()
        proceso.stdout.close()
        salida = salida.decode(sys.getdefaultencoding())

        self.installAppUpdate(obj)

        self.addConsole("Instalando Midnigth commander", obj)
        self.addConsole(salida, obj)

        proceso8 = subprocess.Popen('apt-get install mc -y', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole(salida8, obj)

    def installAppPgadmin3(self, obj):

        self.addConsole("Instalando Pgadmin3", obj)

        proceso8 = subprocess.Popen('apt-get install pgadmin3 -y', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole(salida8, obj)

    def installAppKazam(self, obj):

        self.addConsole("Instalando Kazam", obj)

        proceso8 = subprocess.Popen('apt-get install kazam -y', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole(salida8, obj)

    def installAppVirtualbox(self, obj):
        self.addConsole("Instalando VirtualBox", obj)

        proceso8 = subprocess.Popen('apt-get install virtualbox -y', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole(salida8, obj)

    def installAppGooglechrome(self, obj):
        self.addConsole("Descargando Google chrome", obj)

        proceso8 = subprocess.Popen('wget -c https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -O chrome64.deb', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole(salida8, obj)

        self.addConsole("Instalando Google chrome", obj)
        proceso = subprocess.Popen('gdebi --n chrome64.deb', shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida = proceso.stdout.read()
        proceso.stdout.close()
        salida = salida.decode(sys.getdefaultencoding())

        self.addConsole(salida, obj)

        subprocess.Popen('rm -rf chrome64.deb', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def installApAngryScanner(self, obj):
        self.addConsole("Descargando Angry Ip Scanner", obj)

        proceso8 = subprocess.Popen('wget -c https://github.com/angryziber/ipscan/releases/download/3.4.2/ipscan_3.4.2_amd64.deb -O ipscan.deb', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole(salida8, obj)

        self.addConsole("Instalando Angry Ip Scanner", obj)
        proceso = subprocess.Popen('gdebi --n ipscan.deb', shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida = proceso.stdout.read()
        proceso.stdout.close()
        salida = salida.decode(sys.getdefaultencoding())

        self.addConsole(salida, obj)

        subprocess.Popen('rm -rf ipscan.deb', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def installApMegasync(self, obj):
        self.addConsole("Descargando Megasync", obj)

        proceso8 = subprocess.Popen('wget -c https://mega.nz/linux/MEGAsync/xUbuntu_14.04/amd64/megasync-xUbuntu_14.04_amd64.deb -O megasync.deb', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole(salida8, obj)

        self.addConsole("Instalando Megasync", obj)
        proceso = subprocess.Popen('gdebi --n megasync.deb', shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida = proceso.stdout.read()
        proceso.stdout.close()
        salida = salida.decode(sys.getdefaultencoding())

        self.addConsole(salida, obj)

        subprocess.Popen('rm -rf megasync.deb', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def installAppMoc(self, obj):
        self.addConsole("Instalando Music on consol", obj)

        proceso8 = subprocess.Popen('apt-get install moc -y', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole(salida8, obj)

    def installAppFuentesWindows(self, obj):

        self.addConsole("Instalando fuentes de windows en linux", obj)

        proceso8 = subprocess.Popen('sudo apt-get install msttcorefonts -y', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole(salida8, obj)

        proceso = subprocess.Popen('fc-cache -fv', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida = proceso.stdout.read()
        proceso.stdout.close()
        salida = salida.decode(sys.getdefaultencoding())

        self.addConsole(salida, obj)

    def installAppReproVlc(self, obj):
        self.addConsole("Instalando Reproductor de musica VLC", obj)

        proceso8 = subprocess.Popen('apt-get install vlc -y', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole(salida8, obj)

    def installAppPencilProject(self, obj):
        self.addConsole("Descargando Pencil project", obj)

        proceso8 = subprocess.Popen('wget -c https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/evoluspencil/evoluspencil_2.0.5_all.deb -O pencilproject.deb', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole(salida8, obj)

        self.addConsole("Instalando Pencil project", obj)
        proceso = subprocess.Popen('gdebi --n pencilproject.deb', shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida = proceso.stdout.read()
        proceso.stdout.close()
        salida = salida.decode(sys.getdefaultencoding())

        self.addConsole(salida, obj)

        subprocess.Popen('rm -rf pencilproject.deb', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def addConsole(self, mensaje, obj):
        Progressbar().console_progress(obj, mensaje)