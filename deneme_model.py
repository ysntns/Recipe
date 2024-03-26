'''
Data Scientist Professional Practical Exam Submission
Use this template to write up your summary for submission. Code in Python or R needs to be included.

'''

## 📝 Task List

'''
Your written report should include both code, output and written text summaries of the following:
- Data Validation:   
  - Describe validation and cleaning steps for every column in the data 
- Exploratory Analysis:  
  - Include two different graphics showing single variables only to demonstrate the characteristics of data  
  - Include at least one graphic showing two or more variables to represent the relationship between features
  - Describe your findings
- Model Development
  - Include your reasons for selecting the models you use as well as a statement of the problem type
  - Code to fit the baseline and comparison models
- Model Evaluation
  - Describe the performance of the two models based on an appropriate metric
- Business Metrics
  - Define a way to compare your model performance to the business
  - Describe how your models perform using this approach
- Final summary including recommendations that the business should undertake
'''

'''
About Tasty Bytes
Tasty Bytes was founded in 2020 in the midst of the Covid Pandemic. The world wanted inspiration so we decided to provide it. We started life as a search engine for recipes, helping people to find ways to use up the limited supplies they had at home.
Now, over two years on, we are a fully fledged business. For a monthly subscription we will put together a full meal plan to ensure you and your family are getting a healthy, balanced diet whatever your budget. Subscribe to our premium plan and we will also deliver the ingredients to your door.
Example Recipe
Servings: 4
Time to make: 2 hours
Category: Lunch/Snack
Cost per serving: $
Nutritional Information (per serving)
Nutrient
Value
Calories
123
Carbohydrate
13g
Sugar
1g
Protein
4g
Ingredients
Tomatoes
Onion
Carrot
Vegetable Stock
Method
Cut the tomatoes into quarters…
'''

'''
⚕️ Data Information ℹ️
The product manager has tried to make this easier for us and provided data for each recipe, as well as whether there was high traffic when the recipe was featured on the home page.
As you will see, they haven’t given us all of the information they have about each recipe.
I will let you decide how to process it, just make sure you include all your decisions in your report.
Don’t forget to double check the data really does match what they say - it might not.
Column Name
Details
recipe
Numeric, unique identifier of recipe
calories
Numeric, number of calories
carbohydrate
Numeric, amount of carbohydrates in grams
sugar
Numeric, amount of sugar in grams
protein
Numeric, amount of protein in grams
category
Character, type of recipe. Recipes are listed in one of ten possible groupings (Lunch/Snacks’, ‘Beverages’, ‘Potato’, ‘Vegetable’, ‘Meat’, ’Chicken, ‘Pork’, ‘Dessert’, ‘Breakfast’, ‘One Dish Meal’).
servings
Numeric, number of servings for the recipe
high_traffic
Character, if the traffic to the site was high when this recipe was shown, this is marked with “High”.
'''

'''
Data Validation ✅✅✅
Overview
In this section, I will analyse in detail how we validate and clean our dataset. 
In the Data Validation phase, we make sure that all variables in the dataset fulfil the provided criteria. 
This includes checking for outliers, missing data and data consistency issues. 
Where necessary, we perform data cleaning operations to prepare the data for analysis.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
