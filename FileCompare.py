from collections import Counter

brandIds = []
brandnames = []

file1 = open("D:\\POI_ATTRIBUTE_VALUE_3_hrl_0_3_3_enu.txt", 'r', encoding="utf8")
for line in file1:
    brandIds.append(line.split("#")[-1])
    brandnames.append(line.split("#")[-2])
a = [item for item, count in Counter(brandIds).items() if count > 1]
if len(a) > 0:
    print(a)
else:
    print("No duplicate Brand ID's")

print("user1")
print("user2")
