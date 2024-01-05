def reverse_text(string):
    i = len(string) - 1
    n = 0
    while i >= n:
        yield string[i]
        i -= 1


for char in reverse_text("step"):
    print(char, end='')
