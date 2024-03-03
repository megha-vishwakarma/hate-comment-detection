# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.pipeline import make_pipeline
# from sklearn.metrics import accuracy_score
# import joblib

# # Load your dataset (replace 'your_dataset.csv' with your actual dataset)
# df = pd.read_csv('comments.csv')

# # Assuming your dataset has 'comment' column for text and 'toxicity' column for labels
# X = df['Comment']
# y = df['class']

# # Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Build a pipeline with CountVectorizer and MultinomialNB
# model = make_pipeline(CountVectorizer(), MultinomialNB())

# # Train the model
# model.fit(X_train, y_train)

# # Evaluate the model
# y_pred = model.predict(X_test)
# accuracy = accuracy_score(y_test, y_pred)
# print(f'Model Accuracy: {accuracy}')

# # Save the trained model to a file
# joblib.dump(model, 'toxicity_model.joblib')

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
import joblib


#Load your dataset (replace 'your_dataset.csv' with your actual dataset)
df = pd.read_csv('comments.csv')

#Assuming your dataset has 'comment' column for text and 'toxicity' column for labels
X = df['Comment']
y = df['class']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build a pipeline with TF-IDF vectorizer and Naive Bayes classifier
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy}')

# Save the trained model to a file
joblib.dump(model, 'toxicity_model.joblib')