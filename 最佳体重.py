height = 180
weight = 80
best_weight = height - 105

if weight < best_weight:
    print("偏瘦")
elif weight > best_weight:
    print("偏胖")
else:
    print("你的体重正常，完美！")