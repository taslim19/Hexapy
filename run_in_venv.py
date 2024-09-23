import os
import subprocess
import sys

# Define paths
venv_dir = 'venv'
requirements_file = 'requirements.txt'
script_file = 'hunt.py'

# Step 1: Create a virtual environment if it doesn't exist
if not os.path.exists(venv_dir):
    print(f"Creating virtual environment in {venv_dir}...")
    subprocess.check_call([sys.executable, '-m', 'venv', venv_dir])

# Step 2: Install dependencies from requirements.txt
venv_python = os.path.join(venv_dir, 'bin', 'python') if os.name != 'nt' else os.path.join(venv_dir, 'Scripts', 'python')

if os.path.exists(requirements_file):
    print(f"Installing dependencies from {requirements_file}...")
    subprocess.check_call([venv_python, '-m', 'pip', 'install', '-r', requirements_file])
else:
    print(f"{requirements_file} not found! Please provide a requirements.txt file.")
    sys.exit(1)

# Step 3: Run the main script (hunt.py) inside the virtual environment
print(f"Running {script_file}...")
subprocess.check_call([venv_python, script_file])
