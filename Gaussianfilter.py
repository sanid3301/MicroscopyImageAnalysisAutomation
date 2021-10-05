from skimage import io, filters
from matplotlib import pyplot as plt

def gaussian_of_image (img, sigma = 1):
    g_image = filters.gaussian(img,sigma)
    return (g_image)

my_image = io.imread ('D:/Academics/IITD/7th Sem/BTP/Image Data/2.jpg')

filtered = gaussian_of_image(my_image,3)

plt.imshow(filtered)
plt.imshow(my_image)

