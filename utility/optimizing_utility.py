# Optimier / Maximiere die Utility
# utility = Rendite - Risiko - Steuer
#
# Die Steuer-Strafe wurde linear angehängt

import numpy  as np
import pandas as pd
import cvxpy  as cp


#def solve_portfolio(expected_returns, cov_matrix, tax_impact, lambda_risk):
def solve_portfolio(
    expected_returns: np.ndarray,  # Muss ein NumPy-Array sein
    cov_matrix:       np.ndarray,  # Muss ein NumPy-Array sein
    tax_impact:       np.ndarray,  # Muss ein NumPy-Array sein
    lambda_risk:      float        # Muss ein Float sein
) -> np.ndarray:                   # Funktions-Output ist ein Array
    
    n = len(expected_returns)
    w = cp.Variable(n)
    
    portfolio_return = expected_returns @ w
    portfolio_risk   = cp.quad_form(w, cov_matrix)
    tax_penalty      = tax_impact @ w
    
    utility = portfolio_return - (lambda_risk / 2) * portfolio_risk - tax_penalty
    
    objective = cp.Maximize(utility)
    
    constraints = [cp.sum(w) == 1, w >= 0]

    prob = cp.Problem(objective, constraints)
    prob.solve()
    return w.value



if __name__ == "__main__":
    # Test Daten
    data = {
        'MU': [120.50, 128.30, 132.90, 125.10, 135.00, 146.40, 165.20],
        'WM': [210.10, 211.00, 210.80, 212.50, 213.10, 214.20, 215.00]
    }

    df = pd.DataFrame(data)
    returns          = df.pct_change().dropna()

    # Parameter vorbereiten
    expected_returns = returns.mean().values
    cov_matrix       = returns.cov().values
    lambda_risk      = 5.0
    est_tax_impact   = np.array([0.05, 0.005]) # Buchgewinne

    weights = solve_portfolio(expected_returns, cov_matrix, est_tax_impact, lambda_risk)


    # Normaler Output
    print("\n--- Optimierungsergebnis ---")
    print(f"MU: {weights[0]:.2%}, WM: {weights[1]:.2%}")

