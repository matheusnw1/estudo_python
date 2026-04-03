
sensores = {
    "Sensor1": [25, 28, 30, 32],
    "Sensor2": [22, 24, 26],
    "Sensor3": [29, 31, 33, 35],
    "Sensor4": [20, 21, 19]
}

print("Leituras dos sensores:")
for sensor, valores in sensores.items():
    print(sensor, valores)

medias = {}

for sensor, valores in sensores.items():
    media = sum(valores) / len(valores)
    medias[sensor] = media

sensor_maior_temp = None
maior_temp = float("-inf")

for sensor, valores in sensores.items():
    temp_max = max(valores)
    if temp_max > maior_temp:
        maior_temp = temp_max
        sensor_maior_temp = sensor

sensores_alerta = []

for sensor, valores in sensores.items():
    if any(temp > 30 for temp in valores):
        sensores_alerta.append(sensor)

total_leituras = 0

for valores in sensores.values():
    total_leituras += len(valores)

print("\nMédia por sensor:", medias)
print("Sensor com maior temperatura:", sensor_maior_temp, maior_temp)
print("Sensores em alerta:", sensores_alerta)
print("Total de leituras:", total_leituras)
