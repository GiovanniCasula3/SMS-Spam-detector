import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import *
from sklearn.svm import *
import pandas

app = Flask(__name__)
global Classifier
global Vectorizer

# loading the data
data = pandas.read_csv('Data/spam.csv', encoding='latin-1')
train_data = data[:4400]
test_data = data[4400:]

# training the model
Classifier = OneVsOneClassifier(SVC(kernel='linear', probability=True))
Vectorizer = TfidfVectorizer()
vectorize_text = Vectorizer.fit_transform(train_data.v2)
Classifier.fit(vectorize_text, train_data.v1)

@app.route('/', methods=['GET'])
def index():
    message = request.args.get('message', '')
    error = ''
    predict_proba = ''
    predict = ''
    
    global Classifier
    global Vectorizer
    try:
        if len(message) > 0:
            vectorize_message = Vectorizer.transform([message])
            label = Classifier.predict(vectorize_message)[0]
            predict = "Messaggio normale" if label == "ham" else "Spam"
    except BaseException as ints:
        error = str(type(ints).__name__) + ' ' + str(ints)
    return render_template(
        'index.html', message=message, predict=predict, error=error
    )
    
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True, use_reloader= True)