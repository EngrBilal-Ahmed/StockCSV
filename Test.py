import psxdata

for symbol in ["BWCL", "GLAXO", "LUCK", "EFERT"]:
    print("\n================", symbol, "================")

    data = psxdata.screener()

    print(data.to_string())