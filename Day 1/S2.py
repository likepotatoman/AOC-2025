with open("C:/Users/dmlam/Downloads/AdventOfCode2025 D-1 input.txt", "r" ) as file:
    content = file.read()
    lines = content.splitlines()

counter = 0
dial = 50
for d in lines:
    if d[0] == "R":
        for i in range(int(d[1:])):
            dial += 1
            if dial % 100 == 0:
                counter += 1
    else:
        for i in range(int(d[1:])):
            dial -= 1
            if dial % 100 == 0:
                counter += 1
    
print(counter)
