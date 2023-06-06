def main(n):
    if n == 0:
        return -0.75
    if n >= 1:
        return (main(n - 1) / 74) - (main(n - 1)**3)
    else:
        print("???")
