def items_to_restock(current_stock, minimum_levels):
    restock = []
    for item in current_stock:
        if item in minimum_levels:
            if current_stock[item] < minimum_levels[item]:
                restock.append(item)
    return restock
print(items_to_restock({'rice': 5,'beans': 20}, {'rice': 10, 'beans': 15}))