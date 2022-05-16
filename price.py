def price(books):
    discount = [1.0, 1.0, 0.95, 0.9, 0.8, 0.75]
    
    p = 0.0
    diffs = []
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
        #p += 8.0 * diff * discount[diff]
        diffs.append(diff)
    diffs.sort()
    three_num = diffs.count(3)
    five_num = diffs.count(5)
    #print(diffs)
    p = diffs.count(1)*8 + diffs.count(2)*2*8*discount[2] + diffs.count(4)*4*8*discount[4]
    #print(p)

    merge_num = three_num if three_num<five_num else five_num
    p += merge_num * 4 * 8 * 2 * discount[4]
    p += (three_num-merge_num) * 3 * 8 * discount[3]
    p += (five_num-merge_num) * 5 * 8 * discount[5]
    return p