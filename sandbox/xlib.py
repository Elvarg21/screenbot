'''
requires
pip install python3_xlib
'''


from Xlib.display import Display

def printWindowHierrarchy(window, indent):
    children = window.query_tree().children
    '''if window.get_wm_class() is not None and window.get_wm_class()[0] == 'firefox':
        #print(window.get_geometry())
        #window.destroy()
        print(window.get_wm_class(), children[0].get_wm_class())
    '''
    #print(type(window))
    att = window.get_attributes()
    wm = window.get_wm_class()
    #if wm is not None and wm[1] == 'Chromium-browser':
    #print(str(att))
    #print(wm)
    if wm is not None and wm[1] == 'Chromium-browser':
        print(wm)
        print(window.get_attributes())
        #print(window.get_image(12, 23, 10, 10, 1, None))
    for w in children:
        #print(indent, window.get_wm_class())
        printWindowHierrarchy(w, indent+'-')
    #window.destroy()

display = Display()
root = display.screen().root
printWindowHierrarchy(root, '-')


'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__drawable__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt_
_', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__resource__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '__window_
_', '_get_struct_prop', '_set_struct_prop', 'arc', 'change_attributes', 'change_property', 'change_save_set', 'circulate', 'clear_area', 'composite_create_region_from_border_clip', 'c
omposite_name_window_pixmap', 'composite_redirect_subwindows', 'composite_redirect_window', 'composite_unredirect_subwindows', 'composite_unredirect_window', 'configure', 'convert_sel
ection', 'copy_area', 'copy_plane', 'create_colormap', 'create_gc', 'create_pixmap', 'create_window', 'delete_property', 'destroy', 'destroy_sub_windows', 'display', 'draw_text', 'fil
l_arc', 'fill_poly', 'fill_rectangle', 'get_attributes', 'get_full_property', 'get_geometry', 'get_image', 'get_motion_events', 'get_property', 'get_wm_class', 'get_wm_client_machine'
, 'get_wm_colormap_windows', 'get_wm_hints', 'get_wm_icon_name', 'get_wm_icon_size', 'get_wm_name', 'get_wm_normal_hints', 'get_wm_protocols', 'get_wm_state', 'get_wm_transient_for',
'grab_button', 'grab_key', 'grab_keyboard', 'grab_pointer', 'id', 'image_text', 'image_text_16', 'kill_client', 'line', 'list_installed_colormaps', 'list_properties', 'map', 'map_sub_
windows', 'owner', 'point', 'poly_arc', 'poly_fill_arc', 'poly_fill_rectangle', 'poly_line', 'poly_point', 'poly_rectangle', 'poly_segment', 'poly_text', 'poly_text_16', 'put_image',
'put_pil_image', 'query_best_size', 'query_pointer', 'query_tree', 'raise_window', 'rectangle', 'reparent', 'rotate_properties', 'send_event', 'set_input_focus', 'set_selection_owner'
, 'set_wm_class', 'set_wm_client_machine', 'set_wm_colormap_windows', 'set_wm_hints', 'set_wm_icon_name', 'set_wm_icon_size', 'set_wm_name', 'set_wm_normal_hints', 'set_wm_protocols',
 'set_wm_state', 'set_wm_transient_for', 'shape_combine', 'shape_get_rectangles', 'shape_input_selected', 'shape_mask', 'shape_offset', 'shape_query_extents', 'shape_rectangles', 'sha
pe_select_input', 'translate_coords', 'ungrab_button', 'ungrab_key', 'unmap', 'unmap_sub_windows', 'warp_pointer', 'xinerama_get_screen_count', 'xinerama_get_screen_size', 'xinerama_g
et_state', 'xrandr_1_0set_screen_config', 'xrandr_create_mode', 'xrandr_get_output_primary', 'xrandr_get_screen_info', 'xrandr_get_screen_resources', 'xrandr_get_screen_resources_curr
ent', 'xrandr_get_screen_size_range', 'xrandr_select_input', 'xrandr_set_output_primary', 'xrandr_set_screen_config', 'xrandr_set_screen_size', 'xtest_compare_cursor']
'''
