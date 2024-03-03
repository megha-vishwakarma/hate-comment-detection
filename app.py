from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('toxicity_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
@app.route('/analyze', methods=['POST'])
def analyze():
    comment = request.form['comment']

    # Use the trained model to predict toxicity
    probabilities = model.predict_proba([comment])[0]
    toxicity_score = probabilities[1]

    print(f"Comment: {comment}")
    print(f"Toxicity Probabilities: {probabilities}")
    print(f"Toxicity Score: {toxicity_score}")

    return render_template('result.html', comment=comment, toxicity_score=toxicity_score)

if __name__ == '__main__':
    app.run(debug=True)
