import psutil
# pip install psutil

# CPU stats
print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
print("CPU Cores:", psutil.cpu_count())

# RAM stats
ram = psutil.virtual_memory()
print("Total RAM:", ram.total)
print("Available RAM:", ram.available)
print("Used RAM:", ram.used)
print("RAM Usage:", ram.percent, "%")

# Hard disk stats
disk = psutil.disk_usage('/')
print("Total Disk Space:", disk.total)
print("Used Disk Space:", disk.used)
print("Free Disk Space:", disk.free)
print("Disk Usage:", disk.percent, "%")