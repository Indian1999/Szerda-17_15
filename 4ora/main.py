map = []
with open("4ora/input.txt", "r", encoding="utf-8") as f:
   for line in f:
       map.append(list(line.strip())) 
       
for row in map:
    print(row)