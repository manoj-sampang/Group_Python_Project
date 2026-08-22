

import tensorflow as tf

# loading the keras dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

#normalize pixel values of the dataset
x_train = x_train/255
x_test = x_test/255

#buidling CNN
model = tf.keras.Sequential()

model.add(tf.keras.Input(shape=(32, 32, 3)))
model.add(
    tf.keras.layers.Conv2D(
        32,
        (3, 3),
        activation="relu",
    )
)

model.add(
    tf.keras.layers.MaxPooling2D((2, 2))
)

model.add(
    tf.keras.layers.Conv2D(
        64,
        (3, 3),
        activation="relu"
    )
)

model.add(
    tf.keras.layers.MaxPooling2D((2, 2))
)

model.add(
    tf.keras.layers.Flatten()
)

model.add(
    tf.keras.layers.Dense(
        64,
        activation="relu"
    )
)

model.add(
    tf.keras.layers.Dense(
        10,
        activation="softmax"
    )
)

#model architecture
model.summary()

#configure learning 
model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
)

#Training

history = model.fit(
        x_train,
        y_train,
        epochs=10,
        validation_data=(x_test, y_test)
)
