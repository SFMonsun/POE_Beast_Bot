import cv2
import numpy as np
from PIL import ImageGrab

def capture_screen(region=None):
    screen = np.array(ImageGrab.grab(bbox=region))
    return screen

def show_matches(template, threshold):
    screen = capture_screen()
    w, h = template.shape[1], template.shape[0]

    # Perform match
    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    # Draw rectangles around matches and dots at their centers
    for pt in zip(*loc[::-1]):
        cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
        center_x = pt[0] + w // 2
        center_y = pt[1] + h // 2
        cv2.circle(screen, (center_x, center_y), 5, (255, 0, 0), -1)

    # Display the result
    cv2.imshow('Matched Areas', screen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

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

# Usage example
template = cv2.imread("Bilder\\finished_delete.JPG")
resultloc = match_template(capture_screen(), template)
print(resultloc)

show_matches(template, 0.8)



#0.57 for store