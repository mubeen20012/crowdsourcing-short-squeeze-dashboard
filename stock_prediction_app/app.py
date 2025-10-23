from flask import Flask, request, render_template
import joblib
import numpy as np
import pandas as pd
import os

# Initialize Flask app
app = Flask(__name__)

# ✅ Load your trained model
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'final_stock_model.pkl')
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # ✅ Get all input values from the form
        features = [float(x) for x in request.form.values()]
        final_features = np.array(features).reshape(1, -1)

        # ✅ Create a DataFrame with the same columns used during training
        columns = [
            'open_price', 'high_price', 'low_price', 'close_price', 'adjclose_price',
            'avg_price', 'MA10', 'MA50', 'VWAP', 'daily_return_pct', 'price_range', 'volume'
        ]

        input_df = pd.DataFrame(final_features, columns=columns)

        # ✅ Predict using DataFrame
        prediction = model.predict(input_df)[0]

        # ✅ Output readable message
        result = "📈 Stock will go UP" if prediction == 1 else "📉 Stock will go DOWN"

        return render_template('index.html', prediction=result)

    except Exception as e:
        return render_template('index.html', prediction=f"⚠️ Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
