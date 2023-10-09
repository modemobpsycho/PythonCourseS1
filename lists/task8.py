seq = input().lower().split()
res = seq.count("a") + seq.count("an") + seq.count("the")

print(f"Общее количество артиклей: {res}")