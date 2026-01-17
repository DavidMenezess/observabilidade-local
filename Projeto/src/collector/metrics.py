import psutil
import os

# Essa função mostra o uso em % e o numero de cores do CPU
def get_cpu_metrics(): 
    return {
        'cpu_usage': psutil.cpu_percent(interval=1),
        'cpu_count': psutil.cpu_count(),
    }

def get_memory_metrics():
    memory = psutil.virtual_memory()
    return {
        'memory_total': memory.total,
        'memory_used': memory.used,
        'memory_available': memory.available,
        'memory_percent': memory.percent,
        'memory_free': memory.free,
    }

def get_disk_metrics():
    disk = psutil.disk_usage('/')
    return {
        'disk_total': disk.total,
        'disk_used': disk.used,
        'disk_percent': disk.percent,
        'disk_free': disk.free,
    }

def get_user_metrics():
    return {
        'current_user': os.getenv('USER'),
    }