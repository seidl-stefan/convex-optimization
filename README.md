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

## Projektstruktur
* `utility/`: Enthält den mathematischen Kern des Optimierers.
    * `optimizing_utility.py`: Hauptlogik zur Portfolio-Berechnung.
* `utility/test/`: Beinhaltet alle Qualitätssicherungs-Tests.
    * `unit_testing_edge_case_lambda_rsik_0.py`: Validierung der Grenzfälle.

## Repository klonen und Portfolio-Optimierung Ausführen
```bash
# 1. Repository klonen und in den Ordner wechseln
git clone https://github.com/seidl-stefan/convex-optimization.git
cd convex-optimization

# 2. Installation der Abhängigkeiten
pip install cvxpy numpy pandas pytest

# 3. Führe die Optimierung aus (aus dem Hauptverzeichnis)
python utility/optimizing_utility.py

# 4. Führe den Test aus (aus dem Hauptverzeichnis)
pytest utility/unit_tests/unit_testing_edge_case_lambda_rsik_0.py