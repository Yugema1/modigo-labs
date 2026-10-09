def replace_first(items, new_value):
    if not items:
        return ()
    else:
        items = list(items)
        items[0] = new_value
        return tuple(items)
print(replace_first((), 9))