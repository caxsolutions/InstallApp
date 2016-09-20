import pygtk, gobject


def progress_timeout(pbobj):
    pbobj.progressbar1.pulse()
    return True

class Progressbar:

    def toggle_activity_mode(self, obj):

        if obj.timer == 0:
            obj.timer = gobject.timeout_add(100, progress_timeout, obj)

    # Clean up allocated memory and remove the timer
    def destroy_progress(self, widget, data=None):
        gobject.source_remove(self.timer)
        self.timer = 0