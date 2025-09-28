def rec(n):
    print(f"llamado con {n}")
    if n == 0:
        return 1
    else:
        return n * rec(n - 1)
print(rec(10))