import os
import sys
import time
import shutil
import subprocess
import webbrowser

if getattr(sys, 'frozen', False):
    PROJECT_ROOT = os.path.dirname(os.path.dirname(sys.executable))
else:
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

ADMIN_PORTAL = os.path.join(PROJECT_ROOT, 'scripts', 'admin_portal.py')
URL = 'http://127.0.0.1:5050'

print('=' * 60)
print('PHISHING INTELLIGENCE - ADMIN PORTAL')
print('=' * 60)

if not os.path.exists(ADMIN_PORTAL):
    print('ADMIN PORTAL NOT FOUND:')
    print(ADMIN_PORTAL)
    input('Press Enter to exit...')
    sys.exit(1)

python_exe = shutil.which('python')

if not python_exe:
    print('Python was not found.')
    input('Press Enter to exit...')
    sys.exit(1)

print('Starting Admin Portal...')

subprocess.Popen([python_exe, ADMIN_PORTAL], cwd=PROJECT_ROOT)

time.sleep(4)

print('Opening dashboard...')
webbrowser.open(URL)

print()
print('Dashboard:', URL)
print('Username: admin')
print('Password: admin123')
