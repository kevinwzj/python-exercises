import subprocess
import sys
from exercises.exercise2 import greet


def test_greet():
    assert greet(" alice ") == "hello Alice"


def test_exercise2_script():
    proc = subprocess.run([sys.executable, "exercises/exercise2.py"], input="alice\n", capture_output=True, text=True)
    assert proc.returncode == 0
    assert proc.stdout.strip().endswith("hello Alice")
