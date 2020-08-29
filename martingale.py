# https://en.wikipedia.org/wiki/Martingale_(betting_system)

import random
import matplotlib.pyplot as plt

initial_budget = 1000
initial_bet = 1
rounds = 1000

results = [1, 0, -1] # RED, 0, BLACK
distribution = [18/37 , 1/37, 18/37]

budgets = [initial_budget]
bets = [initial_bet]

budget = initial_budget
bet = initial_bet

for i in range(0, 1000):
    result = random.choices(results, distribution)[0]
    if result == 1:
       budget += bet
       bet = initial_bet
    else:
        budget -= bet
        bet = bet*2
        # bet = min(bet*2, 2000) use max bet
        
    if budget <= 0:
        print("Bankrupt")
        break
    
    budgets.append(budget)
    bets.append(bet)
    
plt.plot(budgets)
plt.plot(bets)

print("Final budget: ", budget)
print("Max bet: ", max(bets))

plt.show()