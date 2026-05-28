
import psutil
import time

while True:

    cpu = psutil.cpu_percent(interval=1)
    memoria = psutil.virtual_memory().percent

    print(f"CPU: {cpu}%")
    print(f"Memória: {memoria}%")

    if cpu > 80:
        print("Uso de CPU muito alto!")

    if memoria > 80:
        print("Uso de memória muito alto!")

    print("-" * 30)

    time.sleep(2)
  
