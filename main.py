import psxdata
import csv
import os
from datetime import date

stocks = [
    "AVN", "BNL", "BWCL", "DGKC", "EFERT", "ENGROH", "EPQL",
    "FABL", "FATIMA", "FFC", "GGL", "GLAXO", "HUBC", "LCI",
    "LOTCHEM", "LUCK", "MEBL", "MLCF", "NATF", "NCPL", "NML",
    "OGDC", "PAEL", "PIBTL", "PSO", "SEARL", "SELECT", "SLM",
    "SNGP", "SSGC", "SYS", "UNITY"
]

csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "psx_prices.csv")

with open(csv_file, "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow(["Symbol", "Live Price"])

    for stock in stocks:
        try:
            #data = psxdata.stocks(stock, start=date.today(), end=date.today(), cache=False)
            data = psxdata.quote(stock, cache=False)

            if not data.empty:
                #price = data.iloc[0]["close"]
                price = data.iloc[0]["price"]
            else:
                price = ""

        except Exception as e:
            print(f"{stock}: Error - {e}")
            price = ""

        writer.writerow([stock, price])
