import numpy as np
import pandas as pd

def run_monte_carlo(age, retirement_age, savings, income, monthly_expense):
    retirement_years = retirement_age - age
    lifespan = 90 - retirement_age
    simulations = 5000

    results = []
    for _ in range(simulations):
        balance = savings
        annual_returns = np.random.normal(loc=0.07, scale=0.15, size=lifespan)
        yearly_cashflow = []

        for i in range(lifespan):
            balance *= (1 + annual_returns[i])
            balance -= monthly_expense * 12
            yearly_cashflow.append(balance)
            if balance < 0:
                break

        results.append(yearly_cashflow)

    df = pd.DataFrame(results).T.fillna(method='ffill')
    success_rate = (df.iloc[-1] > 0).mean() * 100
    return df, success_rate
