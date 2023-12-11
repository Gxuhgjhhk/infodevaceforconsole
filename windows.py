import py3nvml
import platform
import psutil


def get_system_info():
    print("Информация о компьютере:")
    print("Операционная система:", platform.system())
    print("Имя пользователя:", platform.node())
    print("Процессор:", platform.processor())
    print("Время работы компьютера:", get_uptime())
    print("Видеокарта:", get_gpu_info())
    print("Диски:")
    print(get_disk_info())
    print("Нагрузка CPU (%):", psutil.cpu_percent())
    print("Запущенные процессы:")
    print(get_running_processes())

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_hours = int(uptime_seconds // 3600)
        uptime_minutes = int((uptime_seconds % 3600) // 60)
        return f"{uptime_hours} часов {uptime_minutes} минут"

def get_gpu_info():
    try:
        py3nvml.nvmlInit()
        device_count = py3nvml.nvmlDeviceGetCount()
        gpu_info = [f"Количество доступных GPU: {device_count}"]
        for i in range(device_count):
            handle = py3nvml.nvmlDeviceGetHandleByIndex(i)
            name = py3nvml.nvmlDeviceGetName(handle)
            gpu_info.append(f"GPU {i+1}: {name.decode('utf-8')}")
        return "\n".join(gpu_info)
    finally:
        py3nvml.nvmlShutdown()
    
def get_disk_info():
    disks = psutil.disk_partitions()
    disk_info = []
    for disk in disks:
        disk_usage = psutil.disk_usage(disk.mountpoint)
        disk_info.append(f"Диск {disk.device}: Общий объем - {disk_usage.total}, Доступно - {disk_usage.free}")
    return "\n".join(disk_info)

def get_running_processes():
    processes = psutil.process_iter()
    process_info = []
    for process in processes:
        process_info.append(f"PID: {process.pid}, Имя: {process.name()}")
    return "\n".join(process_info)

if __name__ == "__main__":
    get_system_info()