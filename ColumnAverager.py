"""
 * Python program to take the column average of an image.
 *
"""
import cv2
import matplotlib.pyplot as plt

imagePath = r'/Users/gabriel/L1R_data/STRIPES.tif'

# reading in the image
src = cv2.imread(imagePath)

# displaying image
windowName = 'image'

cv2.imshow(windowName, src)

h, w, c = src.shape
print('Image size: ')
print('Width:  ', w)
print('Height: ', h)
print(f'Channels: {c}\n')

idx = 0
means = [0]*w
count = [0]*w
while (idx < w):
    means[idx] = src[:,idx].mean()
    count[idx] = idx + 1
    idx += 1

# plotting
plt.plot(count, means)
plt.xlabel('Column')
plt.ylabel('Column Mean')
plt.title('Column Average')
plt.show()

# waits for user to press any key
# # (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)
