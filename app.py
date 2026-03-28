import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open('models/svm_model.pkl', 'rb'))
tfidf = pickle.load(open('models/tfidf_vectorizer.pkl', 'rb'))
# Title
st.title("🛒 Fake Review Detection System")

st.write("Detect whether a product review is Genuine or Fake using Machine Learning.")

# Input box
review = st.text_area("Enter your review here:")

# Prediction function
def predict_review(review):
    review_tfidf = tfidf.transform([review])
    prediction = model.predict(review_tfidf)[0]

    if prediction == 1:
        return "❌ Fake Review"
    else:
        return "✅ Genuine Review"

# Button
if st.button("Check Review"):
    if review.strip() == "":
        st.warning("Please enter a review!")
    else:
        result = predict_review(review)
        st.success(f"Prediction: {result}")