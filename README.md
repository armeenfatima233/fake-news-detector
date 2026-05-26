# 📰 Fake News Detector

A machine learning web app that classifies news articles as REAL or FAKE with 98.6% accuracy.

## Live Demo
🔗 [https://huggingface.co/spaces/Armeen123/fake-news-detector](https://huggingface.co/spaces/Armeen123/fake-news-detector)

## How It Works
1. User pastes a news headline or article
2. Text is converted to TF-IDF features
3. Logistic Regression model predicts Real/Fake
4. Confidence score is displayed

## Model Details
- **Dataset:** ISOT Fake News Dataset (44,898 articles)
- **Algorithm:** Logistic Regression
- **Features:** TF-IDF (10,000 features)
- **Accuracy:** 98.6%
- **F1-Score:** 0.99

## Limitations
- Trained on US political news (2016-2017)
- May not generalize to non-English content
- Detects linguistic patterns, not facts

## Tech Stack
- Python + Scikit-learn
- Streamlit
- Hugging Face Spaces
- Pandas

## Run Locally
```bash
git clone https://github.com/Armeen294/fake-news-detector.git
cd fake-news-detector
pip install -r requirements.txt
streamlit run app.py
