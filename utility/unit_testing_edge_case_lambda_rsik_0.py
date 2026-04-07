# Wenn das Risiko egal ist (λ=0), wird nur noch die Netto-Rendite 
# (Rendite minus Steuer) maximiert. Der Optimierer sollte dann alles (100%)
# in das Asset stecken, das nach Steuern am meisten übrig lässt.

# pytest unit_testing_edge_case_lambda_rsik_0.py


import pytest

import numpy  as np
import pandas as pd
import cvxpy  as cp

from optimizing_utility import solve_portfolio


def test_diversification_high_risk_aversion():
    """
    Sanity Check & Logic Test: Hohe Risiko-Aversion.
    Wenn beide Assets ähnliche Renditen haben, aber das Risiko hoch ist,
    darf der Optimierer NICHT alles in ein Asset stecken.
    """
    # Setup: Beide Assets fast identisch in Rendite und Steuer
    expected_returns = np.array([0.10, 0.10])
    tax_impact       = np.array([0.02, 0.02])
    
    # Aber: Asset A ist extrem riskant, Asset B ist stabil
    # (Varianz von A ist 0.5, von B nur 0.01)
    cov_matrix = np.array([
        [0.50, 0.00], 
        [0.00, 0.01]
    ])
    
    # Wir setzen Lambda hoch (Angsthase)
    weights = solve_portfolio(expected_returns, cov_matrix, tax_impact, lambda_risk=10)
    
    print(f"\n[Diversifikation] Gewichte bei hohem Risiko: A: {weights[0]:.2%}, B: {weights[1]:.2%}")
    
    # --- Assertions ---
    # 1. Sanity Check (Budget & Non-Short)
    assert np.isclose(np.sum(weights), 1.0), "Budget-Constraint verletzt"
    assert np.all(weights >= -1e-9), "Short-Selling-Verbot verletzt"
    
    # 2. Logik-Check: Da B viel sicherer ist, muss B deutlich mehr Gewicht bekommen als A
    assert weights[1] > weights[0], "Fehler: Das sicherere Asset sollte höher gewichtet sein"
    
    # 3. Diversifikation: Da Lambda hoch ist, sollte A nicht 0% sein (wegen minimaler Risikostreuung),
    # aber der Großteil muss in B liegen.
    assert weights[1] > 0.80, "Fehler: Bei diesem Risikounterschied sollte B dominieren"


def test_edge_case_zero_risk_aversion():
    """
    Edge Case: Lambda = 0.
    Der Optimierer muss das gesamte Kapital in das Asset mit der 
    höchsten Netto-Rendite stecken (Corner Solution).
    Netto = Rendite - Steuern
    """
    # Daten: Asset A hat 10% Rendite, Asset B hat 8%.
    # Aber:  Asset A hat  5% Steuern, Asset B nur 1%.
    # Netto: A = 5%, B = 7% -> Alles muss in B fließen.
    expected_returns = np.array([0.10, 0.08]) # Rendite
    tax_impact       = np.array([0.05, 0.01]) # Steuern
    cov_matrix       = np.array([[0.1, 0.01], [0.01, 0.1]]) # Risiko ist hoch, sollte aber egal sein
    
    weights = solve_portfolio(expected_returns, cov_matrix, tax_impact, lambda_risk=0)

    print(f"\n[Test-Info] Netto-Renditen: A: {expected_returns[0]-tax_impact[0]:.2%}, B: {expected_returns[1]-tax_impact[1]:.2%}")
    print(f"[Test-Info] Errechnete Gewichte: Asset A: {weights[0]:.4%}, Asset B: {weights[1]:.4%}")

    # Assertions: Erwartung / Du behauptest, dass ein bestimmtes Ergebnis wahr ist.
    #assert <Bedingung>, <Optionaler Fehlertext>
    assert weights[0] < 0.001, f"Fehler: Asset A sollte fast 0% haben, hat aber {weights[0]:.2%}"
    assert weights[1] > 0.999, f"Fehler: Asset B sollte fast 100% haben, hat aber {weights[1]:.2%}"
    assert np.isclose(np.sum(weights), 1.0), f"Sanity Check fehlgeschlagen: Summe ist {np.sum(weights)}"
    assert np.all(weights >= -1e-9), "Sanity Check fehlgeschlagen: Negative Gewichte entdeckt"


# Weiterer Sanity Check
# Was passiert bei gleicher Netto-Rendite
# -> unendlich viele optimale Lösungen
# Jede Kombination, die in der Summe 100% ergibt, liefert denselben Nutzen (Utility).


# Lass den Test scheitern
# tax_impact = np.array([0.05, 0.01]) ändere z.B. zu
# tax_impact = np.array([0.01, 0.05]) sodass das Netto sich ändert

#           Rendite     Steur       Netto
# Asset A   10%         5%          5%
# Asset B    8%         1%          7%     ---> Optimzier schaufelt alles in B

#           Rendite     Steur       Netto
# Asset A   10%         1%          9%     ---> Optimzier schaufelt alles in A
# Asset B    8%         5%          3%          aber Assertion will alles in B


if __name__ == "__main__":
    # Führt die Tests aus
    print("\n--- Starte Unit Tests ---")
    pytest.main([__file__])
    
    print("\n--- Interpretation ---")
    print("Fall ein kleiner Punkt . vorkommt: Erfolg")
    print("Fall ein F vorkommt: Test fehlgeschlagen")
