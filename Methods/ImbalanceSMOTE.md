1. Under sampling majority class
   99000 vs 1000  
   99000 -> 1000 vs 1000
   not prefered since you throw away so much data
2. Over sampling the minority class by duplication
   99000 vs 1000
   1000x99 leads 99000 vs 99000
3. Over sampling the minority class by SMOTE (syntetic Minority Over-sampling Technique) using k-nearest neighbors algorithm
   imbalanced learning (https://imbalanced-learn.org/stable/auto_examples/index.html#general-examples)
4. Ensemble Method
   3000 vs 1000
   train 3 models by dividing 3000 to 1000 vs 1000
   and do the majority vote
5. Focal Loss
   will penalize majority samples during loss calculation and give more weight to minority class samples. (https://medium.com/analytics-vidhya/how-focal-loss-fixes-the-class-imbalance-problem-in-object-detection-3d2e1c4da8d7#:~:text=Focal%20loss%20is%20very%20useful,is%20simple%20and%20highly%20effective)

for example : customer churn rate, device failure, cancer prediction