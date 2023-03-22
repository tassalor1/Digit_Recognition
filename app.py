import io
import base64
from PIL import Image
from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)
model = pickle.load(open('random_forest_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('front.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the base64 image data from the request
    image_data = request.json['image']
    image_data = base64.b64decode(image_data.split(',')[1])

    # Load the image and preprocess it
    image = Image.open(io.BytesIO(image_data))
    image = image.convert('L') # Convert to grayscale
    image = image.resize((28, 28), Image. LANCZOS) # Resize the image to 28x28
    image_array = np.asarray(image).reshape(1, -1) # Convert to NumPy array and flatten

    # Predict the digit
    prediction = model.predict(image_array)
    output = int(prediction[0])

    return jsonify({"digit": output})

if __name__ == "__main__":
    app.run(port=5000, debug=True)

