# MNIST_Digit_Recognition

This repository contains a Convolutional Neural Network (CNN) model for recognising handwritten digits using the MNIST dataset, along with a simple web-based front end for digit classification and a Flask backend for serving the model.

## **Overview**
The goal of this project is to create an easy-to-use application that enables users to drag and drop an image of a digit and receive a classification from the trained CNN model. The project consists of three main components:

**CNN Model**: A deep learning model built using TensorFlow and Keras, trained on the MNIST dataset for handwritten digit recognition. The model architecture includes multiple convolutional layers, pooling layers, dropout layers, and a fully connected dense layer to perform the classification task. The model achieves high accuracy in recognizing the digits from the dataset.

**Front-end**: A simple web interface built with HTML, CSS, and JavaScript, where users can draw digits and receive the classification results. The front-end features a canvas for drawing the digits, buttons for clearing the canvas or submitting the drawn digit, and a display area for showing the predicted digit class.

**Back-end**: A lightweight Flask server that serves the model and handles requests from the front-end. The server loads the trained CNN model and exposes an API for receiving digit images from the front-end. Upon receiving an image, the server preprocesses it and feeds it to the CNN model for prediction. The predicted digit is then sent back to the front-end to be displayed to the user.

## **Tech Stack, Algorithms, and Libraries**
The project utilizes a range of technologies, algorithms, and libraries to achieve its objectives:

## **Tech Stack**
* **Front-end**: HTML, CSS, and JavaScript

* **Back-end**: Flask (Python web framework)

* **Deep Learning**: TensorFlow and Keras

## **Algorithms**
* **Convolutional Neural Network (CNN)**: A deep learning algorithm used for image classification tasks, such as handwritten digit recognition. CNNs are highly effective in capturing spatial features and patterns within images, making them suitable for this project.

## **Libraries**
* **TensorFlow**: An open-source machine learning library developed by Google Brain, used to build and train the CNN model.

* **Keras**: A high-level deep learning API, built on top of TensorFlow, that simplifies the process of designing, building, and training neural networks.

* **Flask**: A lightweight web framework for Python, used to build the back-end server for serving the trained model and handling requests from the front-end.

* **NumPy**: A popular library for numerical computing in Python, used for various preprocessing tasks related to the input images.

* **Pillow**: A Python Imaging Library (PIL) fork that provides tools for opening, manipulating, and saving image files, used for processing the drawn digit images received from the front-end.

This project demonstrates the application of deep learning techniques to solve real-world problems and provides an interactive way to explore handwritten digit recognition using a powerful CNN model and a user-friendly interface.

