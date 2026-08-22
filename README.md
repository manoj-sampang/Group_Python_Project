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

