url = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/CV0101/Images/Donald_Trump_Justin_Trudeau_2017-02-13_02.jpg' 

import urllib.request
from matplotlib import pyplot as plt
from pylab import rcParams

def plot_image(image_url, size=(12, 9)):
   
 urllib.request.urlretrieve(image_url, "exercise_image.jpg") 
    exercise_image = cv2.imread("exercise_image.jpg")

    if len(exercise_image.shape) == 3:
        exercise_image = cv2.cvtColor(exercise_image, cv2.COLOR_BGR2RGB)
 
    rcParams['figure.figsize'] = size[0], size[1]
    plt.axis("off")
    plt.imshow(exercise_image, cmap="Greys_r")
    plt.show()

plot_image(url)
--->https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/CV0101/Images/Donald_Trump_Justin_Trudeau_2017-02-13_02.jpg