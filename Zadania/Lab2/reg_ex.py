import re

text = """Ala ma kota, a kot ma Ale.
Kot pije mleko.
Kot wszedł na płotek.
Kot spadł z płotka.
Płotek się załamał."""

# Funkcja 'findall' - Poszukuje fragmenty stringa dla danego wzorca.
words_findall = re.findall(r'\w+', text)
print("Funkcja 'findall':")
print(words_findall, "\n")

# Funkcja 'split' - Dzieli stringa przy każdym wystąpieniu wzorca.
print("Funkcja 'split':")
words_split = re.split(r'\.\n', text)
print(words_split, "\n")

# Funkcja 'sub' - Zastępuje w stringu wszystkie wystąpienia wzorca.
print("Funkcja 'sub':")
words_sub = re.sub(r'Kot', 'Kotek', text)
print(words_sub, "\n")

# Funkcja 'search' - Skanuje stringa w poszukiwaniu pierwszego miejsca, gdzie występuje wzorzec.
words_search_1 = re.search("mleko", text)
words_search_2 = re.search("woda", text)
print("Funkcja 'search':")
print(words_search_1)
print(words_search_2, "\n")

# Funkcja 'match' - Sprawdza, czy początek stringa pasuje do wzorca.
words_match_1 = re.match("Ala", text)
words_match_2 = re.match("Ania", text)
print("Funkcja 'match':")
print(words_match_1)
print(words_match_2, "\n")

# Funkcja 'fullmatch' - Sprawdza, czy cały string pasuje do wzorca.
words_fullmatch = re.fullmatch(r'[a-zA-Z0-9-\s.]+', text)
print("Funkcja 'fullmatch':")
print(words_fullmatch, "\n")

# Funkcja 'finditer' - Znajduje dopasowania wzorca w stringu jako iterator
words_finditer = re.finditer(r'[A-Z]', text)
print("Funkcja 'finditer':")
for iterator in words_finditer:
    print(iterator)

# Funkcja 'escape' - Dodaje ukośniki przed wszystkimi znakami specjalnymi w stringu.
print("\nFunkcja 'escape':")
words_escape = re.escape(text)
print(words_escape)
