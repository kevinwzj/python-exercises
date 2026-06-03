import runpy
import subprocess
import sys
from exercises.exercise2 import greet, main


def test_greet():
    assert greet(" alice ") == "hello Alice"


def test_greet_variants():
    assert greet("BOB") == "hello Bob"
    assert greet("") == "hello "
    assert greet("o'neil") == "hello O'Neil"


def test_exercise2_script():
    proc = subprocess.run([sys.executable, "exercises/exercise2.py"], input="alice\n", capture_output=True, text=True)
    assert proc.returncode == 0
    assert proc.stdout.strip().endswith("hello Alice")


def test_main_with_input(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda prompt="": "dave")
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello Dave"


def test_run_as_module(capsys, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda prompt="": "erin")
    runpy.run_path("exercises/exercise2.py", run_name="__main__")
    captured = capsys.readouterr()
    assert captured.out.strip() == "hello Erin"
