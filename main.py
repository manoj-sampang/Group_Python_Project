# Project on Image Classfication (CIFAR-10)

# loading the data_set from tensorflow keras

from tensorflow.keras.datasets import cifar10


(x_train, y_train), (x_test, y_test) = cifar10.load_data()

print(type(x_train))
print(type(y_train))
print(type(x_test))
print(type(y_test))





