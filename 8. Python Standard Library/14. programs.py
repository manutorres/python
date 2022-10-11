import subprocess

powershell = "C:/Program Files/PowerShell/7/pwsh.exe"
# command = "ls"
command = "Get-ChildItem -Name"  # Equivalente
completado = subprocess.run(
    [powershell, "-Command", command],
    capture_output=True,
    text=True)  # Stdout a string

print("Args", completado.args)
print("Returncode", completado.returncode)
print("Stderr", completado.stderr)
print("Stdout", completado.stdout)

try:
    completado = subprocess.run(
        ["python", "scriptt.py"],
        capture_output=True,
        text=True,  # Stdout a string
        check=True)  # Lanza excepcion en caso de error
    print("Args", completado.args)
    print("Returncode", completado.returncode)
    print("Stderr", completado.stderr)
    print("Stdout", completado.stdout)
except subprocess.CalledProcessError as ex:
    print("Excepcion capturada:", ex)
