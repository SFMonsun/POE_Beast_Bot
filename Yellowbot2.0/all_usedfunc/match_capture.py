import cv2
import numpy as np
from PIL import ImageGrab

def capture_screen(region=None):
    screen = np.array(ImageGrab.grab(bbox=region))
    return screen


def match_template(screen, template, threshold=0.59):
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val > threshold:
        template_height, template_width = template.shape[:2]
        match_center_x = max_loc[0] + template_width // 2
        match_center_y = max_loc[1] + template_height // 2
        return (match_center_x, match_center_y)
    else:
        return None