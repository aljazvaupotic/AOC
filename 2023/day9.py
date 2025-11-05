import time


def calculate_differences(arr):
    if all(diff == 0 for diff in arr):
        arr.append(0)
        return arr

    differences = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    result = arr.copy()
    result.append(calculate_differences(differences)[-1] + arr[-1])
    return result


def calculate_differences2(arr):
    if all(diff == 0 for diff in arr):
        arr.insert(0, 0)
        return arr

    differences = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]
    result = arr.copy()
    result.insert(0, result[0] - calculate_differences2(differences)[0])
    return result


st = time.time()
# f = open("demo9.txt")
f = open("input9.txt")
data = f.readlines()
values = [(x.strip()).split(" ") for x in data]
m = reversed(values)
r = []
f = []
for line in values:
    tmp = list(map(int, line))
    r.append(calculate_differences(tmp)[-1])
    f.append(calculate_differences2(tmp)[0])


print(sum(r), sum(f))

print(" Total run time")
print("--- %s seconds ---" % (time.time() - st))
t = time.time()
a = []
for line in values:
    tmp = list(map(int, line))
    a.append(calculate_differences(tmp)[-1])
print(sum(r))
print(" Total run time")
print("--- %s seconds ---" % (time.time() - t))