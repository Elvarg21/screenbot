'''
Another test of gtk and cairo
'''

import gi
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk
import cairo


def main():
    print(dir(Gdk))
    root_win = Gdk.get_default_root_window()
    print(root_win)
    print(Gdk.get_display_arg_name())

    width = root_win.get_width()
    height = root_win.get_height()

    ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    pb = Gdk.pixbuf_get_from_window(root_win, 0, 0, width, height)

    cr = cairo.Context(ims)
    Gdk.cairo_set_source_pixbuf(cr, pb, 0, 0)
    cr.paint()

    ims.write_to_png("screenshot.png")


if __name__ == "__main__":
    main()
