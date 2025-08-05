list = ["apple","banana","orange","apple","mango"]

unique_item = set()

for i in list:
    if i in unique_item:
        print(i)
        break
    unique_item.add(i)


