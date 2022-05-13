src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [el for idx,el in enumerate(src) if src[idx-1] < el]
print(result)