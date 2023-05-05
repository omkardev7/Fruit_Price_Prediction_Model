# Fruit_Price_Prediction_Model
This project involves the development of a machine learning model to predict the fruit prices for various cities. The aim is to create a model that can accurately predict the prices of various fruits for a given city and month.The dataset contains prices of different fruits for different cities, along with other parameter such as month in India.

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
