coins = float(input())
currencies = {'RUB': 2.98,
              'ARS': 0.82,
              'HNL': 0.17,
              'AUD': 1.9622,
              'MAD': 0.208}

for i in currencies:
    print(f'I will get {round(currencies[i] * coins, 2)} {i} from the sale of {coins} conicoins')

