# Mixture of Gaussion

unsupervised
probabilit of x is if low from a threshold...

p(x) < epsilion

Expectation - Maximization Algorithm

Suppose there is a latent (hidden/unobserved) random variable z and
x, z are distributed

P(x,z) = P(x|z) P(z)
where z is multinomal (Pi)
x|z ~ N(mean, E)

if we know the z's can use MLE
logLikelihood(pi, mean, E) = Sum log p(x,z; pi, mean, E)

pi, mean , E know formula but we do not know z....

E step: (Expectation step) : Guess value of z's

estimate the w's probability -> bayeshian formula
w's is how much x is assigned to the M(mean) gaussian

M step: (Maximization step)
calculate phi, mean, and E

- in kmeans the data in between classes, assign strictly to one group where in GMM we calculate the probability of belonging classes
