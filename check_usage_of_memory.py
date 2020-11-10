import os
import psutil

def check_usage_of_memory():
    pid = os.getpid()
    py = psutil.Process(pid)
    memory_usage = round(py.memory_info()[0]/2.**30, 2)
    print("memory usage :", memory_usage)