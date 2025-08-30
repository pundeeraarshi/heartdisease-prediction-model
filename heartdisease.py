import streamlit as st
import pandas as pd
import numpy as np
import pickle
import random

st.header('Heart Disease Prediction Using Machine Learning')

data = '''Heart Disease Prediction using Machine Learning Heart disease prevention is critical, and data-driven prediction systems can significantly aid in early diagnosis and treatment. Machine Learning offers accurate prediction capabilities, enhancing healthcare outcomes. In this project, I analyzed a heart disease dataset with appropriate preprocessing. Multiple classification algorithms were implemented in Python using Scikit-learn and Keras to predict the presence of heart disease.

Algorithms Used:

**Logistic Regression**

**Naive Bayes**

**Support Vector Machine (Linear)**

**K-Nearest Neighbors**

**Decision Tree**

**Random Forest**

**XGBoost**

**Artificial Neural Network (1 Hidden Layer, Keras)**
'''

st.markdown(data)


st.image('https://cdn.mos.cms.futurecdn.net/dMhEcS6kLzdgWmnYjkCCVT-970-80.jpg.webp')

#st.subheader('Checking Error')
#with open('heart_disease_pred.pkl','rb') as f:
#   try:
#        st.write('File Loading')
#        chatgpt = pickle.load(f)
#    except Exception as e:
#        st.write('File not found',e)

 Load data
url = '''https://github.com/ankitmisk/Heart_Disease_Prediction_ML_Model/blob/main/heart.csv?raw=true'''
df = pd.read_csv(url)


st.sidebar.header('Select Features to Predict Heart Disease')
st.sidebar.image('https://humanbiomedia.org/animations/circulatory-system/cardiac-cycle/heart-beating.gif')

all_values = []

for i in df.iloc[:,:-1]:
    min_value, max_value = df[i].agg(['min','max'])

    var =st.sidebar.slider(f'Select {i} value', int(min_value), int(max_value),
                      random.randint(int(min_value),int(max_value)))

    all_values.append(var)

final_value = [all_values]

ans = chatgpt.predict(final_value)[0]

if ans == 0:
    st.success('No Heart Disease')
else:
    st.warning('Heart Disease Detected')

st.markdown('Designed by: **Aarshi Pundeer**')


