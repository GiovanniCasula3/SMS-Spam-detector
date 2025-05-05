# SMS Spam Detector

A machine learning application that detects whether an SMS message is spam or not.

## Disclaimer

This model has significant potential for improvement with access to a larger and more diverse dataset. At its current stage, it is still possible to craft spam messages that bypass the classifier. However, the current performance is quite impressive considering the model was trained on just 500 KB of data.

## Features

- Real-time SMS message classification
- Simple and intuitive web interface
- Machine learning model trained on a dataset of spam and non-spam messages
- High accuracy in detecting spam messages

## Technologies Used

- Python 3
- Flask (Web Framework)
- scikit-learn (Machine Learning)
- TF-IDF Vectorization
- Support Vector Machine (SVM) classifier
- HTML/CSS/JavaScript

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/GiovanniCasula3/SMS-Spam-detector 
   cd sms-spam-detector
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your browser and navigate to:
   ```
   http://localhost:8080
   ```

## Usage

1. Enter an SMS message in the text field
2. Click the "Check" button
3. The application will classify the message as either "Normal Message" or "Spam"

### Programmatic Usage

If you want to use the model directly from Python, here is how you can do it:

```python
from joblib import load

# Load model and vectorizer (assuming you've saved them)
classifier = load("model.joblib")
vectorizer = load("vectorizer.joblib")

message = "Congratulations! You've won a prize. Click here to claim."
vector = vectorizer.transform([message])
prediction = classifier.predict(vector)[0]
print("Spam" if prediction != "ham" else "Messaggio normale")
```

## Web Interface Examples

### Example 1: Normal Message (Ham)
Input:
```
Hey, what time are we meeting for dinner tonight?
```
Output:
```
Normal message, or Ham
```

### Example 2: Spam Message
Input:
```
CONGRATULATIONS! You've been selected to receive a free iPhone 13. Click here to claim your prize now: http://bit.ly/claim-prize
```
Output:
```
Spam
```

### Example 3: Normal Message (Ham)
Input:
```
Your Uber will arrive in 3 minutes. Driver: Marco, License plate: AB123CD
```
Output:
```
Messaggio normale
```

### Example 4: Spam Message
Input:
```
URGENT: Your bank account has been suspended. Call this number immediately to verify your identity: +1234567890
```
Output:
```
Spam
```

## Project Structure

- `app.py`: Main application file containing the Flask server and ML model
- `Data/spam.csv`: Dataset used for training the model
- `templates/`: HTML templates for the web interface
- `static/`: Static files (CSS, JavaScript, images)

## Model Information

The application uses a Support Vector Machine (SVM) classifier with a linear kernel. The text is vectorized using TF-IDF (Term Frequency-Inverse Document Frequency) to convert the text messages into numerical features that can be used by the machine learning algorithm.