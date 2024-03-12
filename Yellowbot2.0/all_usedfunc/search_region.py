import pyautogui
#search region for beast in bestariy
def get_search_region_left_25():
    screen_width, screen_height = pyautogui.size()
    region_width = int(screen_width * 2 / 5)  # Calculate 2/5 of screen width
    search_region = (0, 0, region_width, screen_height)  # Region covers left 2/5 of screen
    return search_region

def get_search_region_right_half():
    screen_width, screen_height = pyautogui.size()
    region_start_x = int(screen_width / 2)  # Start from the middle of the screen
    
    # Calculate the right edge of the screen
    region_end_x = screen_width  # The right edge of the screen

    # The region now is (x, y, x2, y2)
    search_region = (region_start_x, 0, region_end_x, screen_height)  # Region covers right half of the screen

    return search_region