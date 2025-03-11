import os
import subprocess

from platform import system
from sys import version_info, executable

def check_python_version():
    if version_info[0:3] >= (3,13,0):
        return True
    else:
        return False

def check_if_pip_is_installed():
    import subprocess

    try:
        subprocess.run(["pip", "--version"], check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError:
        return False

def install_pip():
    subprocess.run([executable, "-m", "ensurepip"])
    print("\nPIP has been installed.")

def check_uv_is_installed():
    output = subprocess.check_output([executable, '-m', 'pip', 'list'], text=True)
    output = output.split('\n')
    for item in output[2:]:
        if "uv" == item.split(" ")[0].strip():
            print("\nUV is already installed.")
            return True
    return False

def install_uv():
    subprocess.run([executable, '-m', 'pip', 'install', 'uv'])
    print("\nUV has been installed.")

def create_venv(version):
    subprocess.run([executable,"-m","uv", "venv", ".venv", f"--python={version}"], check=True)
    print('\nVirtual Environment Created.')

def activate_venv(file_name):
    if system() == 'Windows':
        subprocess.run([r".venv\Scripts\python", file_name])
    else:
        subprocess.run([r"source .venv/bin/python", file_name])

def setup(file_name, version):
    if not check_python_version():
        if not check_if_pip_is_installed():
            install_pip()
        if not check_uv_is_installed():
            install_uv()
        create_venv(version)
        activate_venv(file_name)
    else:
        if system() == 'Windows':
            subprocess.run([executable, file_name])
        else:
            subprocess.run([executable, file_name])
        

if __name__ == "__main__":
    setup(file_name="new_test.py", version=3.13)