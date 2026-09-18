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

csv_file = os.path.join( os.path.dirname(os.path.abspath(__file__)), "psx_prices.csv")

today = date.today()

with open(csv_file, "w", newline="") as file:

    writer = csv.writer(file)
    writer.writerow(["Symbol", "Live Price"])
    for stock in stocks:
        price = ""
        try:
            data = psxdata.quote(stock, cache=False)
            if not data.empty and "price" in data.columns:
                value = data.iloc[0]["price"]
                if value is not None and str(value).strip() != "":
                    price = value
                    print(f"{stock}: {price}  [quote]")

        except Exception as e:
            print(f"{stock}: Quote error - {e}")
        if price == "":
            try:
                data = psxdata.stocks(
                    stock,
                    start=today,
                    end=today,
                    cache=False
                )

                if not data.empty:
                    # Make sure we use today's row
                    data["date"] = data["date"].astype(str)

                    today_data = data[
                        data["date"].str.startswith(str(today))
                    ]

                    if not today_data.empty:
                        value = today_data.iloc[-1]["close"]

                        if value is not None and str(value).strip() != "":
                            price = value
                            print(f"{stock}: {price}  [stocks fallback]")

            except Exception as e:
                print(f"{stock}: Fallback error - {e}")

        # ---------------------------------------------------------
        # 3. Nothing found
        # ---------------------------------------------------------
        if price == "":
            print(f"{stock}: PRICE NOT FOUND")

        writer.writerow([stock, price])