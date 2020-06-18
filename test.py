import cv2
import numpy as np 

img = cv2.imread('img1.jpg', 0)
mask = cv2.imread('mask.png', 0)

# flood fill to remove mask at borders of the image
h, w = img.shape[:2]
for row in range(h):
    if mask[row, 0] == 255:
        cv2.floodFill(mask, None, (0, row), 0)
    if mask[row, w-1] == 255:
        cv2.floodFill(mask, None, (w-1, row), 0)
for col in range(w):
    if mask[0, col] == 255:
        cv2.floodFill(mask, None, (col, 0), 0)
    if mask[h-1, col] == 255:
        cv2.floodFill(mask, None, (col, h-1), 0)

# flood fill background to find inner holes
holes = mask.copy()
cv2.floodFill(holes, None, (0, 0), 255)

# invert holes mask, bitwise or with mask to fill in holes
holes = cv2.bitwise_not(holes)
mask = cv2.bitwise_or(mask, holes)

# display masked image
masked_img = cv2.bitwise_and(img, img, mask=mask)
masked_img_with_alpha = cv2.merge([img, img, img, mask])

cv2.imwrite('masked.png', masked_img)
cv2.imwrite('masked_transparent.png', masked_img_with_alpha)