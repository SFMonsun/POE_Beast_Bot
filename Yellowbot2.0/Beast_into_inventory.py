import pyautogui
import time
import sys
import cv2

#function imports

from all_usedfunc.match_capture import capture_screen,match_template
from all_usedfunc.search_region import get_search_region_left_25,get_search_region_right_half
from all_usedfunc.escape_stop import should_continue
#NEED TO BE A NEW ONE
def Yellow_finder(images, search_area):
    screen = capture_screen(region=search_area)
    for image in images:
        result = match_template(screen, image)
        if result is not None:
            return True
    return False

def Yellow_beast_clicker(Top_yellow_beast_location):
    
    pyautogui.moveTo(Top_yellow_beast_location,duration = 0.12)
    time.sleep(0.2)
    pyautogui.click()
    
#finds bestariy orb and picks it up
def store(store_image):
    #cv2.imshow('test',store_image)
    screen = capture_screen()
    match_result = match_template(screen, store_image, 0.82)
    if match_result is not None:
       

        pyautogui.moveTo(match_result,duration=0.12)
        time.sleep(0.05)
        pyautogui.click(button='right')
    else:
        height = 1920
        width = 1080
        pyautogui.moveTo(height / 2, width / 2,duration=0.12)
        time.sleep(1)
        screen = capture_screen()
        match_result = match_template(screen, store_image, 0.82)
        if(match_result is None):
            print("no store found")
            sys.exit()
        else:store(store_image)
#just checks if there is still storage left in inv
def inv_finder(inv2png,search_area=None):
    screen = capture_screen(region=search_area)
    
    result = match_template(screen,inv2png)
    if result is not None:
        return True
    return False

def inv(inv2png,right_half_screen):
    
    screen = capture_screen(region=right_half_screen)
    match_result = match_template(screen, inv2png)

    if match_result is not None:
        x_cord = match_result[0]
        x_cord = x_cord+960
        y_cord = match_result[1]
        pyautogui.moveTo(x_cord,y_cord, duration=0.12)
        pyautogui.click()
       



def Beast_into_inventory_mainloop(Top_yellow_beast_location):
    

    right_half_screen = get_search_region_right_half()
    Empty_Beast_Orb_Image = cv2.imread("Bilder\\store.png")
    Inventory_slot_image = cv2.imread("Bilder\\inv2.png")
    while True:

        should_continue()
        
        #picks orb
        store(Empty_Beast_Orb_Image)
        #clicks on beast with it
        Yellow_beast_clicker(Top_yellow_beast_location)
        #puts in inv
        inv(Inventory_slot_image,right_half_screen)
        if(inv_finder(Inventory_slot_image,right_half_screen) == False):
            break
        should_continue()

