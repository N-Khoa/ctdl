# import cv2
# from google.colab.patches import cv2_imshow

# cat_image = cv2.imread("/content/binary_cat.png",0)
# cv2_imshow(cat_image)

# counts = dict()
# height, width = cat_image.shape
# for row in range(height):
#   for col in range(width):
#       counts[cat_image[row,col]] = counts.get(cat_image[row,col],0) + 1

# print('Counts', counts)

# import matplotlib.pyplot as plt

# names = list(counts.keys())
# values = list(counts.values())

# plt.bar(range(len(counts)), values, tick_label=names)
# plt.show()