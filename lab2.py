grocery_list_input = input("Введите список покупок через запятую (пример: печенье, огурцы, масло, шоколад): ")
price_list = {}

while True:
    price_list_input = input("Введите список цен на товары в магазине (пример: Десяточка: печенье:10, огурцы:20, масло:30, шоколад:100): ")
    if price_list_input == "":
        break
    else:
        shop_name = price_list_input.split(":", 1)[0]
        prices_dict = { prices_in_shop.split(":")[0]: float(prices_in_shop.replace(",", "").split(":")[1]) for prices_in_shop in price_list_input.split(" ")[1:]}
        price_list[shop_name] = prices_dict

def compare_prices(input_prices):
    compared_list = { shop : total_price(input_prices[shop]) for shop in input_prices }
    print(f'Цена продуктовой корзины составляет:')
    for i in compared_list:
        print(f'В магазине {i} --- {compared_list[i]}')
    highest_price_shop = max(compared_list, key=compared_list.get)
    lowest_price_shop = min(compared_list, key=compared_list.get)
    discount = compared_list[highest_price_shop] - compared_list[lowest_price_shop]
    print(f'Лучше всего можно сэкономить в магазине {lowest_price_shop} на сумму {discount}')

def total_price(shop):
    total = 0
    for i in shop: total += shop[i]
    return total

compare_prices(price_list)