 
import psutil

psutil.virtual_memory()
psutil.disk_partitions()

def check_system_health():
    cpu_threshold = int(input("Enter CPU threshold percentage: "))
    memory_threshold = int(input("Enter Memory threshold percentage: "))
    disk_threshold = int(input("Enter Disk usage threshold percentage: "))

    current_cpu = psutil.cpu_percent(interval=1)
    current_memory = psutil.virtual_memory().percent
    current_disk = psutil.disk_usage('/').percent

    if current_cpu > cpu_threshold:
        print(f"Warning: CPU usage is high ({current_cpu}%)")
    else:
        print(f"CPU usage is normal ({current_cpu}%)")

    if current_memory > memory_threshold:
        print(f"Warning: Memory usage is high ({current_memory}%)")
    else:
        print(f"Memory usage is normal ({current_memory}%)")

    if current_disk > disk_threshold:
        print(f"Warning: Disk usage is high ({current_disk}%)")
    else:
        print(f"Disk usage is normal ({current_disk}%)")

check_system_health()