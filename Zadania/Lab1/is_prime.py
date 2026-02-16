def is_prime(number: int):
    if number < 2:
        print("Liczba '" + str(number) + "' nie jest liczbą pierwszą")
        return
    if number == 2:
        print("Liczba '2' jest liczbą pierwszą")
        return
    if (number % 2) == 0:
        print("Liczba '" + str(number) + "' nie jest liczbą pierwszą")
        return
    czy_pierwsza = True
    dzielnik = 3
    while dzielnik <= (number / 2) + 1:
        if number % dzielnik == 0:
            czy_pierwsza = False
            break
        dzielnik += 2
    if czy_pierwsza:
        print(f"Liczba '" + str(number) + "' jest liczbą pierwszą")
    else:
        print(f"Liczba '" + str(number) + "' nie jest liczbą pierwszą")

is_prime(0)
is_prime(1)
is_prime(2)
is_prime(3)
is_prime(4)
is_prime(5)
is_prime(9)
is_prime(10)
is_prime(11)
is_prime(12)
is_prime(13)
