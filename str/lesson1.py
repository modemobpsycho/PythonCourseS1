short, *_, long = sorted(
    [input(), input(), input()], key=len
)  # Вывести из трех слов самое длинное и самое короткое
print(short, long, sep="\n")
