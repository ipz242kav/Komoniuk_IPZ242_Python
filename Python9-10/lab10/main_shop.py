from shop import Shop

all_store = Shop("МійМагазин", "Універсальний", 100)
print(f"Назва магазину: {all_store.shop_name}")
all_store.describe_shop()
all_store.open_shop()
