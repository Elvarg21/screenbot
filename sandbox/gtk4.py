
import signal
import time
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango

handlerId = 0

def main():
    button = Gtk.Button("Hello")
    scroll_win = Gtk.ScrolledWindow()
    scroll_win.add(button)
    win = Gtk.Window()
    win.add(scroll_win)

    # Connect to expose signal to allow time
    # for the window to be drawn
    #global handlerId
    #handlerId = win.connect_after('expose-event', drawWindow)
    time.sleep(1)
    drawWindow(win)

    win.show_all()

def drawWindow(win): #, e):
    width, height = win.get_size()
    pixbuf = Gtk.gdk.Pixbuf(Gtk.gdk.COLORSPACE_RGB, False, 8, width, height)

    # Retrieve the pixel data from the gdk.window attribute (win.window)
    # of the Gtk.window object
    screenshot = pixbuf.get_from_drawable(win.window, win.get_colormap(),
                                          0, 0, 0, 0, width, height)
    screenshot.save('screenshot.png', 'png')

    # Disconnect this handler so that it isn't
    # repeated when the screen needs to be redrawn again
    #global handlerId
    #win.disconnect(handlerId)

if __name__ == '__main__':
    main()
    Gtk.main()
