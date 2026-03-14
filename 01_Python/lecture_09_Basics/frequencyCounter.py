numbers = [1,2,2,3,3,3,4,4,4,4,5,5,5,5]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1
    print(f"Current: {num}, Frequency: {frequency}")  # Debug line

print(f"\nFinal result: {frequency}")