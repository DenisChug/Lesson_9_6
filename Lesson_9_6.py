
def all_variants(text):
    length_text = len(text)
    for x in range(1, length_text + 1):
        for y in range(length_text - x + 1):
            yield text[y:y + x]


a = all_variants("abc")
for i in a:
    print(i)