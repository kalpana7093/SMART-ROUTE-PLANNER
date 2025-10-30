# SMART-ROUTE-PLANNER
# 🚚 Smart Route Planner — Data-Driven Logistics Optimization

The **Smart Route Planner** is an AI-powered logistics optimization solution that predicts delivery delays and recommends the most cost-efficient delivery routes.  
It integrates **machine learning**, **route optimization**, and **interactive analytics** into a single Streamlit dashboard for intelligent logistics management.

---

## 🧠 Executive Summary

Modern logistics operations face constant challenges — fluctuating fuel costs, unpredictable traffic, weather delays, and sustainability concerns.  
The Smart Route Planner addresses these problems by combining **predictive analytics** and **optimization algorithms** to assist logistics planners in making data-driven delivery decisions.

---

## 🎯 Objectives

- Predict delivery delays using real-world variables such as traffic, weather, and toll costs.
- Optimize delivery routes for minimum cost, distance, and environmental impact.
- Provide an interactive and intuitive dashboard for real-time logistics analysis.
- Enable data-driven decision-making for transport and operations teams.

---

## 🧭 Project Roadmap

| Phase | Description |
|-------|--------------|
| **1️⃣ Data Understanding & Preparation** | Collected and cleaned datasets (`orders.csv`, `routes_distance.csv`, etc.), standardized schema, and ensured relational integrity. |
| **2️⃣ Exploratory Data Analysis (EDA)** | Visualized and analyzed delivery delay patterns, cost breakdowns, and route performance using Matplotlib and Seaborn. |
| **3️⃣ Machine Learning Model** | Trained classification models (Logistic Regression, Random Forest) to predict delivery delays. Tuned and saved final model using `joblib`. |
| **4️⃣ Route Optimization Engine** | Implemented **Google OR-Tools** to calculate optimal delivery routes minimizing distance, tolls, and traffic delays. |
| **5️⃣ Streamlit Dashboard** | Built an interactive app to visualize data, run delay predictions, and perform real-time route optimization. |
| **6️⃣ Deployment** | Deployed the full app on **Streamlit Cloud**, making it accessible from any browser. |

---

## 🧩 Features

- 🔮 **Predictive Modeling:** Estimates the probability of delayed deliveries.
- 🗺️ **Route Optimization:** Finds shortest and most cost-effective routes using OR-Tools.
- 📊 **Visual Analytics:** Interactive Streamlit dashboard for delay, route, and cost insights.
- ⚙️ **Automation:** Reduces manual decision-making with AI-driven route suggestions.
- 🌿 **Sustainability:** Minimizes CO₂ emissions by optimizing travel paths.

---

## 🧮 Technology Stack

| Category | Tool / Library |
|-----------|----------------|
| Language | Python 3.12 |
| Framework | Streamlit |
| ML Library | scikit-learn |
| Optimization | Google OR-Tools |
| Visualization | Matplotlib, Seaborn |
| Data Handling | Pandas, NumPy, Joblib |
| Deployment | Streamlit Cloud / Localhost |

---

## 🧰 Folder Structure
