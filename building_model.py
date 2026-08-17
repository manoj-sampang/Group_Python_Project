

import tensorflow as tf

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

model.summary()
