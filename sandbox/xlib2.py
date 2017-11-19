'''
getting focused window
'''

import Xlib.display

display = Xlib.display.Display()
window = display.get_input_focus().focus
wmclass = window.get_wm_class()
if wmclass is None:
    print('ok')
    window = window.query_tree().parent
    wmclass = window.get_wm_class()

print(wmclass)
print(window.get_geometry())
print(window.get_attributes())
