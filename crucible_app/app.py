from view.main_window import MainWindow
from gi.repository import GLib, Adw
import sys
import gi

gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")

class Main(Adw.Application):
    def __init__(self):
        super().__init__(application_id="com.megabytesofrem.crucible")
        GLib.set_application_name("Crucible")

    def do_activate(self):
        window = MainWindow(application=self)
        # self.apply_stylesheet()
        window.present()


app = Main()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
