# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle

# Load the model
loaded_model = pickle.load(open('D:/New folder/Evcar_acceptance.sav', 'rb'))

# Input data
input_data = (1, 3, 4, 0, 2, 2, 1, 3, 3, 1, 3, 2, 1, 1)

# Convert input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Predict using the loaded model
prediction = loaded_model.predict(input_data_reshaped)

# Print the prediction result
if prediction[0] == 0:
    print('evcar')
else:
    print('gasoline car')
