# Consumer Behavior & Shopping Habits

## 📌 Overview

The **Consumer Behavior and Shopping Habits** project explores consumer preferences, purchasing patterns, and shopping behavior using machine learning and data analysis.

The project uses the **Consumer Behavior and Shopping Habits Dataset** to analyze factors that influence purchasing decisions and to build machine learning models for predicting consumer-related outcomes.

The goal is to transform raw consumer data into meaningful insights that can help businesses understand their customers, improve marketing strategies, optimize product offerings, and enhance customer satisfaction.

## 📊 Dataset

The dataset is sourced from Kaggle:

**Dataset:** [Consumer Behavior and Shopping Habits Dataset](https://www.kaggle.com/datasets/zeesolver/consumer-behavior-and-shopping-habits-dataset)

The dataset contains information related to:

* 👤 Customer demographics
* 🛍️ Products purchased
* 💰 Purchase amounts
* ⭐ Review ratings
* 📍 Customer locations
* 📦 Shipping preferences
* 💳 Payment methods
* 🎁 Discounts and promotional codes
* 🔄 Previous purchases
* 📅 Purchase frequency
* 👕 Product categories and sizes
* 🌦️ Shopping season
* 🔔 Subscription status

## 🎯 Problem Statement

Understanding consumer buying behavior is important for businesses that want to make data-driven decisions.

In this project, we use **data analysis, classification, and regression techniques** to identify patterns in consumer behavior and build predictive models.

The project focuses on questions such as:

* What factors influence purchase amounts?
* Can customer purchasing behavior be predicted?
* Which customer characteristics are associated with different purchasing patterns?
* How do discounts, subscriptions, shipping methods, and payment methods relate to purchasing behavior?
* Can machine learning models be used to predict future consumer-related outcomes?

## 🤖 Machine Learning Approach

The project explores both **regression and classification** techniques.

### Regression

Regression models are used to predict continuous values such as **purchase amount**.

The project includes a **Purchase Amount Prediction** application where users can enter customer and purchase-related information and receive a predicted purchase amount.

### Classification

Classification models can be used to categorize consumers or predict categorical outcomes based on their characteristics and purchasing behavior.

## 🛠️ Technologies Used

* **Python**
* **Pandas** – Data manipulation and analysis
* **NumPy** – Numerical computation
* **Matplotlib** – Data visualization
* **Seaborn** – Exploratory data analysis
* **Scikit-learn** – Machine learning
* **Joblib** – Model serialization
* **Streamlit** – Machine learning web application

## 🌐 Purchase Prediction App

A **Streamlit web application** has been developed to demonstrate the regression model.

Users can provide information such as:

* Age
* Gender
* Item Purchased
* Category
* Location
* Size
* Color
* Season
* Review Rating
* Subscription Status
* Shipping Type
* Discount Applied
* Promo Code Used
* Previous Purchases
* Payment Method
* Frequency of Purchases

The application then uses the trained machine learning model to predict the expected **purchase amount in USD and INR**.

## 📁 Project Structure

```text
Consumer-Behavior-Shopping-Habits/
│
├── app.py
├── linear_regression_model.pkl
├── requirements.txt
├── README.md
└── ...
```

## 🚀 Running the Streamlit Application Locally

### 1. Clone the repository

```bash
git clone https://github.com/akashuniyal01/Consumer-Behavior-Shopping-Habits.git
```

### 2. Navigate to the project directory

```bash
cd Consumer-Behavior-Shopping-Habits
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will then be available at the local Streamlit URL displayed in your terminal.

## ☁️ Deployment

The Streamlit application can be deployed using platforms such as **Render**.

A typical Render configuration is:

**Build Command**

```bash
pip install -r requirements.txt
```

**Start Command**

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

## 👥 Collaborators

* Mahmoud Alhousseiny
* Gray Lumsden
* Jon York

## 📚 Dataset Source

This project uses the **Consumer Behavior and Shopping Habits Dataset** available on Kaggle.

Dataset: https://www.kaggle.com/datasets/zeesolver/consumer-behavior-and-shopping-habits-dataset

## 🔮 Future Improvements

Possible future improvements include:

* Improving model performance through feature engineering
* Comparing multiple regression and classification algorithms
* Using proper categorical encoding techniques
* Hyperparameter tuning
* Adding interactive data visualizations to the Streamlit application
* Implementing real-time currency conversion
* Adding additional prediction models
* Deploying the complete application online
* Improving the user interface and user experience

## 📌 Disclaimer

This project is intended for **educational and analytical purposes**. Predictions generated by the machine learning models are based on the available dataset and should not be considered guaranteed real-world outcomes.
