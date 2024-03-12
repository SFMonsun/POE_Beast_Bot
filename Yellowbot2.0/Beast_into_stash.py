import pyautogui 
import time
import keyboard
import cv2
import sys

from all_usedfunc.escape_stop import should_continue
from all_usedfunc.match_capture import capture_screen,match_template
from all_usedfunc.search_region import get_search_region_left_25,get_search_region_right_half
#kekw look at the name
def click_on_stash(stash_image,search_area=None):
    time.sleep(1.5)
    screen = capture_screen(region=search_area)
    match_result = match_template(screen, stash_image)
    if match_result is not None:
     
        pyautogui.moveTo(match_result, duration=0.2)
        
        time.sleep(0.3)
        pyautogui.click()
    
        
    else:
        print("STASH NOT FOUND.")
        sys.exit()

#strg down and clicks on all orbs in inv
def move_filled_into_stash(filled_store_image,search_area):
    
    screen = capture_screen(search_area)
    match_result = match_template(screen, filled_store_image ,0.8)
    if match_result is not None:
        
        
        x_cord = match_result[0]
        x_cord = x_cord+960
        y_cord = match_result[1]
        pyautogui.keyDown('ctrl')
        pyautogui.moveTo(x_cord,y_cord, duration=0.12)
        pyautogui.keyDown('ctrl')
        
        pyautogui.click()
        return True
        
    else:
        
        
        return False
#Just is for checking if there is still stuff left in inv
def is_filled_store(filled_store_image,search_area):
    screen = capture_screen(search_area)
    result = match_template(screen,filled_store_image,0.8)
    if result is not None:
        return True
    return False

#just clicks on the beast sta tab
def click_on_stashtab(BEAST_STA_image,search_area=None):
    screen = capture_screen(region=search_area)
    
    
    match_result = match_template(screen, BEAST_STA_image)
    if match_result is not None:
        pyautogui.moveTo(match_result, duration=0.2)
        time.sleep(0.3)
        pyautogui.click()
        time.sleep(0.3)
        
        #time.sleep(0.01)
        
    else:
        print("beast sta STASH NOT FOUND")
        
        sys.exit()
def Beast_into_stash_mainloop():
    Stash_image = cv2.imread("Bilder\\stash_image.png")
    Filled_Beastary_Orb_image = cv2.imread("Bilder\\filledstore.png")
    Beast_Stash_Tab_image = cv2.imread("Bilder\\BEAST_STA.png")

    right_half_screen = get_search_region_right_half()

    click_on_stash(Stash_image)
    time.sleep(1)
    click_on_stashtab(Beast_Stash_Tab_image)
    for i in range(100):

        should_continue()
        #strg it into stash
        move_filled_into_stash(Filled_Beastary_Orb_image,right_half_screen)
       
        
        if(is_filled_store(Filled_Beastary_Orb_image,right_half_screen) == False):
            pyautogui.keyUp('ctrl')
            pyautogui.press('h')
            break
        else:
            print("True")
