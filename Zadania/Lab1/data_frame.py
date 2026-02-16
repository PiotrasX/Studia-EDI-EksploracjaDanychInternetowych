import pandas as pd

data = {
    "substancja": ["tlen", "magnez", "żelazo", "chlor", "wodór", "promet"],
    "gęstość (kg/m³)": [1.429, 1738, 7874, 3.214, 0.082, 7264],
    "topnienie (°C)": [-218.79, 650, 1538, -101.5, -259.198, 1042],
    "wrzenie (°C)": [-182.962, 1090, 2861, -34.04, -252.762, 3000]
}

df = pd.DataFrame(data)

print("Wypisanie całej ramki:")
print(df)

print("\nWypisanie drugiej kolumny")
print(df["gęstość (kg/m³)"])

print("\nSprawdzenie drugiej kolumny, czy wartości są większe od 10")
print(df["gęstość (kg/m³)"] > 10)

print("\nWypisanie trzeciego wiersza:")
print(df.loc[2])

print("\nWypisanie pierwszych trzech wierszy:")
print(df.head(3))

print("\nWypisanie ostatnich dwóch wierszy:")
print(df.tail(2))
