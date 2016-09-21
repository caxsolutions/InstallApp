import pygtk, gobject

def progress_timeout(pbobj):
    pbobj.progressbar1.pulse()
    return True

class Progressbar:

    def toggle_activity_mode(self, obj):

        if obj.timer == 0:
            obj.timer = gobject.timeout_add(50, progress_timeout, obj)

    # Clean up allocated memory and remove the timer
    def destroy_progress(self, obj):

        if obj.timer:
            gobject.source_remove(obj.timer)
            obj.timer = 0

            textbuffer = obj.textarearesumen.get_buffer()
            text = textbuffer.get_end_iter()
            textbuffer.insert(text, "\n")
            textbuffer.insert(text, "\n -------------------------------------------")
            textbuffer.insert(text, "\n Instalacion cancelada por el usuario")
