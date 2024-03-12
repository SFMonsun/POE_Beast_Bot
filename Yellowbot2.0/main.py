import pyautogui
import time
from pynput.mouse import Listener
import delete_red_Beast
import Beast_into_inventory
import Beast_into_stash
import cv2

from all_usedfunc.match_capture import capture_screen,match_template
from all_usedfunc.search_region import get_search_region_left_25,get_search_region_right_half
from all_usedfunc.escape_stop import should_continue

def on_click(x, y, button, pressed):
    if pressed:
        global X_Button
        X_Button = (x, y)
        return False  # Stop listener

print("Please click top X_Button...")
with Listener(on_click=on_click) as listener:
    listener.join()

clicked_position = X_Button
Top_yellow_beast_location = (X_Button[0]+40,X_Button[1]+60)
time.sleep(1)


delete_red_Beast.delete_read_beast_loop(X_Button)
while True:
    Beast_into_inventory.Beast_into_inventory_mainloop(Top_yellow_beast_location)
    time.sleep(1)
    Beast_into_stash.Beast_into_stash_mainloop()





#plan 
#red beast regex typen
#red beast deleten 
#stop when all deletet
#regex löschen

#yellow beast fillen
#stash code etc



