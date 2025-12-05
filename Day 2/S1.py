with open("C:/Users/dmlam/Downloads/AdventOfCode2025 D-2 input.txt", "r" ) as file:
    content = file.read().split(",")

def check_invalid(n):
    if n >= 10:
        if len(str(n)) % 2 == 0:
            if str(n)[:int(len(str(n))/2)] == str(n)[int(len(str(n))/2):]:
                print(n)
                return n
        else:
            if str(n)[:int((len(str(n))+1)/2)] == str(n)[int((len(str(n)) + 1)/2):]:
                print(n)
                return n

    return 0

counter = 0
for d in content:
    print(d)
    for s in range(int(d.split("-")[0]), int(d.split("-")[1])):
        counter += check_invalid(s)
    
print(counter)
