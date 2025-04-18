from fastapi import FastAPI

# Allows you to validate request data
from pydantic import BaseModel

import pickle
import numpy as np

# Load saved ML model
with open("model/iris_model.pkl", "rb") as f:
    model = pickle.load(f)

# Creates an instance of the app
app = FastAPI()

# # 2. Define the request data structure using Pydantic
# class NumberInput(BaseModel):
#     number: int

# Define input schema
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width:  float
    petal_length: float
    petal_width:  float

# 3. Define a POST API endpoint to receive data
@app.post("/predict")

def predict_species(data: IrisInput):
    features = np.array([[data.sepal_length, data.sepal_width,
                          data.petal_length, data.petal_width]])

    prediction = model.predict(features)
    species = ['setosa', 'versicolor', 'virginica']
    
    return {
        "input": data.dict(),
        "predicted_species": species[prediction[0]]
    }

# # Function that handles requests
# def check_even_odd(data: NumberInput):
#     """
#     Accepts a number and returns whether it's even or odd.
#     """
#     if data.number % 2 == 0:
#         result = "Even"
#     else:
#         result = "Odd"
    
#     #Sends a JSON response back to the client
#     return{
#         "input":      data.number,
#         "prediction": result
#     }