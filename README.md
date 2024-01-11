I have used Genetic algorithm to solve the 8-queens problem. Based on the genetic algorithm, I have used -

1. **Encoding scheme** : The code uses Integer encoding scheme, where the number represents the coordinates of queens placed.

2. **Fitness Function** : The number of queens attacking each other is defined as the fitness value. For optimality, the value should be as small as possible.

3. **Genetic operator** :
   
**Selection** : Roulette wheel selection i.e. random selection is made.

**Crossover** : Position of any two queens are swapped.

**Mutation** : Choosen chromosome's coordinate is increased by 1.

In the code, Deap package is used for implementing. The best position is -
                                                  *[5 → 3 → 1 → 7 → 4 → 6 → 0 → 2]*

**Python Code Implementation:**

Import Deap : [pip install deap]

Import Numpy : [pip install numpy]
