def get_middle_char(text):
    if len(text) % 2 == 0:
        center = len(text) // 2
        return text[center-1:center + 1]
    else:
        center = len(text) // 2
        return text[center]
print(get_middle_char('power'))