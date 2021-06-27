def math_operations(*args, **kwargs):
    current_el = 0
    for el in range(len(args)):
        if current_el == 0:
            kwargs['a'] += args[el]
            current_el += 1
        elif current_el == 1:
            kwargs['s'] -= args[el]
            current_el += 1
        elif current_el == 2:
            if args[el] == 0:
                current_el += 1
                continue
            kwargs['d'] /= args[el]
            current_el += 1
        elif current_el == 3:
            kwargs['m'] *= args[el]
            current_el += 1
        if current_el == 4:
            current_el = 0

    return kwargs

print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))