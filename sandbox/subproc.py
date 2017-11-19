'''
retrieving window id
'''

import os
import signal
import subprocess
import time
from Xlib.display import Display



def find_by_id(window, target_id):
    print(window.id, target_id)
    if window.id == target_id:
        return window
    children = window.query_tree().children
    for w in children:
        res = find_by_id(w, target_id)
        if res is not None:
            return res


p = subprocess.Popen(['gnome-terminal'])

print(p.pid)

display = Display()
root = display.screen().root
window = find_by_id(root, p.pid)
print(window)
#print(window.get_wm_class())
print(0x1400003)
time.sleep(5)
os.killpg(os.getpgid(p.pid), signal.SIGTERM)

'''
something like this
command = "xprop -root _NET_ACTIVE_WINDOW"
output = subprocess.Popen(["/bin/bash", "-c", command], stdout=subprocess.PIPE)
frontmost = output.communicate()[0].decode("utf-8").strip().split()[-1]
'''
