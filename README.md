# 📰 Fake News Detector

A machine learning web app that classifies news articles as Real or Fake.

## 🔗 Live Demo
(https://huggingface.co/spaces/Armeen123/fake-news-detector)

## Model Details
- **Dataset:** ISOT Fake News Dataset (44,898 articles)
- **Features:** TF-IDF (10,000 features) on title + body text
- **Algorithm:** Logistic Regression
- **Accuracy:** 98.6%
- **F1-Score:** 0.99

## Limitations
- Trained on US political news (2016–2017)
- May not generalize to other domains or languages
- Detects linguistic patterns only — not a fact-checker

## Tech Stack
Python · Scikit-learn · Streamlit · Hugging Face Spaces
