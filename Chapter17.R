# This is just to get the data from BayesRules package

library(bayesrules)

data("voices")



write.csv(voices, "voices.csv", row.names = FALSE)