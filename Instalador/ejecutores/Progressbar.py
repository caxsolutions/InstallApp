import pygtk, gobject

class Progressbar:

    def progress_timeout(self, pbobj):
        pbobj.progressbar1.pulse()
        return True

    def toggle_activity_mode(self, obj):

        if obj.timer == 0:
            obj.timer = gobject.timeout_add(50, self.progress_timeout, obj)
            #obj.btnInstalar.set_label(obj.appInstalando);

    # Clean up allocated memory and remove the timer
    def destroy_progress(self, obj):

        if obj.timer:
            gobject.source_remove(obj.timer)
            obj.timer = 0

            textbuffer = obj.textarearesumen.get_buffer()
            text = textbuffer.get_end_iter()
            textbuffer.insert(text, "\n")
            textbuffer.insert(text, "\n-------------------------------------------")
            textbuffer.insert(text, "\n Instalacion cancelada por el usuario")

            self.archi.close()

    def console_progress(self, obj, mensaje):

            textbuffer = obj.textarearesumen.get_buffer()
            text = textbuffer.get_end_iter()
            textbuffer.insert(text, "\n")
            textbuffer.insert(text, "\n-------------------------------------------\n")
            textbuffer.insert(text, mensaje)
            self.crearArchivoResultado(mensaje)


    def crearArchivoResultado(self, mensaje):
        self.archi = open('datos.txt', 'a')
        self.archi.write("\n-------------------------------------------\n")
        self.archi.write(mensaje + '\n')


