import pandas as pd
import numpy  as np
import tensorflow as tf
from  sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
df=pd.read_csv("C:\my workspace\project\AI-based-IT-training-system\Student Engagement Level-Multiclass.csv")
df.head()
x=df[df.columns[1:-1]]
y=df[df.columns[-1:]]
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Initialize and train the SVM classifier
clf = SVC(kernel='linear', C=1.0, random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Evaluate the model's accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
report = classification_report(y_test, y_pred)
print("Classification Report:\n", report)

# Use the trained model to predict the pace of a new learner
new_learner_features = [87,20,58,15,12,1,1,1,1,1,1,1]  # Replace with the feature vector of the new learner
predicted_pace = clf.predict([new_learner_features])[0]
print(f"The new learner's predicted pace is: {predicted_pace}")
