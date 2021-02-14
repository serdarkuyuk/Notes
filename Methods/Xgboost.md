Xgboost Regressor
https://www.youtube.com/watch?v=w-_vmVfpssg

(always devide to binary three)

base model is mean of independent value and calculate the residuals

contstruct a tree
- based on dependent category (could bu continues) devide the residuals
- estimate the similarities weight for each branch


for category xgboosting
similarities weight  = sum(residual)2 / (sum(Probabilit x (1-Probability)) + lambda(hyperparameter) )

for regression xgboosting
similarities weight  = sum(residual)2 / #of Residuals + lamda
