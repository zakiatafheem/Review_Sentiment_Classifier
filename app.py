import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("🍽 Review Sentiment Classifier")

review_text = st.text_area("Enter your review:")

if st.button("Predict"):
    if review_text.strip() == "":
        st.warning("Please enter a review")
    else:
        prediction = model.predict([review_text])[0]

        if prediction == 1:
            st.success("✅ Positive Review")
        else:
            st.error("❌ Negative Review")