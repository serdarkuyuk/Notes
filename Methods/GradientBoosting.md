This is a boosting algorithm where decision threes added one antoher sequentially.

link to
https://www.youtube.com/watch?v=Nol1hVtLOSg

1. There is a base model where outputs are average of target values (find the derivative of loss function to minimize loss function, this is the reason to get average)
2. Calculate the residuals actual-prediction(mean value)
3. Create a decision tree where it learns the residual. Target will be residuals. (residuals will be multiple a learning rate)
4. Repeat the steps until last residuals are 0

F(x) = ho(x) + L1 h1(x) + L2 h2(x) + ... + Ln hn(x)

https://en.wikipedia.org/wiki/Gradient_boosting

## requirements
* inputs, outputs
* derivatable loss function
* no of trees
