import pickle
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import io
import base64
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

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
    top_6_fruits = results_df.mean().sort_values(ascending=False).head(6).index

    # Get the prices of the top 5 fruits
    prices = results_df.loc[0, top_6_fruits].values.round(2)

    # Convert the prices to a list
    prices = list(prices)

    # Get the names of the top 5 fruits
    fruits = list(top_6_fruits)

        # Filter the DataFrame to get the row for the specified center and month
    filtered_df = df[(df["Centername"] == Centername) & (df["Month"] == Month)]

    # Get the list of fruit prices for the specified center and month
    fruit_prices = list(filtered_df.iloc[0][2:].items())

    # Sort the fruit prices in descending order
    sorted_fruit_prices = sorted(fruit_prices, key=lambda x: x[1], reverse=True)

    # Print the sorted list with column names
    # Create a new DataFrame with the sorted fruit prices
    Actual_result_df = pd.DataFrame(sorted_fruit_prices, columns=["Fruit", "Price"])

        
    # Create a bar chart of the predicted prices
    fig = Figure(figsize=(8, 6), dpi=100)
    axis = fig.add_subplot(1, 1, 1)
    axis.bar(fruits, prices, color='blue')
    axis.set_title(f'Predicted Fruit Prices in {Centername} for {Month}')
    axis.set_xlabel('Fruit')
    axis.set_ylabel('Price (in Rs)')

    # Save the plot to a buffer
    buffer = io.BytesIO()
    canvas = FigureCanvas(fig)
    canvas.print_png(buffer)
    data = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()

    # Create a bar chart of the actual fruit prices
    fig = Figure(figsize=(8, 6), dpi=100)
    axis = fig.add_subplot(1, 1, 1)
    axis.bar(Actual_result_df["Fruit"].head(6), Actual_result_df["Price"].head(6), color='green')
    axis.set_title(f'Actual Fruit Prices in {Centername} for {Month}')
    axis.set_xlabel('Fruit')
    axis.set_ylabel('Price (in Rs)')
    axis.tick_params(axis='x', rotation=45)

    # Save the plot to a buffer
    buffer2 = io.BytesIO()
    canvas2 = FigureCanvas(fig)
    canvas2.print_png(buffer2)
    data2 = base64.b64encode(buffer2.getvalue()).decode('utf-8')
    plt.close()

    #
    fig = Figure(figsize=(8, 6), dpi=100)
    axis = fig.add_subplot(1, 1, 1)

    # Sort the actual prices dataframe by price in descending order
    Actual_result_df = Actual_result_df.sort_values('Price', ascending=False)

    # Add the bar plots for predicted and actual prices
    axis.bar(fruits, prices, color='green', label='Predicted')
    axis.bar(Actual_result_df["Fruit"].head(6), Actual_result_df["Price"].head(6), color='orange', label='Actual', alpha=0.7)

    # Add a line plot for predicted prices
    axis.plot(fruits, prices, marker='o', color='purple', linestyle='dashed')

    # Add a line plot for actual prices
    axis.plot(Actual_result_df["Fruit"].head(6), Actual_result_df["Price"].head(6), marker ='o', color='blue', linestyle='dashed')

    # Set the chart title, axis labels, and legend
    axis.set_title(f'Predicted vs Actual Fruit Prices in {Centername} for {Month}')
    axis.set_xlabel('Fruit')
    axis.set_ylabel('Price (in Rs)')
    axis.legend()

    # Set the x-axis labels to 45-degree angle for readability
    axis.tick_params(axis='x', rotation=45)

    # Set the y-axis limits to a difference of 1000
    y_min = min(min(prices), min(Actual_result_df["Price"].head(6)))
    y_max = max(max(prices), max(Actual_result_df["Price"].head(6)))
    axis.set_ylim([y_min - 500, y_max + 500])



    # Save the plot to a buffer
    buffer3 = io.BytesIO()
    canvas3 = FigureCanvas(fig)
    canvas3.print_png(buffer3)
    data3 = base64.b64encode(buffer3.getvalue()).decode('utf-8')
    plt.close()


    # Render the results page with the predicted prices and the plot
    return render_template('result.html', month=Month, city=Centername, fruits=fruits, prices=prices,Actual_result_df=Actual_result_df, plot_data=data, plot_data2=data2,plot_data3=data3)

if __name__ == "__main__":
    # Run the Flask app
    app.run(debug=True)
