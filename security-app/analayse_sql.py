import subprocess

def start_sqlmap():
    target_url = "http://localhost/3306"
    command = f"sqlmap -u {target_url} --batch --dbs"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if error:
        print("Error:", error.decode())
    else:
        print("SQLMap output:")
        print(output.decode())

start_sqlmap()