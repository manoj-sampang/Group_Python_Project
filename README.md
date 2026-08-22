# Project Title
    Project on [IMAGE RECOGNITION] using CIFAR 10 dataset which have 10 classes of images to recognize 


# Project Structure
    Group_Python_Project
    |
    |-- .venv/                      *** virtual environment so the packages/libraries are not scattered ***
    |-- main.py                     *** the src code for the project where the python code resides *** 
    |-- manual_image_classifier.py  
    |-- requirements.txt            *** lists all the external libraries and dependencies required ***
    |-- README.md                   *** documentation of the project ***
    |-- .gitignore                  *** here, resides the ignored folder and file while pushing to git ***

# Installation
    ### Firstly, activate the virtual environment 
        - python3.13.14 -m venv .venv 
            # windows : .venv/Scripts/activate
            # mac/linux : source .venv/bin/activate

    ### Install the dependencies used 
        - tensorflow, numpy and matplotlib  ###used 
            # pip install -r requirements.txt
 
    - used for storing images efficiently   ### Numpy

    - used for displaying images    ### Matplotlib

    - AI library to implement neural networks provides ready-made building blocks   ### Tensorflow


# Advanced Concepts
    # CNN models
        - initially, before building the model we need to understand how datasets are divided and how Convolutional 
          Neural Network works ### tensorflow, keras 

        - here, datasets are divided into 50,000 images for training the model and 10,000 for testing the model for 
          accuracy, seeing how efficient is the model on those training data.

        ### Dataset Structure 
            -- here each image is 32 x 32 pixels horizontal and vertical with each pixel with its (R,G,B) values,
               so, our structure of the dataset is typcially (50,000 images, 32 row pixels, 32 column pixels, 3 colors)
               which would be 4-dimensional numpy array.
               for only training the data on, those are just numeric values/colors representing each pixel.

               
            Inside the dataset
                    | 
                    |--1st image 
                    |    |
                    |    |-- 1st row
                    |    |       | 
                    |    |       |-- 1st column
                    |    |       |       |
                    |    |       |       |--[R, G, B]
                    |    |       |
                    |    |       |
                    |    |       |--2nd column
                    |    |       .       |
                    |    |       .       |--[R, G, B]
                    |    |       .   
                    |    |       |
                    |    |       |
                    |    |       |--32 column
                    |    |               |
                    |    |               |--[R, G, B]
                    |    |
                    |    |
                    |    |-- 2nd row
                    |    |       | 
                    |    |       |-- 1st column
                    |    |       |       |
                    |    |       |       |--[R, G, B]
                    |    |       |
                    |    |       |
                    |    |       |--2nd column
                    |    |       .       |
                    |    |       .       |--[R, G, B]
                    |    |       .
                    |    |       |
                    |    |       |
                    |    |       |--32 column
                    |    |               |
                    |    |               |--[R, G, B]
                    |    |
                    |    |
                    |    .
                    |    .
                    |    .
                    |    |-- 32 row
                    |            | 
                    |            |-- 1st column
                    |            |       |
                    |            |       |--[R, G, B]
                    |            |
                    |            |
                    |            |--2nd column
                    |            .       |
                    |            .       |--[R, G, B]
                    |            .
                    |            |
                    |            |
                    |            |--32 column
                    |                    |
                    |                    |--[R, G, B]
                    |
                    .
                    .
                    .
                    |--50,000th image
                            |
                            |-- 1st row
                            |       | 
                            |       |-- 1st column
                            |       |       |
                            |       |       |--[R, G, B]
                            |       |
                            |       |
                            |       |--2nd column
                            |       .       |
                            |       .       |--[R, G, B]
                            |       .   
                            |       |
                            |       |
                            |       |--32 column
                            |               |
                            |               |--[R, G, B]
                            |
                            |
                            |-- 2nd row
                            |       | 
                            |       |-- 1st column
                            |       |       |
                            |       |       |--[R, G, B]
                            |       |
                            |       |
                            |       |--2nd column
                            |       .       |
                            |       .       |--[R, G, B]
                            |       .
                            |       |
                            |       |
                            |       |--32 column
                            |               |
                            |               |--[R, G, B]
                            |
                            |
                            .
                            .
                            .
                            |-- 32 row
                                    | 
                                    |-- 1st column
                                    |       |
                                    |       |--[R, G, B]
                                    |
                                    |
                                    |--2nd column
                                    .       |
                                    .       |--[R, G, B]
                                    .
                                    |
                                    |
                                    |--32 column
                                            |
                                            |--[R, G, B]


                            
                            #Similarly, each image has its own label representing any equivalent value that corresponds to
                             one of its 10 classes, here there are 50,000 labels for all of those 50,000 images, so there                                would be 50,000 labels in a single column which is represented (50,000 labels, 1 column) so,                                that would be 2-dimensional array/ndarray.
                             for all of those 50,000 images each label corresponds to the respective image classes.

                             --label Structure
                                    |
                                    |
                                    |-1st       [value(0-9)]
                                    |
                                    |-2nd       [value(0-9)]
                                    |
                                    |-3rd       [value(0-9)]
                                    .
                                    .
                                    .
                                    |-50,000th  [value(0-9)]

        
        ### CNN (Convolutional Neural Network)

            A Convolutional Neural Network is a neural network architecture commonly used for image-related tasks.

            Instead of directly treating an entire image as one long list of numbers, CNNs process small regions of the 
            image using kernels (filters). These kernels learn useful patterns from the images during training.

            ### Convolution

                CIFAR-10 images have the shape:

                    32 × 32 × 3

                where:
                    32 → image height
                    32 → image width
                     3 → RGB channels

                A 3 × 3 kernel is used to examine small regions of the image.

                Since the image has three RGB channels, a kernel actually has the shape:

                    3 × 3 × 3

                The kernel contains weights. These weights are multiplied with the corresponding pixel values in the 
                selected region and the results are combined to produce an output value.

                The kernel then moves across the image and repeats this operation for different regions.

                For a 32 × 32 image with a 3 × 3 kernel and no padding:

                    32 - 3 + 1 = 30

                Therefore, the resulting feature map has:

                    30 × 30

                output positions for one kernel.

            ### Multiple Kernels

                A CNN does not use only one kernel. Our first convolutional layer uses 32 kernels.

                    1 kernel  → 30 × 30 feature map
                    32 kernels → 30 × 30 × 32 feature maps

                Each kernel has its own weights and can learn to respond to different patterns in the images.

            ### Max Pooling

                After convolution, MaxPooling is used to reduce the spatial dimensions of the feature maps.

                A 2 × 2 pooling window examines a small region and keeps the maximum value.

                    30 × 30 × 32
                            ↓
                    MaxPooling(2 × 2)
                            ↓
                    15 × 15 × 32

                This reduces the amount of data while retaining strong feature responses.

            ### Second Convolution

                The second convolutional layer uses 64 kernels.

                    15 × 15 × 32
                            ↓
                    Conv2D(64, 3 × 3)
                            ↓
                    13 × 13 × 64

                The 64 kernels can learn additional and more complex features from the feature maps produced by the 
                previous layer.

            ### Flatten

                After the convolution and pooling operations, the feature maps are converted into a one-dimensional array.

                    6 × 6 × 64
                        ↓
                    Flatten
                        ↓
                      2304

            ### Dense Layers

                The flattened 2304 values are passed to a Dense layer containing 64 neurons.

                    2304 → 64

                Finally, another Dense layer contains 10 neurons because CIFAR-10 contains 10 classes.

                    64 → 10

                The final layer produces the model's predictions for the ten
                CIFAR-10 classes.
