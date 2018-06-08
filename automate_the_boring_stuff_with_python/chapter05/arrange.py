def display_inventory(item):
    total = 0
    for k, v in item.items():
        print(v,k)
        total += v
    print(total)

items = {"rope":1, "torch":6, "gold coin":42, "danger":1, "arrow":12}
display_inventory(items)