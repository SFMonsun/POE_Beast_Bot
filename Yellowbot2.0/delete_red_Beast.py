import pyautogui
import time
import keyboard
import sys
import cv2
import pyperclip

from all_usedfunc.escape_stop import should_continue
from all_usedfunc.match_capture import capture_screen,match_template
from all_usedfunc.search_region import get_search_region_left_25,get_search_region_right_half
#plan 
#red beast regex typen
#red beast deleten 
#stop when all deletet
#regex löschen

def type_regex():
    search_area = get_search_region_left_25
    screen = capture_screen()#region = search_area
    templateimage = cv2.imread("Bilder\\regex_field.jpg")
    center_regex_field = match_template(screen,templateimage)
    return center_regex_field

def delete_read_beast_loop(X_Button):
    center_regex_field = type_regex()
    pyautogui.moveTo(center_regex_field,duration=0.14)
    time.sleep(1)
    pyautogui.click()
    pyperclip.copy("(Farric|Saqawine|Fenumal|Craicic) (?!Presence)")
    pyautogui.hotkey("ctrl", "v")


    iteration_counter = 0  
    check_frequency = 15
    while True:
        should_continue()
        pyautogui.moveTo(X_Button,duration=0.15)
        pyautogui.click()
        time.sleep(0.05)
        pyautogui.hotkey("enter")
        should_continue()

        iteration_counter += 1
        
        if iteration_counter >= check_frequency:
            screen = capture_screen()
            if(match_template(screen,cv2.imread("Bilder\\finished_delete.jpg"),0.95)):
                break  # Break the loop if the condition is met
            iteration_counter = 0  # Reset the counter
    
    screen = capture_screen()
    templateimage = cv2.imread("Bilder\\x_finished_delete.jpg")
    center_regex_xbutton = match_template(screen,templateimage,0.9)
    pyautogui.moveTo(center_regex_xbutton,duration=0.16)
    time.sleep(0.5)
    pyautogui.click()






    
