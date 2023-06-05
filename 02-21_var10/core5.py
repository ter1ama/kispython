def main(x):
    sum = 0
    for i in range(len(x)):
        parenthesis = ((83 * x[i]) + ((x[i]) ** 3) + 0.01) ** 7
        undersum = 70 * parenthesis
        sum += undersum
    result = sum * 69
    return result
