# 📈 Stock Movement Prediction using Machine Learning

An end-to-end **Data Science project** that predicts whether a stock’s price will go **up or down** using various technical indicators. The model is trained, optimized, and deployed through a **Flask web app** with a clean UI.

---

## 🚀 Features
- Predicts **stock price direction** (UP/DOWN)
- End-to-end pipeline: preprocessing → model → deployment
- Hyperparameter tuning with **GridSearchCV**
- Interactive Flask web app
- Gradient Boosting Classifier with ~89% accuracy

---

## 🧰 Tech Stack
- **Python**
- **Pandas, NumPy, Scikit-learn**
- **Matplotlib, Seaborn**
- **Flask**
- **Joblib**
- **HTML, CSS**

---

## 📊 Model Workflow

1. **Data Preprocessing**
   - Drop unnecessary columns
   - Scale features using StandardScaler & MinMaxScaler

2. **Model Training**
   - Compare multiple ML models
   - Best: Gradient Boosting Classifier (Accuracy: 0.89)

3. **Model Optimization**
   - Tuned hyperparameters using GridSearchCV
   - Validated using cross-validation

4. **Deployment**
   - Flask app for prediction
   - HTML form for inputs
   - Displays prediction with intuitive messages

---

## 💻 How to Run Locally
```bash
# Clone the repo
git clone https://github.com/yourusername/Stock-Movement-Predictor.git
cd Stock-Movement-Predictor

# Install dependencies
pip install -r requirements.txt

# Run Flask App
python app.py
Visit http://127.0.0.1:5000 in your browser.

🧠 Model Performance
Metric	Score
Accuracy	0.889
Mean CV Accuracy	0.877
F1-Score	0.89

🛠 Future Improvements
Real-time stock data API
Database integration for history tracking
Cloud deployment
Streamlit dashboard

📄 [View Full Project Report](PROJECT_REPORT.md)

👩‍💻 Author

Musfira Mubeen
🎓 Data Science Enthusiast | Python Developer | Machine Learning Learner
🔗 LinkedIn: https://www.linkedin.com/in/musfira-mubeen/
 • 💻 GitHub: https://github.com/mubeen20012
📧 musfira.mubeen@example.com

