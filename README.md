# Multple_linear_regression
Multiple linear Regression

Backward elimination is a feature selection technique commonly used in regression analysis to identify and remove insignificant independent variables from a regression model. This process helps in simplifying the model and improving its interpretability by eliminating variables that do not contribute significantly to the prediction.

Performing backward elimination in Excel involves these steps:

Step 1: Prepare Your Data
Organize your data with the dependent variable (the one you want to predict) and independent variables (potential predictors) in columns.

Step 2: Initial Regression
Start by performing a multiple linear regression analysis using all the independent variables. This is the initial model you will work with.

Step 3: Analyze the p-values
For each independent variable, look at its p-value in the regression output. The p-value indicates the significance of each variable's contribution to the model. A higher p-value suggests that the variable might not be contributing significantly.

Step 4: Eliminate Insignificant Variables
Remove the variable with the highest p-value from your model. This is typically the one with the highest p-value above a certain significance level (often 0.05 or 0.1).

Step 5: Refit the Model
Run the regression again with the remaining variables.

Step 6: Repeat the Process
Continue the process of eliminating the variable with the highest p-value and refitting the model until all remaining variables have p-values below your chosen significance level.




