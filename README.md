# HOUSE-PRICE-PREDICTION
**House Price Prediction System**
*Developed by Praveen Singh*

The House Price Prediction System is a machine learning-based web application designed to estimate the market value of residential properties based on various influencing factors. This project was developed as part of the AIML Summer Internship 2026 at IIHMF, MNNIT Allahabad, Prayagraj.

The primary objective of this project is to assist buyers, sellers, and real estate agents in making informed decisions by providing accurate price predictions using historical housing data. The system leverages the Boston House Prices dataset, which contains 506 records with 13 key features including crime rate, number of rooms, age of property, distance to employment centers, tax rate, and population status.

The project follows the complete Machine Learning lifecycle. In the data preprocessing phase, missing values were handled, duplicates were removed, and features were normalized using Standard Scaler to ensure optimal model performance. Exploratory Data Analysis was performed using histograms, scatter plots, boxplots, and correlation heatmaps to uncover meaningful patterns and relationships within the data.

Three regression models were trained and evaluated — Linear Regression, Random Forest Regressor, and XGBoost Regressor. Model performance was measured using standard regression metrics including Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R² Score. XGBoost demonstrated the best overall performance with the highest R² score and lowest error rates among all three models.

The final model was deployed as an interactive web application using Streamlit, allowing users to input property details and instantly receive a predicted house price. The application provides a simple, user-friendly interface accessible without any technical knowledge.

This project successfully demonstrates the practical application of machine learning in the real estate domain and highlights how data-driven approaches can significantly improve property valuation accuracy.
