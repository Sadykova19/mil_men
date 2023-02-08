energy = 1000
spent_energy = 0
recovered_energy = 0

activities = {
    1: 100,
    2: 60,
    3: 180,
    4: 200,
    -1: 60,
    -2: 150,
    -3: 500
}

for i in range(10 ** 6):
    action = int(input("Введите количество действий (1-4 для расходов, от -1 до -3 для восстановления): "))
    if action in activities:
        energy -= activities[action]
        spent_energy += activities.get(action, 0) if action > 0 else 0
        recovered_energy += activities.get(action, 0) if action < 0 else 0
    else:
        print("Недопустимая активность")
        continue

    if energy <= 0:
        print(f"Энергия потрачена: {spent_energy}, Энергия восстановлена: {recovered_energy}")
        break
