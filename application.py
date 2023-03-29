import io
import base64
from PIL import Image, ImageOps
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
import numpy as np

application = Flask(__name__)
CORS(application)
model = load_model('cnn2_model.h5')

@application.route('/')
def home():
    return render_template('front.html')

@application.route('/api/predict', methods=['POST'])
def predict():
    # Get the base64 image data from the request
    image_data = request.json['image']
    image_data = base64.b64decode(image_data.split(',')[1])

    # Load the image and preprocess it
    image = Image.open(io.BytesIO(image_data))
    image = image.convert('L') # Convert to grayscale
    image = ImageOps.invert(image)  # Invert the colors to black background and white number
    image = image.resize((28, 28), Image.LANCZOS) # Resize the image to 28x28
    image_array = np.asarray(image).reshape(1, 28, 28, 1) / 255.0 #  Convert to NumPy array, flatten, and normalize

    # Predict the digit
    prediction = model.predict(image_array)
    output = np.argmax(prediction)

    return jsonify({"digit": int(output)})

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
