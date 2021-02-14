Xgboost Regressor
https://www.youtube.com/watch?v=w-_vmVfpssg

(always devide to binary three)

base model is mean of independent value and calculate the residuals

contstruct a tree
- based on dependent category (could be continues) divide the residuals (this means split based on a value)
- estimate the similarities weight for each branch (and the root)
- information gain = sum(branch similarity weights) - root similarity weight
- do repeat for each probable values, and construct a three where gain is maximum

- after contructing the three calculate the results (avereging the brach values) - these are yhats

yhat = base mode (averate) + learning rate (0-1) x yhats
next yhat = ho + L x Tree1 + L x Tree2

Gamma is a hyperparameter to post pruning. if gain is negative cut the brunch, it it is positive keep it.

for category xgboosting
similarities weight  = sum(residual)2 / (sum(Probabilit x (1-Probability)) + lambda(hyperparameter) )

for regression xgboosting
similarities weight  = sum(residual)2 / ()#of Residuals + lamda)


# Application

https://github.com/krishnaik06/Hyperparameter-Optimization/blob/master/Hyperparameter%20Optimization%20For%20Xgboost.ipynb

```python
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
import xgboost
params={
 "learning_rate"    : [0.05, 0.10, 0.15, 0.20, 0.25, 0.30 ] ,
 "max_depth"        : [ 3, 4, 5, 6, 8, 10, 12, 15],
 "min_child_weight" : [ 1, 3, 5, 7 ],
 "gamma"            : [ 0.0, 0.1, 0.2 , 0.3, 0.4 ],
 "colsample_bytree" : [ 0.3, 0.4, 0.5 , 0.7 ]
}

classifier=xgboost.XGBClassifier()
random_search=RandomizedSearchCV(classifier,param_distributions=params,n_iter=5,scoring='roc_auc',n_jobs=-1,cv=5,verbose=3)

random_search.best_estimator_
random_search.best_params_

classifier=xgboost.XGBClassifier(base_score=0.5, booster='gbtree', colsample_bylevel=1,
       colsample_bytree=0.5, gamma=0.4, learning_rate=0.1,
       max_delta_step=0, max_depth=6, min_child_weight=7, missing=None,
       n_estimators=100, n_jobs=1, nthread=None,
       objective='binary:logistic', random_state=0, reg_alpha=0,
       reg_lambda=1, scale_pos_weight=1, seed=None, silent=True,
       subsample=1)

```
