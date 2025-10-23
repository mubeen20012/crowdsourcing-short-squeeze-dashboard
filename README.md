# 📈 Crowdsourcing Short Squeeze Dashboard

A **data-driven machine learning dashboard** built using **Flask** that predicts short-squeeze opportunities in stock markets.  
This project applies **Gradient Boosting Classification** on real stock data (e.g., GME) to forecast market trends and provide visual insights through an interactive web interface.

---

## 🧠 Project Overview

The **Crowdsourcing Short Squeeze Dashboard** aims to assist investors and analysts by predicting whether a stock is likely to experience a short squeeze based on engineered market features.

The app:
- 🧩 Uses machine learning (Gradient Boosting Classifier) to classify short-squeeze potential  
- 📊 Displays predictions and trends through an interactive Flask dashboard  
- 📈 Helps identify opportunities by combining historical and engineered stock features  

---

## 🗂️ Folder Structure
crowdsourcing-short-squeeze-dashboard/
│
├── data/
│ ├── GME_stock.csv # Historical stock data
│ └── stock_feature.csv # Engineered features for model training
│
├── model/
│ └── final_stock_model.pkl # Trained Gradient Boosting Classifier model
│
├── notebook/
│ ├── stock_feature_engineering.ipynb # Feature creation and analysis
│ ├── stock_price_prediction.ipynb # Model training and evaluation
│ └── stock_price_prediction.py # Script version for model training
│
├── stock_prediction_app/
│ ├── templates/
│ │ └── index.html # Frontend for Flask web app
│ └── app.py # Flask backend logic for model prediction
│
├── requirement.txt # Dependencies
├── runtime.txt # Python version for Render
├── procfile # Render start command
└── README.md

---

## ⚙️ Tech Stack

**Languages & Frameworks:**  
🐍 Python | 🌐 Flask  

**Libraries:**  
📦 Pandas | NumPy | Plotly | Joblib | Scikit-learn  

**Machine Learning Model:**  
🚀 Gradient Boosting Classifier  

**Deployment:**  
☁️ Render (Cloud hosting for Flask apps)

---

## 📊 Model Performance

- **Model Used:** Gradient Boosting Classifier  
- **Accuracy:** 0.89 (89%)  
- **Evaluation Metric:** Confusion Matrix  
- **Result:** Balanced performance across both classes (0 and 1)

### Confusion Matrix Visualization  
![Confusion Matrix Heatmap](https://github.com/yourusername/crowdsourcing-short-squeeze-dashboard/blob/main/notebook/confusion_matrix.png)

| Metric | Value |
|---------|--------|
| Accuracy | 0.89 |
| Precision | High |
| Recall | Balanced |
| F1-score | Strong overall performance |

The model effectively predicts **potential short-squeeze events**, minimizing both false positives and negatives.

---

## 💻 How to Run Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/crowdsourcing-short-squeeze-dashboard.git
cd crowdsourcing-short-squeeze-dashboard

Install dependencies
pip install -r requirement.txt

Run the Flask app
cd stock_prediction_app

python app.py
Open your browser

Go to 👉 http://127.0.0.1:5000/

👩‍💻 Author
Musfira Mubeen
🎓 Data Science Enthusiast | Python Developer | Machine Learning Learner
🔗 LinkedIn: https://www.linkedin.com/in/musfira-mubeen/
 • 💻 GitHub: https://github.com/mubeen20012
📧 musfira.mubeen@example.com

