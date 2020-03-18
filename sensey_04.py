# інтераткивний підруОснови Python. Контрольні завдання 4

def double_tuple(value):
    '''takes a tuple of any numbers or strings and modifies it into a tuple of tuples of two elements (in pairs)'''
    return tuple([value[i:i + 2] for i, item in enumerate(value) if i % 2 == 0])


def trimmed_text(text, limit):
    '''the function truncates the text, the words do not break off in the middle (exception is the first word), and at the end adds "..."'''
    ellipsis = "..."
    len_text = len(text)
    if limit < len_text:
        index = text.rfind(' ', 0, (limit - 2))
        if index == -1:
            index = limit - len(ellipsis)
        return text[:index].rstrip(',.:;!?') + ellipsis
    return text


print(double_tuple.__doc__)
print(double_tuple((1, 4, 8, 6, 3, 7, 1)))

print(trimmed_text.__doc__)
print(trimmed_text( "Proin eget tortor risus", 24))  # "Proin eget tortor risus"
print(trimmed_text("Proin eget tortor risus.", 23))  # "Proin eget tortor..."
print(trimmed_text("Proin eget tortor risus.", 6))  # "Pro..."

