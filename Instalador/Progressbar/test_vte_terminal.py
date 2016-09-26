from gi.repository import GObject
#GObject is not required. I just import it everywhere just in case.
#Gtk, Vte, and GLib are required.
from gi.repository import GLib
import os, gtk, vte
#os.environ['HOME'] helps to keep from hard coding the home string.
#os is not required unless you want that functionality.

class TheWindow(gtk.Window):

    def __init__(self):
        gtk.Window.__init__(self, title="inherited cell renderer")
        self.set_default_size(600, 300)
        self.terminal     = vte.Terminal()
        self.terminal.fork_command_full(
                vte.PtyFlags.DEFAULT, #default is fine
                os.environ['HOME'], #where to start the command?
                ["/bin/sh"], #where is the emulator?
                [], #it's ok to leave this list empty
                GLib.SpawnFlags.DO_NOT_REAP_CHILD,
                None, #at least None is required
                None,
                )
        #Set up a button to click and run a demo command
        self.button = gtk.Button("Do The Command")
        #To get the command to automatically run
        #a newline(\n) character is used at the end of the
        #command string.
        self.command = "echo \"Sending this command to a virtual terminal.\"\n"
        command = gtk.Label("The command: "+self.command)
        self.button.connect("clicked", self.InputToTerm)
        #end demo command code

        #set up the interface
        box = gtk.Box(orientation=gtk.Orientation.VERTICAL)
        box.pack_start(self.button, False, True, 0)
        box.pack_start(command, False, True, 1)
        #a scroll window is required for the terminal
        scroller = gtk.ScrolledWindow()
        scroller.set_hexpand(True)
        scroller.set_vexpand(True)
        scroller.add(self.terminal)
        box.pack_start(scroller, False, True, 2)
        self.add(box)

    def InputToTerm(self, clicker):
        #get the command when the button is clicked
        length = len(self.command)
        #A length is not required but is the easiest mechanism.
        #Otherwise the command must be null terminated.
        #Feed the command to the terminal.
        self.terminal.feed_child(self.command, length)


win = TheWindow()
win.connect("delete-event", gtk.main_quit)
win.show_all()
gtk.main()