# args
def calculate_somme(*numbers: int) -> int:
    return sum(numbers)


somme = calculate_somme(1, 2, 5, 10, 5, 54, 41, 165)
print(somme)


# kwargs
def order_car(name: str, *options: str, **details) -> str:

    print(f"you order {name} \navec les options suivantes")

    for option in options:
        print(f" - {option}")

    for key, value in details.items():
        print(f"{key}: {value}")


order_car("Tesla", "Noire", "boite auto", moteur="2KD", type="Electrique")
