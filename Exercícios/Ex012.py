# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

def calculate_discounted_price(price, discount):
    return price - (price * discount)

while True:
    product_price_input = input('Enter the product price in Euros: ').strip()

    try:
        product_price = float(product_price_input)
        break
    except ValueError:
        print('Invalid product price. Enter only numbers and decimals.')
        continue

discount_5 = 0.05
discount_10 = 0.10
discount_15 = 0.15

# Apply discount using if and elif
if product_price > 1000:
    discount_percentage = discount_15
elif product_price > 400:
    discount_percentage = discount_10
elif product_price > 100:
    discount_percentage = discount_5
else:
    discount_percentage = 0.0

discounted_price = calculate_discounted_price(product_price, discount_percentage)
discount_amount = product_price - discounted_price

print(f'\nOriginal price: {product_price:.2f} Euros')
print(f'Discount percentage: {discount_percentage * 100:.0f}%')
print(f'Discount amount: {discount_amount:.2f} Euros')
print(f'\nDiscounted price: {discounted_price:.2f} Euros')
