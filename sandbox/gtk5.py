import time
import signal
import cairo
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango



def init_ui(app):

    #app.connect("draw", app.on_draw)

    app.set_title("Transparent window")
    app.resize(500, 100)
    app.set_position(Gtk.WindowPosition.CENTER)
    app.connect("delete-event", Gtk.main_quit)
    app.show_all()

def tran_setup(app):

    app.set_app_paintable(True)
    screen = app.get_screen()

    visual = screen.get_rgba_visual()
    if visual is not None and screen.is_composited():
        app.set_visual(visual)

def on_draw(app, wid, cr):
    cr.set_source_rgba(0, 0, 0, 0.1)
    cr.set_operator(cairo.OPERATOR_SOURCE)
    cr.paint()

def get_screenshot(app):
    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, 500, 100)
    pb = Gdk.pixbuf_get_from_window(app, 0, 0, 500, 100)

    cr = cairo.Context(ims)
    Gdk.cairo_set_source_pixbuf(cr, pb, 0, 0)
    cr.paint()

    ims.write_to_png("window_screenshot.png")


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    app = Gtk.Window()

    tran_setup(app)
    init_ui(app)


    time.sleep(1)
    get_screenshot(app)



if __name__ == '__main__':
    main()
    Gtk.main()
