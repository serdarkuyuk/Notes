# Random Forest

## Pro of Decision Tree
1. Scale in var, means units could be not uniform (scale) for features.
2. Robust to irrelevant features. if a paramater is irrelevant, it will not be split on
3. Interpratibility : follow chart...
## Cons of Decision Tree
1. Overfit.

pruning : depth of the decision tree

# Ensemble  : a group of items work together as a whole


# Idea 1
## Bagging : Train N tees (1000) - varieties in rows

for each tree random sampling 80/20 train end test...
pick what majority of the trees predict.

This will allow to get uncertainty...
however if one feature is very important over emphasized, all trees are correlated.

# Idea 2
## Random Subspace - variablity of columns
At each split, only consider subset of features (p)
classification : sqrt(p) regression p/2  


Cons: computational complexity
uninterpreability due to many decision trees

## Feature Importance
1. accuracy on the ith training set
2. permute the jth feature
3. accuracy on permuted training set
4. average over all training sets
