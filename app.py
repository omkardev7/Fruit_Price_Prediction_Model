import pickle
from flask import Flask, render_template, request
import pandas as pd
import numpy as np

# Load the trained model
pipeline = pickle.load(open("models/model1.pkl", "rb"))

# Load the dataset
df = pd.read_csv('./dataset/Fruit_Dataset_2.csv')

# Create a Flask app
app = Flask(__name__)

# Define the home page route
@app.route("/")
def home():
    return render_template("home.html")

# Define the prediction route
@app.route("/predict", methods=["POST"])
def predict():
    # Get the input values from the form
    Month = request.form["Month"]
    Centername = request.form["Centername"]

    # Make a prediction using the trained model
    prediction = pipeline.predict([[Month, Centername]])

    # Get the column names of the fruit prices
    fruit_columns = df.columns[2:]

    results = {}
    for i, fruit in enumerate(fruit_columns):
        results[fruit] = prediction[:, i]

    # Convert the dictionary to a pandas DataFrame
    results_df = pd.DataFrame(results)

    # Get the top 5 fruits sorted by predicted prices in descending order
    top_5_fruits = results_df.mean().sort_values(ascending=False).head(10).index

    # Get the prices of the top 5 fruits
    prices = results_df.loc[0, top_5_fruits].values.round(2)

    # Convert the prices to a list
    prices = list(prices)

    # Get the names of the top 5 fruits
    fruits = list(top_5_fruits)
    # Render the results page with the predicted prices
    return render_template('result.html', month=Month, city=Centername, fruits=fruits, prices=prices)

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
