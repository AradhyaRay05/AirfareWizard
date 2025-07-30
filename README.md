# ✈️ AirfareWizard  
**AI-powered flight fare predictor**

---

## 🧠 Project Goal

**AirfareWizard** is a machine learning-based flight fare prediction system that estimates the cost of a flight ticket based on journey details provided by users. The goal is to offer intelligent pricing insights using historical data and a trained ML model through an interactive web interface.

---

## 📌 Project Overview

This project uses historical flight data to predict airfare prices. It applies feature engineering, data cleaning, and an ML regression model (CatBoost) to build an accurate predictor. Users can interact with the model via a Streamlit web app, which allows them to input travel details and receive fare estimates instantly.

---

## 🔁 Project Workflow

### 1. **Data Preprocessing**
- Converted `Date_of_Journey`, `Dep_Time`, and `Arrival_Time` into separate day, month, hour, and minute features
- Calculated flight **Duration** in hours and minutes
- Performed **One-Hot Encoding** on categorical columns: `Airline`, `Source`, `Destination`, `Additional_Info`
- Mapped `Total_Stops` to numerical values
- Removed redundant and irrelevant features like `Route` and `Additional_Info` where necessary

### 2. **Model Building**
- Tried multiple models: **Linear Regression**, **Decision Tree Regressor**, **Random Forest Regressor**, and **CatBoost Regressor**
- Chose **CatBoost Regressor** for final deployment due to:
  - Better handling of categorical data
  - Higher accuracy
  - Faster training without extensive preprocessing

### 3. **Evaluation Metrics**
- **R² Score (CatBoost):** `0.9048` (90.48% accuracy) on test data
- **Mean Absolute Error (MAE):** Used to measure prediction error
- CatBoost outperformed other models on validation and test sets

### 4. **Deployment**
- Frontend created using **Streamlit**, offering an intuitive interface
- Trained model saved as `model.pkl` using Python's `pickle`
- App handles missing model errors gracefully
- Designed to be deployed on:
  - **Streamlit Cloud** *(for free & quick deployment)*
  - **Render**, **Railway**, or **Heroku** *(for advanced options)*

---

## ⚙️ Tech Stack

### 📌 Programming Language
- Python 3.10+

### 📚 Libraries Used
- **Pandas** – data manipulation  
- **NumPy** – numerical operations  
- **Matplotlib** – data visualization  
- **Seaborn** – statistical plots  
- **Scikit-learn** – ML preprocessing & metrics  
- **CatBoost** – regression model  
- **Streamlit** – web deployment  
- **Pickle** – model serialization  

---

## 📁 Project Structure

```
AirfareWizard/
├── app.py                             # Streamlit app frontend
├── model.pkl                          # Trained CatBoost model
├── Flight Fare Prediction.ipynb       # EDA, preprocessing, and model training
├── requirements.txt                   # All dependencies
└── README.md                          # Project documentation
```

---

## ✨ Features

- Predicts flight fare based on:
  - **Airline**  
  - **Date of Journey**  
  - **Source and Destination**  
  - **Departure and Arrival Time**  
  - **Total Stops**  
  - **Duration (hours and minutes)**  
  - **Additional Info** (e.g., red-eye flight, business class)
- Clean and responsive UI using Streamlit
- Error handling for missing model or inputs
- Predict button to dynamically show result

---

## 🌱 Future Enhancements

- Deploy as a public web service (e.g., Streamlit Cloud)
- Include **round-trip fare prediction**
- Add **visual insights** like fare trends over months
- Use **live API data** to recommend the best time to fly
- Implement **user login** to track predictions

---

## 🚀 Getting Started

```bash
git clone https://github.com/your-username/AirfareWizard.git
cd AirfareWizard
pip install -r requirements.txt
streamlit run app.py
```
---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

<p>
  <a href="mailto:aradhyaray99@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/rayaradhya"><img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://github.com/AradhyaRay05"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

---

Thanks for visiting ! Feel free to explore my other repositories and connect with me. 🚀 
