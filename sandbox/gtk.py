"""
Joined gtk tests
"""

import time
import signal
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango

import cairo


class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()
        self.width = 500
        self.height = 100

        self.tran_setup()
        self.init_ui()

    def init_ui(self):

        self.connect("draw", self.on_draw)

        self.set_title("Transparent window")
        self.resize(self.width, self.height)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def tran_setup(self):

        self.set_app_paintable(True)
        screen = self.get_screen()

        visual = screen.get_rgba_visual()
        if visual is not None and screen.is_composited():
            self.set_visual(visual)

    def on_draw(self, wid, cr):
        cr.set_source_rgba(0, 0, 0, 0.1)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()

    def get_screenshot(self):
        print(dir(self))
        ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.width, self.height)
        pb = Gdk.pixbuf_get_from_window(self, 0, 0, self.width, self.height)

        cr = cairo.Context(ims)
        Gdk.cairo_set_source_pixbuf(cr, pb, 0, 0)
        cr.paint()

        ims.write_to_png("window_screenshot.png")


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app = Example()
    time.sleep(1)
    app.get_screenshot()
    Gtk.main()


if __name__ == "__main__":
    main()
