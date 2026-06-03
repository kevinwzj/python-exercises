import subprocess
import sys
from exercises.exercise1 import greet, main


def test_greet():
    assert greet("Alice") == "Hello, Alice!"


def test_cli():
    res = subprocess.run([sys.executable, "exercises/exercise1.py", "Bob"], capture_output=True, text=True)
    assert res.returncode == 0
    assert res.stdout.strip() == "Hello, Bob!"


def test_main_uses_argv(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["exercise1.py", "Charlie"])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Charlie!"
