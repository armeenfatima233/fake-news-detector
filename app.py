import streamlit as st
import pickle

# Load model and vectorizer
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# UI
st.set_page_config(page_title="Fake News Detector", page_icon="📰")

st.title("📰 Fake News Detector")
st.write("Paste a news headline or article below to check if it's real or fake.")

user_input = st.text_area("Enter news text here:", height=200)

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        input_tfidf = vectorizer.transform([user_input])
        prediction = model.predict(input_tfidf)[0]
        confidence = model.predict_proba(input_tfidf)[0][prediction] * 100

        if prediction == 1:
            st.success(f"✅ This looks REAL — {confidence:.1f}% confidence")
        else:
            st.error(f"🚨 This looks FAKE — {confidence:.1f}% confidence")

st.markdown("---")
st.caption("Model trained on ISOT Fake News Dataset | 44,898 articles | Accuracy: 98.6%")