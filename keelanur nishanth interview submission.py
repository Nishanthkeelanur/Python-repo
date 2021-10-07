import pandas as pd
import numpy as np
import json

jsonstring = '[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166, "WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",  "HeightCm": 167, "WeightKg": 82}]'

jsondata=json.loads(jsonstring)

#print(jsondata)

df=pd.DataFrame(jsondata)

df['BMI']= df['WeightKg']/((df['HeightCm'])/100)**2


df['BMI']=np.round(df['BMI'],decimals=2)

df.loc[(df['BMI'] <= 18.5), 'BMI Category'] = 'Underweight'

df.loc[(df['BMI'] >=18.5) & (df['BMI'] <= 24.9), 'BMI Category'] = 'Normal Weight'  

df.loc[(df['BMI'] >= 25) & (df['BMI'] <= 29.9), 'BMI Category'] = 'Overweight'  

df.loc[(df['BMI'] >= 30) & (df['BMI'] <= 34.9), 'BMI Category'] = 'Moderately obese'  

df.loc[(df['BMI'] >= 35) & (df['BMI'] <= 39.9), 'BMI Category'] = 'Severely obese'  

df.loc[(df['BMI'] >= 40) , 'BMI Category'] = 'Very  severely obese'  


df.loc[df['BMI Category'] == 'Underweight'  ,'Health risk'] = 'Malnutrition risk'

df.loc[df['BMI Category'] == 'Normal Weight'  ,'Health risk'] = 'Low risk'

df.loc[df['BMI Category'] == 'Overweight'  ,'Health risk'] = 'Enhanced risk'

df.loc[df['BMI Category'] == 'Moderately obese'  ,'Health risk'] = 'Medium risk'

df.loc[df['BMI Category'] == 'Severely obese'  ,'Health risk'] = 'High risk'

df.loc[df['BMI Category'] == 'Very severely obese'  ,'Health risk'] = 'Very high risk'

print(df)

print('_'*40)
print('Gender Count')
print('_'*40)
print(df['Gender'].value_counts())

print('_'*40)
print('Health Risk')
print('_'*40)

print(df['Health risk'].value_counts())

print('_'*40)
print('BMI Catefory')
print('_'*40)
print(df['BMI Category'].value_counts())


