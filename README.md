# Fruit_Price_Prediction_Model
This project presents a machine learning approach to predict fruit prices for various cities. Two regression models, Random Forest Regressor and Decision Tree Regressor, were evaluated, and the results showed that the Random Forest Regressor performed better. The developed Flask web application takes user input in the form of a month and a center name and uses the machine learning model to predict the prices of fruits for that center in that month. The application displays the top six predicted fruit prices in a bar chart and compares them with the actual fruit prices for the specified center and month in another bar chart. Finally, a third bar chart is created that displays both the predicted and actual prices for the top six fruits in descending order. This project demonstrates the potential of machine learning in predicting fruit prices, which could have significant implications for the agriculture and food industries.

## Installation

1. Clone the repository from GitHub:

```bash
  git clone https://github.com/Omkar-Rajkumar-Khade/Fruit_Price_Prediction_Model.git
```


2. Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```


## How to Use
To get started with this project, follow these steps:
* Clone this repository
* Install the required dependencies using pip: pip install -r requirements.txt
* Start the Flask server: python app.py
* Send a POST request to the /predict endpoint with a JSON payload containing the values of various of city and month

### Folder Structure 

`dataset` folder contains the engineering.csv dataset used in the project.

`Fruit_price_prediction_with_pipeline.ipynb` notebook that was used to develop and train the model.

`app.py` is the Flask application file that defines the API endpoints and loads the saved model.

`models` is folder that contain the serialized machine learning models that is used for prediction.

`README.md` is the project documentation file.

`requirements.txt` lists the Python dependencies required to run the project.

`templates` folder contains the HTML templates for the web application.

`static` folder contains the images.


### Prerequisites

To run the project, you must have the following installed on your system:

* Python 3.6+
* Flask
* Pandas
* Scikit-learn

## Machine Learning Model Training

To predict the price of a bike, we trained three different regression models:

* Random Forest Regressor (RFR)
* Decision Tree Regressor (DTR)

The transformers used in the pipeline are:

* `ColumnTransformer`: Used to apply different transformers to different columns of the data.
* `StandardScaler`: Used to standardize the numerical data.
* `OneHotEncoder`: Used to encode categorical data.

We created four pipelines, one for each regression model, using the two column transformers created earlier and the corresponding regression model.

We trained each pipeline on the training data, made predictions using the test data, and evaluated each model's performance using R-squared score and Root mean square error (RMSE).

## Results
After training and testing the four regression models, we found the following results:

| Model           | R-square | RMSE |
| ----------------- |----------------| ------------------------------------------------------------------ |
| Random Forest Regressor (RFR) | 0.22| 1119.69 |
| Decision Tree Regressor (DTR) |0.06 | 1380.21|

Based on the R-square and RMSE values you provided, it appears that the Random Forest Regressor (RFR) outperformed the Decision Tree Regressor (DTR) in predicting the target variable. The RFR has an R-square of 0.22, which indicates that the model explains 22% of the variance in the target variable. The RMSE of 1119.69 suggests that the average distance between the predicted and actual values of the target variable is relatively low.

In contrast, the DTR has an R-square of 0.06, which indicates that the model explains only 6% of the variance in the target variable. The RMSE of 1380.21 suggests that the average distance between the predicted and actual values of the target variable is relatively high.

Based on the results provided, the Random Forest Regressor (RFR) seems to be the best-performing algorithm for this particular problem. As we can see, the RFR model outperforms the DTR model in both metrics. However, the R-squared values for both models are relatively low, indicating that the models aren't doing a great job of explaining the variance in the target variable.

## Model Integration
This project features a Flask application that permits users to interact with a machine learning model by entering customized input parameters such as months and city, and receiving fruit price predictions in response. Flask is a Python-based web framework that enables the development of web applications. The trained machine learning model is loaded using the pickle library from a saved file, allowing it to be integrated into the Flask application.

The Flask app has two HTML templates: home.html and result.html, which provide the user interface for entering input parameters and displaying the predicted price. The home.html template includes a form where the user can input the necessary parameters to make a price prediction. When the user submits the form, the Flask app obtains the input parameters, and the machine learning model utilizes them to make a price prediction. The predicted price is then shown on the result.html template, which is responsible for presenting the predicted price in a user-friendly manner.

This Flask web application that takes input from the user in the form of a month and a center name. It then uses a machine learning model to predict the prices of fruits for that center in that month and displays the top six predicted fruit prices in a bar chart.

The script then filters the dataset to get the actual fruit prices for the specified center and month and displays the top six actual fruit prices in a second bar chart. Finally, the script creates a third bar chart that displays both the predicted and actual prices for the top six fruits in descending order.

The bar charts are created using the Matplotlib library and are saved as PNG images. The PNG images are then converted to base64 format and embedded in the HTML template that is rendered by Flask.

To run the Flask app, the app.run(debug=True) command is utilized, which launches the development server and enables debug mode. Debug mode is advantageous during development since it allows developers to view detailed error messages and other pertinent information that can be used to diagnose and fix issues with the app.

To utilize the app, simply navigate to the home page (http://localhost:5000/) and input the desired parameters. Once the form is submitted, the predicted price is displayed on the results page. The app can be deployed on a local machine or a server for public use.

## Conclusion
In conclusion, this project presents a valuable application of machine learning in predicting fruit prices for different cities. The results of the evaluation of the two regression models show that the Random Forest Regressor model performs better in predicting fruit prices compared to the Decision Tree Regressor model. Although both models had relatively low R-squared values, this project serves as a starting point for future exploration of other regression models or optimization of hyperparameters to improve the accuracy of fruit price predictions.

The Flask web application provides an interactive and user-friendly platform for users to predict and compare fruit prices for different centers and months. The use of bar charts to display the predicted and actual fruit prices provides an easy-to-understand visualization for users to compare and analyze the data. This tool could be useful for stakeholders in the agriculture and food industries to make informed decisions regarding pricing, distribution, and supply chain management.

Overall, this project demonstrates the potential of machine learning in predicting fruit prices and provides a foundation for future research in this field. Further improvements could be made by incorporating more data sources, optimizing the models, and expanding the application to other regions and commodities.
