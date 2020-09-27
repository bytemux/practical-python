# Launch app
cd porty-app
python3 print-report.py portfolio.csv prices.csv txt

# Generate app dist
python setup.py sdist

# Install app dist
python -m pip install porty-0.0.1.tar.gz
