items = list(range(1, 19))
weights = [4, 8, 3, 5, 9, 2, 3, 1, 5, 2, 4, 2, 7, 10, 3, 13, 11, 8]
values = [6, 12, 4, 3, 7, 1, 3, 2, 7, 3, 4, 2, 10, 13, 5, 16, 14, 9]
max_capacity = 45

best_value = 0
best_items = []
best_total_weight = 0  

n = len(items) 

for i in range(2**n):
    # 2進数に変換
    pattern = format(i, f"0{n}b")
    
    current_weight = 0 
    current_value = 0   
    current_items = []  
    
    # n回目のパターンの重さ、価値、品物リストの作成
    for j in range(n):
        if pattern[j] == "1":
            current_weight += weights[j]
            current_value += values[j]
            current_items.append(items[j])
            
    #比較　　容量を超えてないかつ，一回前より値段が高かったら更新
    if current_weight <= max_capacity and current_value > best_value:
        best_value = current_value
        best_total_weight = current_weight
        best_items = current_items

print(f"選んだ品物: {best_items}")
print(f"最大の値段: {best_value}")
print(f"容量: {best_total_weight} / {max_capacity}")