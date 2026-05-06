# 1. Start mit einem Python-Betriebssystem
FROM python:3.10-slim

# 2. Arbeitsverzeichnis im Container festlegen
WORKDIR /app

# 3. requirements.txt kopieren und installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Deinen Code kopieren
COPY . .

# 5. Was soll passieren, wenn der Container startet?
CMD ["python", "main.py"]
