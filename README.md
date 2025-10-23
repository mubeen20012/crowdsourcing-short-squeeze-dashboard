📈 Stock Movement Prediction Web App

🧠 Overview
The Stock Movement Prediction App is a machine learning–powered web application built with Flask that predicts whether a stock’s price will go UP 📈 or DOWN 📉 based on key daily market indicators.
It provides a modern, interactive interface where users can input real-world stock data and instantly get predictions powered by a Gradient Boosting Classifier trained on historical price patterns.

🚀 Features
✅ Predicts stock movement direction (Up or Down)
✅ Built with Flask and Gradient Boosting Classifier
✅ Clean, modern, and responsive web interface
✅ Real-time form validation and prediction
✅ Organized modular project structure
✅ Error-handling for smooth user experience

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

🧩 Tech Stack
| Component            | Technology                                  |
| -------------------- | ------------------------------------------- |
| **Frontend**         | HTML5, CSS3 (Custom UI Design)              |
| **Backend**          | Python (Flask)                              |
| **Machine Learning** | Gradient Boosting Classifier (scikit-learn) |
| **Libraries Used**   | pandas, NumPy, joblib                       |
| **IDE**              | Visual Studio Code                          |

  



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

📊 Model Details
Algorithm Used: Gradient Boosting Classifier
Training Dataset: stock_features.csv
Target Variable: target_updown
Performance Metric: Accuracy

Input Features:
Open Price
High Price
Low Price
Close Price
Adjusted Close Price
Average Price
Moving Averages (MA10, MA50)
VWAP (Volume Weighted Average Price)
Daily Return Percentage
Price Range
Volume

Output:
1 → Stock will go UP 📈
0 → Stock will go DOWN 📉

🖼️ User Interface Preview
The app features a sleek, gradient-based dark theme with labeled input fields, intuitive buttons, and a result display card.
Users can enter the stock details and instantly get prediction results with clear visuals.

<img width="1366" height="885" alt="stock" src="https://github.com/user-attachments/assets/a18f1f3e-262a-400f-b97b-5dafcad3ca87" />

Deployment on Render
Create a free account on Render.com
, then:
Connect your GitHub repo
Add these settings:
Build Command: pip install -r requirements.txt
Start Command: python stock_prediction_app/app.py
Auto-deploy your model app 🚀

👩‍💻 Author
Musfira Mubeen
🎓 Data Science Enthusiast | Python Developer | Machine Learning Learner
🔗 LinkedIn: https://www.linkedin.com/in/musfira-mubeen/
 • 💻 GitHub: https://github.com/mubeen20012
📧 musfira.mubeen@example.com

