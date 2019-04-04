records = []
record = 0

number = 0

def calc_per(num,steps=0):
    if len(str(num)) != 1:
        digits = [int(i) for i in str(num)]
        new_number = 1
        for digit in digits:
            new_number *= digit
        steps += 1
        if len(str(new_number)) != 1:
            steps = calc_per(new_number, steps)
    return steps

while True:
    steps = calc_per(number)
    if steps > record:
        print(f"steps: {steps} number: {number}")
        records.append([steps, number])
        record = steps
    number += 1
    
