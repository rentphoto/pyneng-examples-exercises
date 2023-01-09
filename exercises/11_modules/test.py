import subprocess

result = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8'])