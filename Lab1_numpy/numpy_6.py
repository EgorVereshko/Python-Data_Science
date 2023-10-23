import numpy as np
import cv2


def draw_rectangle(image, x, y, width, height, background_color, rectangle_color):
    background_color = tuple(background_color)
    rectangle_color = tuple(rectangle_color)

    cv2.rectangle(image, (x, y), (x + width, y + height), background_color, -1)
    cv2.rectangle(image, (x, y), (x + width, y + height), rectangle_color, 2)

    return image


def draw_ellipse(image, center_x, center_y, a, b, background_color, ellipse_color):
    background_color = tuple(background_color)
    ellipse_color = tuple(ellipse_color)

    cv2.ellipse(image, (center_x, center_y), (a, b), 0, 0, 360, background_color, -1)
    cv2.ellipse(image, (center_x, center_y), (a, b), 0, 0, 360, ellipse_color, 2)

    return image


image = np.zeros((400, 400, 3), dtype=np.uint8)

image = draw_rectangle(image, 50, 50, 200, 100, (0, 255, 255), (250, 0, 0))

image = draw_ellipse(image, 250, 250, 100, 50, (0, 0, 255), (0, 255, 0))

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
