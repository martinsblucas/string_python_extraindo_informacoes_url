import re


def main():
    address = "R. Frei Caneca, 148 - Centro - Rio de Janeiro - RJ, 20211-040"
    cep = get_cep_from_address(address)
    print(f"Address: {address}")
    print(f"CEP: {cep}")


def get_cep_from_address(address):
    pattern = re.compile("[0-9]{5}[-]?[0-9]{3}")
    search = pattern.search(address)
    return search.group() if search else None


if __name__ == "__main__":
    main()
