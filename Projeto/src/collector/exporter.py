from prometheus_client import start_http_server, Gauge, Counter
import time
from src.collector.metrics import (
    get_cpu_metrics,
    get_memory_metrics,
    get_disk_metrics,
    get_user_metrics
)

# Métricas de CPU
cpu_percent = Gauge('system_cpu_percent', 'CPU usage percentage')
cpu_count = Gauge('system_cpu_count', 'Number of CPU cores')

# Métricas de Memória
memory_percent = Gauge('system_memory_percent', 'Memory usage percentage')
memory_used = Gauge('system_memory_used_bytes', 'Memory used in bytes')
memory_total = Gauge('system_memory_total_bytes', 'Total memory in bytes')

# Métricas de Disco
disk_percent = Gauge('system_disk_percent', 'Disk usage percentage')
disk_used = Gauge('system_disk_used_bytes', 'Disk used in bytes')
disk_total = Gauge('system_disk_total_bytes', 'Total disk space in bytes')

def update_metrics():
    # Pegar dados de CPU
    cpu_data = get_cpu_metrics()
    cpu_percent.set(cpu_data['cpu_usage'])
    cpu_count.set(cpu_data['cpu_count'])
    
    # Pegar dados de memória
    memory_data = get_memory_metrics()
    memory_percent.set(memory_data['memory_percent'])
    memory_used.set(memory_data['memory_used'])
    memory_total.set(memory_data['memory_total'])
    
    # Pegar dados de disco
    disk_data = get_disk_metrics()
    disk_percent.set(disk_data['disk_percent'])
    disk_used.set(disk_data['disk_used'])
    disk_total.set(disk_data['disk_total'])


def run():
    # Iniciar servidor HTTP na porta 8000
    start_http_server(8000)
    print("Servidor iniciado na porta 8000")
    print("Acesse: http://localhost:8000/metrics")
    
    try:
        # Loop infinito
        while True:
            update_metrics()  # Atualizar métricas
            time.sleep(5)     # Esperar 5 segundos
    except KeyboardInterrupt:
        print("\nEncerrando servidor...")


if __name__ == '__main__':
    run()