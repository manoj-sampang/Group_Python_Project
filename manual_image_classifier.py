
import tensorflow as tf
import matplotlib.pyplot as plt


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

class_names = [
    "airplane",
    "automobile",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck"
]
def count_each_classes():
    count = {}
    for i in range(10):
        count[i] = 0
    for label in y_train:
        label = label[0]             
        count[label] += 1 
    return count

def image_count_display(image_dict):
   
    for i in range(10):
        print(f"{class_names[i]} -> {image_dict[i]} images ")
def show_image(index_image):
    plt.imshow(x_train[index_image])
    plt.title(class_names[y_train[index_image][0]])
    plt.axis("off")
    plt.show()

def validity_check(index_image):
    if index_image >= 0:
        if index_image < 50000:
            return True
    return False
print(" ==== Image Classifer through index provided using cifar10 datasets ==== ")

print(" Information about the Datasets")

image_dict = count_each_classes()
image_count_display(image_dict)




index_image = int(input("Enter index through (0 - 49999): "))

if validity_check(index_image):
    show_image(index_image)

else: 
    print("Invalid Index format")





