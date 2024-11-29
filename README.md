# Tweet Sentiment Analysis

This project analyzes tweet sentiments (HAPPY or SAD) using a trained machine learning model. It includes a front-end interface for displaying predictions and a back-end for model inference and training.

---

## Project Structure
```
├── app.py
├── basics.py
├── LATEST_NOV.pkl
├── model_training.ipynb
├── Procfile
├── README.md
├── requirements.txt
├── static
│   ├── class_distribution.jpg
│   ├── confusion_matrix.jpg
│   ├── distribution_curve.jpg
│   ├── happy.jpg
│   ├── learning_curve.jpg
│   ├── precision_recall_curbve.jpg
│   ├── ROC.jpg
│   └── sad.jpg
├── templates
│   ├── after.html
│   └── home.html
```


---

## Features

1. **Sentiment Prediction**:
   - Predicts if a tweet expresses a HAPPY or SAD sentiment.
   - Displays the result visually using images or GIFs.

2. **Model Training**:
   - `model_training.ipynb` includes code for training the sentiment analysis model.
   - Evaluation metrics such as confusion matrix, precision-recall curve, ROC curve, etc., are included.

3. **Front-End**:
   - Uses Flask and HTML templates for user interaction.
   - Provides a clean and interactive UI for entering tweets and viewing predictions.
---

## Installation and Setup

### Prerequisites

- Python 3.8 or above
- `pip` package manager
- Virtual environment (`venv`)

### Step 1: Clone the Repository

```bash
git clone <repository_url>
cd <repository_folder>
```

### Step 2: Create and Activate a Virtual Environment

* Create the virtual environment
```
python3 -m venv venv
```

* Activate the virtual environment
```
source venv/bin/activate
```

### Step 3: Install Required Dependencies
Install the dependencies listed in requirements.txt
```
pip install -r requirements.txt
```

### Step 4: Run the Flask Application
Start the Flask server by running
```
python app.py
```

The app will be accessible at http://10.42.0.198:5000/

---
## How to Run

* Open your browser and go to http://10.42.0.198:5000/.
* Enter a tweet in the input field on the homepage.
* Submit the tweet to analyze its sentiment.
* View Results:

The app will display whether the sentiment is HAPPY or SAD, accompanied by a visual representation (image).
 
---