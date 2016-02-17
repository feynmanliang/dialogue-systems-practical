library(ggplot2)

data = read.csv("mcc-data.csv")
str(data)

ggplot(data, aes(x=100*Iteration, y=Success.Mean, colour=factor(Nu))) +
  geom_line() +
  scale_y_continuous() +
  labs(title="MCC with Focus Tracker (r=0.15)",
       x="Iterations", y="Average Success (Testing Set)", colour="Nu")
