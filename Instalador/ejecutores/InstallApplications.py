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

    def installApp(self, obj, comando, texto):
        proceso8 = subprocess.Popen('apt-get install ' + comando + ' -y', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole("Instalando " + texto, obj)
        self.addConsole(salida8, obj)

    def installAppDescargar(self, obj, ruta, texto):

        nombreTmp = "apptemp.deb";
        self.addConsole("Descargando " + texto, obj)

        proceso8 = subprocess.Popen('wget -c ' + ruta + ' -O ' + nombreTmp, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida8 = proceso8.stdout.read()
        proceso8.stdout.close()
        salida8 = salida8.decode(sys.getdefaultencoding())

        self.addConsole(salida8, obj)

        self.addConsole("Instalando " + texto, obj)
        proceso = subprocess.Popen('gdebi --n ' + nombreTmp, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        salida = proceso.stdout.read()
        proceso.stdout.close()
        salida = salida.decode(sys.getdefaultencoding())

        self.addConsole(salida, obj)

        subprocess.Popen('rm -rf ' + nombreTmp, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

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

    def addConsole(self, mensaje, obj):
        Progressbar().console_progress(obj, mensaje)