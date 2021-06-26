firework_effect = [int(el) for el in input().split(", ")]
explosive_power = [int(el) for el in input().split(", ")]
firework_effect_copy = firework_effect.copy()
explosive_power_copy = explosive_power.copy()

palm_firework = 0
willow_firework = 0
crossette_firework = 0

for power in range(len(explosive_power_copy)-1, -1, -1):
    if len(firework_effect) == 0 or len(explosive_power) == 0:
        break
    while not len(firework_effect) == 0 or not len(explosive_power) == 0:
        firework = 0
        current_firework = firework_effect[firework]
        current_power = explosive_power[power]

        if current_firework <= 0:
            firework_effect.remove(current_firework)
            if len(firework_effect) == 0:
                break
            continue
        if current_power <= 0:
            explosive_power.remove(current_power)
            break
        if (current_firework + current_power) % 3 == 0 and (current_firework + current_power) % 5 == 0:
            crossette_firework += 1
            firework_effect.remove(current_firework)
            explosive_power.pop(power)
            break
        elif (current_firework + current_power) % 3 == 0 and not (current_firework + current_power) % 5 == 0:
            palm_firework += 1
            firework_effect.remove(current_firework)
            explosive_power.pop(power)
            break
        elif (current_firework + current_power) % 5 == 0 and not (current_firework + current_power) % 3 == 0:
            willow_firework += 1
            firework_effect.remove(current_firework)
            explosive_power.pop(power)
            break
        else:
            firework_effect.append(current_firework -1)
            firework_effect.remove(current_firework)


if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
    print('Congrats! You made the perfect firework show!')
    if firework_effect:
        print(f"Firework Effects left: {', '.join([str(el) for el in firework_effect])}")
    if explosive_power:
        print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")
    print(f'Palm Fireworks: {palm_firework}')
    print(f'Willow Fireworks: {willow_firework}')
    print(f'Crossette Fireworks: {crossette_firework}')

else:
    print("Sorry. You can't make the perfect firework show.")
    if firework_effect:
        print(f"Firework Effects left: {', '.join([str(el) for el in firework_effect])}")
    if explosive_power:
        print(f"Explosive Power left: {', '.join([str(el) for el in explosive_power])}")

    print(f'Palm Fireworks: {palm_firework}')
    print(f'Willow Fireworks: {willow_firework}')
    print(f'Crossette Fireworks: {crossette_firework}')