def delete_nth(order,max_e):
    exit = [], counts = {}
    for i in order:
        current_count = counts.get(i, 0)
        if current_count < max_e:
            exit.append(i)
            counts[i] = current_count + 1
    return exit
