# 📩 SpamGuard - SMS Spam Detection

SpamGuard is a Machine Learning-based SMS spam detection application that classifies messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP).

The project uses **TF-IDF feature extraction** and a **Support Vector Machine (SVM)** classifier to detect spam messages. A Streamlit web application is included to allow users to enter and analyze messages interactively.

---

## 🚀 Project Overview

Spam messages are unwanted messages that may contain advertisements, fraudulent offers, fake prizes, suspicious links, or other unwanted content.

This project builds an end-to-end Machine Learning pipeline that:

- Cleans and preprocesses SMS messages
- Converts text into numerical features using TF-IDF
- Trains multiple Machine Learning models
- Compares model performance using multiple evaluation metrics
- Performs hyperparameter tuning using GridSearchCV
- Selects the best-performing model
- Saves the trained model using Joblib
- Provides a Streamlit web application for real-time prediction

---

## 🎯 Objectives

- Detect whether an SMS message is spam or legitimate.
- Apply NLP techniques to text data.
- Compare different Machine Learning algorithms.
- Optimize the best-performing model using hyperparameter tuning.
- Build a complete ML pipeline from preprocessing to deployment.
- Create a simple web interface for real-time predictions.

---

## 📊 Dataset

The project uses the **SMS Spam Collection Dataset**.

The dataset contains SMS messages labeled as:

- `ham` → Legitimate message
- `spam` → Spam message

### Dataset Features

| Feature | Description |
|---|---|
| Label | Spam or Ham |
| Message | Text content of the SMS |

The dataset contains approximately **5,500+ SMS messages**.

---

## 🧹 Data Preprocessing

The SMS messages were cleaned before model training.

The preprocessing includes:

- Removing unnecessary punctuation
- Cleaning text data
- Separating features and target labels
- Encoding labels:
  - `ham = 0`
  - `spam = 1`
- Splitting the dataset into training and testing sets

The dataset was divided into:

- **80% Training Data**
- **20% Testing Data**

Stratified splitting was used to maintain the class distribution.

---

## 🔤 Feature Engineering - TF-IDF

Since Machine Learning models cannot directly understand raw text, the messages were converted into numerical vectors using **TF-IDF (Term Frequency-Inverse Document Frequency)**.

The final TF-IDF configuration was:

```text
max_df = 0.95
min_df = 2
ngram_range = (1, 2)
sublinear_tf = True