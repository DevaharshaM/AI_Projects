I have implemented fuzzy controller for washing maachine using scikit-fuzzy package. Here, there are three linguistic variables i.e Degree of dirtiness, Size of load clothes and Washing time. The linguistic variables Degree of Dirtiness and Size of load clothes are inputs and Washing time is the output. The controller is designed using 5 rules which are given in as Fuzzy Associative memory. The washing time when degree of diriness is 60% and Size of the load clothes in 70% is calculated using aggregation of clipped washing time and the defuzzification method is mean of maxima (MoM). 

The formula for the Mean of Maxima is given as -

                                    $MoM = \sum_{x=a}^{b} \frac{\mu_A(x).x}{|M|}$

where a,b are min and max membership values respectively

The suggested washing time comes approximately at 36.4 with a membership function of 0.6

**Python Code Implementation:**

Import Skfuzzy : [pip install scikit-fuzzy]
Import Numpy : [pip install numpy]
Import Matplot : [pip install matplotlib]
