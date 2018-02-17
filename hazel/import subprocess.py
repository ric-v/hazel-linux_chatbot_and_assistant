import subprocess
out_bytes = subprocess.Popen(['netstat','-a'])
print out_bytes