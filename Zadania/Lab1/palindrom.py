text = input("Podaj ciąg znaków do sprawdzenia palindroma: ")
text = text.lower()
size = int(len(text) / 2)
i = 0
palindrom = True
while i < size:
    if text[i] != text[-i - 1]:
        palindrom = False
        break
    i += 1
print("Czy słowo '" + text + "' to palindrom:", palindrom)
