import streamlit as st
import pickle

# Load the trained pipeline
with open("spam_pipeline.pkl", "rb") as file:
    pipeline = pickle.load(file)

# Streamlit UI
st.title("Spam Detection App")
user_input = st.text_area("Enter a message:")

if st.button("Predict"):
    prediction = pipeline.predict([user_input])  # Directly use the pipeline
    result = "Spam" if prediction[0] == 1 else "Not Spam"
    st.write(f"Prediction: **{result}**")

# Sample sentence for testing
# "Your account have 100 debeted, is waiting to be collected. Simply text the password \MIX\" to 85069 to verify. Get Usher and Britney. FML"