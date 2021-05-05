text = [["Glitch", "is", "a", "minor", "problem", "that", "causes", "a", "temporary", "setback"],
        ["Ephemeral", "lasts", "one", "day", "only"],
        ["Accolade", "is", "an", "expression", "of", "praise"]]
value = int(input())
# result = []
result = [j for i in text for j in i if len(i) <= value]
# for i in text:
#     for j in i:
#         if len(j) <= value:
#             result.append(j)
print(result)
