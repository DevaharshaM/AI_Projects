Here, we have used Baesian conditional probability to solve the Monty hall problem. The different scenarios to be considered can be given below-

*Assumption - Let's assume the Prize is behind Door 2*

Case: The initial probabilty of the three doors will be equal to (1/3)

Case 1: If the user chooses Door 1, Monty can only open Door 3 as the prize is behind Door 2. If the user chooses to switch, the person will win, if not loose.

Case 2: If the user chooses Door 2, Monty can show either Door 1 or Door 3. If the user doesn't choose to switch, the person will win.

Case 3: If the user chooses Door 3, Monty can only open Door 1 as the prize is behind Door 2. If the user chooses to switch, the person will win, if not loose.

Here, if the winning probability is calculated if user switches, it equals to (2/3)

The Loosing probability, if the user switch equals to (1/3)

**Python Code Implementation:**

Import PGMPY : [pip install pgmpy]