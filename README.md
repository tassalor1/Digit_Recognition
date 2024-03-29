# Digit_Recognition

## ** Currently Offline **
This repository contains a Convolutional Neural Network model for recognising handwritten digits using the MNIST dataset, deployed on an AWS EC2 instance using Nginx as a reverse proxy server and Flask as a web framework.

## **Overview**
The goal of this project is to create an easy-to-use application that enables users to input a digit image through drag and drop and receive a classification from the trained CNN model. The project consists of three main components:

**CNN Model**: A deep learning model built using TensorFlow and Keras, trained on the MNIST dataset for handwritten digit recognition. The model architecture includes multiple convolutional layers, pooling layers, dropout layers, and a fully connected dense layer to perform the classification task. The model achieves a 98.93% test accuracy score in recognising the digits from the dataset.

**Front-end**: A simple web interface built with HTML, CSS, and JavaScript, where users can drag and drop digit images and receive the classification results.The design is styled using the [98.css](https://jdan.github.io/98.css/#table-view) library, which gives the interface a retro Windows 98-inspired appearance, and incorporates icons from the [Win98 Icons](https://win98icons.alexmeub.com/)
 collection for a consistent vintage look.

**Back-end**: A lightweight Flask server that serves the model and handles requests from the front-end. The server loads the trained CNN model and exposes an API for receiving digit images from the front-end. Upon receiving an image, the server preprocesses it and feeds it to the CNN model for prediction. The predicted digit is then sent back to the front-end to be displayed to the user.

## **Tech Stack, Algorithms, and Libraries**
The project utilises a range of technologies, algorithms, and libraries to achieve its objectives:

## **Tech Stack**
* **Front-end**: HTML, CSS, and JavaScript

* **Back-end**: Flask 

* **Deep Learning**: Python, TensorFlow and Keras

## **Algorithms**
* **Convolutional Neural Network (CNN)**: A deep learning algorithm used for image classification tasks, such as handwritten digit recognition. CNNs are highly effective in capturing spatial features and patterns within images, making them suitable for this project.

## **Libraries**
* **TensorFlow**
* **Keras**
* **Flask**
* **NumPy**
* **Pillow**
* **98.css**

This project demonstrates the application of deep learning techniques to solve real-world problems and provides an interactive way to explore handwritten digit recognition using a powerful CNN model and a user-friendly interface.



