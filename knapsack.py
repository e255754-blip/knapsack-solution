items = list(range(1, 19))
goods = [4, 8, 3, 5, 9, 2, 3, 1, 5, 2, 4, 2, 7, 10, 3, 13, 11, 8]
prices = [6, 12, 4, 3, 7, 1, 3, 2, 7, 3, 4, 2, 10, 13, 5, 16, 14, 9]
max_capacity = 45

best_value = 0
best_goods = []
best_total_capacity = 0

n = len(items) 

for i in range(2**n):
    pattern = format(i, f"0{n}b")
    
    now_capacity = 0
    now_value = 0
    now_goods = []
    
    for j in range(n):
        if pattern[j] == "1":
            now_capacity += goods[j]
            now_value += prices[j]
            now_goods.append(items[j])
            
    if now_capacity <= max_capacity and now_value > best_value:
        best_value = now_value
        best_total_capacity = now_capacity
        best_goods = now_goods

print(f"選んだ品物の組み合わせ (番号): {best_goods}")
print(f"総値段 (最大価値): {best_value}")
print(f"総容量: {best_total_capacity} / {max_capacity}")