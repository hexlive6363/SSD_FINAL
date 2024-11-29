from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the model and vectorizer from the pickle file
model, vectorizer = pickle.load(open('Lates.pkl', 'rb'))

# Check the loaded objects
print(f"Model type: {type(model)}")
print(f"Vectorizer type: {type(vectorizer)}")

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    # Get the input data from the form
    data1 = request.form['a']

    # Transform the input using the vectorizer
    input_vector = vectorizer.transform([data1])

    # Predict the sentiment
    prediction = model.predict(input_vector)[0]
    print(prediction) 
    return render_template('after.html', data=prediction)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
