

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
import cairo


class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()

        self.setup()
        self.init_ui()


    def setup(self):

        self.set_app_paintable(True)
        self.set_type_hint(Gdk.WindowTypeHint.DOCK)
        self.set_keep_below(True)
        #self.set_keep_above(True)

        screen = self.get_screen()
        visual = screen.get_rgba_visual()
        if visual is not None and screen.is_composited():
            self.set_visual(visual)


    def init_ui(self):

        self.connect("draw", self.on_draw)

        lbl = Gtk.Label()
        text = "You have been hacked! Haha!"
        lbl.set_text(text)

        fd = Pango.FontDescription("Serif 40")
        lbl.modify_font(fd)
        lbl.modify_fg(Gtk.StateFlags.NORMAL,Gdk.color_parse("white"))

        self.add(lbl)

        self.resize(300, 250)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


    def on_draw(self, wid, cr):

        cr.set_operator(cairo.OPERATOR_CLEAR)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)


def main():

        app = Example()
        Gtk.main()


if __name__ == "__main__":
    import signal
    print(signal.SIGINT, signal.SIG_DFL)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
