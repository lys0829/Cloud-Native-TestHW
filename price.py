def price(books):
    discount = [1.0, 1.0, 0.95, 0.9, 0.8, 0.75]
    tmp = []
    diff = 0
    for b in books:
        if b in tmp:
            continue
        diff += 1
        tmp.append(b)

    return 8.0 * diff * discount[diff] + 8.0 * (len(books)-diff)