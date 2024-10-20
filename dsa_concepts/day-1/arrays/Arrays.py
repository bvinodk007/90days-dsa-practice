expenses = [2200,2350,2001,2130,2190]
print(expenses[1] - expenses[0])
print(expenses[0] + expenses[1]+expenses[2])
print(2000 in expenses)
expenses.append(1980)
print(expenses)
expenses[3] = expenses[3] - 200
print(expenses)

heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append('black panther')
print(heros)
heros.remove('black panther')
heros.insert(3, 'black panther')
heros[1:3]=['doctor strange']
print(heros)
heros.sort()
print(heros)

max_number = int(input())
odd_numbers = []
for i in range(1, max_number):
    if i % 2 != 0:
        odd_numbers.append(i)
print(odd_numbers)