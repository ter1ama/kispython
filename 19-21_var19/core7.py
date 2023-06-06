def main(s):
    s1 = int(s[0], base=16)
    s2 = int(s[1], base=16)
    s3 = int(s[2], base=16)
    s5 = int(s[3], base=16)
    return hex((s5 << 9) | (s3 << 6) | (s2 << 4) | (s1 << 0))
