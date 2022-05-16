def price(books):
    discount = [1.0, 1.0, 0.95, 0.9, 0.8, 0.75]
    
    p = 0.0
    while len(books) != 0:
        tmp = []
        diff = 0
        topop = []
        for i in range(len(books)):
            b = books[i]
            if b in tmp:
                continue
            diff += 1
            tmp.append(b)
            topop.append(i)
        newbooks = []
        for i in range(len(books)):
            if i in topop:
                continue
            newbooks.append(books[i])
        books = newbooks
        p += 8.0 * diff * discount[diff]

    return p