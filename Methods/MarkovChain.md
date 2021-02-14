# Markov Chain Algorithm

state = {sunny, cloud}
the current state only depends on the previous state.
Markov Assumption = P(Wt|Wt-1,Wt-2...) = P(Wt|Wt-1)
Transition Matrix =

                sunny(t) | cloudy(t)
sunny(t-1)      0.3         0.7
cloudy(t-1)     0.5         0.5

steady state
sunny    1      0.7     0.56          ...  same         
cloudy   0      0.3     0.44        .....  same

sunny x 0.3 + cloudy x 0.7 = 1
sunny + cloudy = 1

sunny = 0.42 cloudy 0.58


# MCMC Markov Chain Monte Carlo
