import random

def r(n,t):
    n_mean = sum(n) / len(n)


    t_mean = sum(t) / len(t)

    lx = []
    ly = []

    def xy(x, y):
        for i in x:
            m = i - n_mean
            lx.append(m)
        for j in y:
            n = j - t_mean
            ly.append(n)

    xy(n, t)


    lxy = []
    for i in range(0, len(lx)):
        lxy.append(lx[i] * ly[i])

    n_lxy = sum(lxy)


    v_lx = []
    v_ly = []
    for i in range(0, len(lx)):
        x = lx[i] * lx[i]
        y = ly[i] * ly[i]
        v_lx.append(x)
        v_ly.append((y))

    var_lx = sum(v_lx)
    var_ly = sum(v_ly)


    denom = (var_lx * var_ly) ** 0.5

    r = n_lxy / denom
    print("carl pearson coefficient of co-relation with actual mean: ",r)

def r1(n,t):
    n_mean = random.choice(n)

    t_mean = random.choice(t)


    lx = []
    ly = []

    def xy(x, y):
        for i in x:
            m = i - n_mean
            lx.append(m)
        for j in y:
            n = j - t_mean
            ly.append(n)

    xy(n, t)



    lxy = []
    for i in range(0, len(lx)):
        lxy.append(lx[i] * ly[i])

    n_lxy = sum(lxy)


    v_lx = []
    v_ly = []
    for i in range(0, len(lx)):
        x = lx[i] * lx[i]
        y = ly[i] * ly[i]
        v_lx.append(x)
        v_ly.append((y))

    var_lx = sum(v_lx)
    var_ly = sum(v_ly)

    denom = (var_lx * var_ly) ** 0.5

    r = n_lxy / denom
    print("carl pearson coefficient of co-relation with assumed: ", r)


def manual_rank(data):
    # Create a list of tuples (value, original_index) and sort it
    indexed_data = sorted((value, index) for index, value in enumerate(data))
    ranks = [0] * len(data)  # Initialize a list to store ranks
    i = 0

    while i < len(indexed_data):
        # Get the current value and its rank
        value = indexed_data[i][0]
        start_index = i  # The starting index for tied values

        # Find the end index for the tied values
        while i < len(indexed_data) and indexed_data[i][0] == value:
            i += 1
        end_index = i  # The end index for tied values

        # Calculate average rank for ties
        average_rank = (start_index + end_index) / 2 + 0.5  # +1 for 1-based rank

        # Assign the average rank to each tied value
        for j in range(start_index, end_index):
            original_index = indexed_data[j][1]
            ranks[original_index] = average_rank

    return ranks


















