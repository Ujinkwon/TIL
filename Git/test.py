<<<<<<< HEAD
def get_middle_char(text):
    if len(text) % 2 == 0:
        center = len(text) // 2
        return text[center-1:center + 1]
    else:
        center = len(text) // 2
        return text[center]
print(get_middle_char('power'))
=======
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)
factorial(4)
>>>>>>> 4d07da1eacd904ee798ad141b37107dc74f7e00d
