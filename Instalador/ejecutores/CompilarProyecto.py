from ejecutores.Progressbar import Progressbar
import subprocess, os, sys

class CompilarProyecto:

    def compilarProyectoWebRfast9(self, obj, ruta=None):

        if ruta != None:
            proceso8 = subprocess.Popen('ant -buildfile ' + ruta + '/build.xml compilar-main', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            salida8 = proceso8.stdout.read()
            proceso8.stdout.close()
            salida8 = salida8.decode(sys.getdefaultencoding())

            self.addConsole("Compilando el proyecto en la ruta " + ruta, obj)
            self.addConsole(salida8, obj)

    def addConsole(self, mensaje, obj):
        Progressbar().console_progress(obj, mensaje)