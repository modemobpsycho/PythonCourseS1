strings = input()

digits = [s for s in strings if s.isdigit()]

print(*digits, sep="")