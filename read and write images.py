
import matplotlib.pyplot as plt

plt.figure()
img = plt.imread('C:/Users/Serkan/PycharmProjects/panda/scipy-lecture-notes-2017.1.1/data/elephant.png')
img_red = img[:, :, 0]
plt.imshow(img_red, cmap=plt.cm.gray)
img_tiny = img[::6, ::6]
plt.imshow(img_tiny, interpolation='nearest')

plt.show()
