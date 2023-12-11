import platform
import psutil


def get_system_info():
    print("Информация о компьютере:")
    print("Операционная система:", platform.system())
    print("Имя пользователя:", platform.node())
    print("Процессор:", platform.processor())
    print("Время работы компьютера:", get_uptime())
    print("Видеокарта:", "Недоступно на Linux")
    print("Диски:")
    print(get_disk_info())
    print("Нагрузка CPU (%):", psutil.cpu_percent())
    print("Запущенные процессы:")
    print(get_running_processes())

def get_uptime():
    uptime_seconds = float(open('/proc/uptime').read().split()[0])
    uptime_hours = int(uptime_seconds // 3600)
    uptime_minutes = int((uptime_seconds % 3600) // 60)
    return f"{uptime_hours} часов {uptime_minutes} минут"

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