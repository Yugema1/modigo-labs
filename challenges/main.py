#Inventory Report Builder
def inventory_report(items):
    if not items:
        return {'total_value': 0, 'most_valuable': None, 'low_stock': []}
    total_value = 0
    max_value = -1
    most_valuable = None
    low_stock_names = []
    
    for name, quantity, price in items:
        item_value = quantity * price
        total_value += item_value
        if item_value > max_value:
            max_value = item_value
            most_valuable_name = name
        if quantity < 5:
            low_stock_names.append(name)
    return {
        'total_value': round(total_value, 2), 
        'most_valuable': most_valuable_name,
        'low_stock': sorted(low_stock_names)
    }
print(inventory_report([('pen', 10, 1.5), ('book', 2, 12.0), ('bag', 4, 20.0)]))