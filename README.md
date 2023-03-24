# Digit_Recognition

This repository contains a Convolutional Neural Network (CNN) model for recognising handwritten digits using the MNIST dataset, along with a simple web-based front end for digit classification and a Flask backend for serving the model.

## **Overview**
The goal of this project is to create an easy-to-use application that enables users to input a digit image through drag and drop and receive a classification from the trained CNN model. The project consists of three main components:

**CNN Model**: A deep learning model built using TensorFlow and Keras, trained on the MNIST dataset for handwritten digit recognition. The model architecture includes multiple convolutional layers, pooling layers, dropout layers, and a fully connected dense layer to perform the classification task. The model achieves a 98.93% test accuracy score in recognizing the digits from the dataset.

**Front-end**: A simple web interface built with HTML, CSS, and JavaScript, where users can drag and drop digit images and receive the classification results.

**Back-end**: A lightweight Flask server that serves the model and handles requests from the front-end. The server loads the trained CNN model and exposes an API for receiving digit images from the front-end. Upon receiving an image, the server preprocesses it and feeds it to the CNN model for prediction. The predicted digit is then sent back to the front-end to be displayed to the user.

## **Tech Stack, Algorithms, and Libraries**
The project utilizes a range of technologies, algorithms, and libraries to achieve its objectives:

## **Tech Stack**
* **Front-end**: HTML, CSS, and JavaScript

* **Back-end**: Flask (Python web framework)

* **Deep Learning**: Python, TensorFlow and Keras

## **Algorithms**
* **Convolutional Neural Network (CNN)**: A deep learning algorithm used for image classification tasks, such as handwritten digit recognition. CNNs are highly effective in capturing spatial features and patterns within images, making them suitable for this project.

## **Libraries**
* **TensorFlow**

* **Keras**

* **Flask**

* **NumPy**

* **Pillow**

This project demonstrates the application of deep learning techniques to solve real-world problems and provides an interactive way to explore handwritten digit recognition using a powerful CNN model and a user-friendly interface.

