from random import choice

def get_binary():
    output = []
    for i in range(8):
        output.append(choice([0,1]))
    return output

def get_binary_sum():
    output = []
    for i in range(8):
        output.append(choice([0,1]))
    return sum(output)

samps = []
counts = 0

while 0 not in samps:
    samps.append(get_binary_sum())
    counts += 1

print(samps)
print(counts)