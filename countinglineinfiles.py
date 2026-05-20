# #counting lines
# file = open("sample.txt")
# count = 0
# for lines in file:
#     count = count + 1

# print(f'total lines ={count}')

# # searching through files
# file = open("sample.txt")
# for line in file:
#     line = line.strip()
#     if line.startswith('import:'):
#         print(line)

#Skipping through Lines
file = open("sample.txt")
for lines in file:
    lines=lines.strip()
    if not lines.startswith('import:'):
        continue
    print(lines)