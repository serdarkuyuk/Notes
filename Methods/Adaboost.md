for 7 sampe
f1, f2, f3, output Weight =
0 1/7
1 1/7

stamps - for each features ... one branch tree
and select the smallest entropy...GINI index

assume 1 sample is error... suming weigth (error) =1/7 - (TE)

performance stump = 1/2 x log ((1-TE)/TE)

new sample weight incorrect = weight x e^(performance stump)
new sample weight for correct = weight x e^-(performance stump)

normalize the weight, we have higher the weight for errored samples
create buckets 0.05-5.2, 5.2-5.7, 5.7-6.1 ............

pick random dataset (0-1) where, it is likely that the wrong samples will be picked.

with new dataset ... do the the same thing pick a stump.... with same weight

Result
feed your test data to DT1, DT2 ... --- stumps and look for the majority decision
each stumps have performance stump (amount of say), we look forward how many have a decision over the others with sum of less amount of say.
