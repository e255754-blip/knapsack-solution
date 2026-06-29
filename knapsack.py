items = list(range(1, 19))
goods = [4, 8, 3, 5, 9, 2, 3, 1, 5, 2, 4, 2, 7, 10, 3, 13, 11, 8]
prices = [6, 12, 4, 3, 7, 1, 3, 2, 7, 3, 4, 2, 10, 13, 5, 16, 14, 9]
max_capacity = 45

best_value = 0
best_goods = []
best_total_capacity = 0

n = len(items) 

for i in range(2**n):
    #２進数に変換
    pattern = format(i, f"0{n}b")
    
    now_capacity = 0
    now_value = 0
    now_items = []
    
    #n回目のパターンの値段，容量，商品リストの作成
    for j in range(n):
        if pattern[j] == "1":
            now_capacity += goods[j]
            now_value += prices[j]
            now_items.append(items[j])
            
    #比較　　容量を超えてないかつ，一回前より値段が高かったら更新
    if now_capacity <= max_capacity and now_value > best_value:
        best_value = now_value
        best_total_capacity = now_capacity
        best_items = now_items

print(f"選んだ品物: {best_items}")
print(f"最大の値段: {best_value}")
print(f"容量: {best_total_capacity} / {max_capacity}")