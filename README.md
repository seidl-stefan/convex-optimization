# Convex Portfolio Optimization von Stefan

Ein Python-basiertes System zur mathematischen Optimierung von Anlageportfolios unter Berücksichtigung von Risiko, Rendite und steuerlichen Auswirkungen. 

Das Skript nutzt konvexe Optimierung (`cvxpy`), um die ideale Gewichtung von Assets zu finden, die den Netto-Nutzen (Rendite abzüglich Risiko-Malus und Steuer-Strafe) maximiert.

## Kernfunktionen
* **Markowitz-Optimierung:** Berechnung der Efficient Frontier mittels quadratischer Programmierung.
* **Steuer-Modellierung:** Integration linearer Steuerbelastungen (Tax Impact) direkt in die Zielfunktion.
* **Risiko-Management:** Variabler Parameter $\lambda$ zur Steuerung der individuellen Risiko-Aversion.
* **Edge-Case Validierung:** Überprüfung mathematischer Grenzfälle (z.B. reine Renditemaximierung bei $\lambda = 0$).

## Tech Stack
* **Sprache:** Python 3.x
* **Module:** `cvxpy` (Optimierung), `numpy` (Matrizenrechnung), `pandas` (Datenhandling), `pytest` (Testing)

## Repository klonen
```bash
# Repository klonen
git clone [https://github.com/seidl-stefan/convex-optimization.git](https://github.com/seidl-stefan/convex-optimization.git)

# Wechsle in den Ordner
cd convex-optimization

# Installation der Abhängigkeiten
pip install cvxpy numpy pandas pytest

# Führe die Optimierung oder den Test aus
python optimizing_utility.py
pytest unit_testing_edge_case_lambda_rsik_0.py