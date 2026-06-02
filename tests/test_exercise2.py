import subprocess
import sys


def test_exercise2_script():
    proc = subprocess.run([sys.executable, "exercises/exercise2.py"], input="alice\n", capture_output=True, text=True)
    assert proc.returncode == 0
    assert proc.stdout.strip().endswith("hello Alice")
