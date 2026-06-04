"""exercise1.py - a minimal starter Python exercise

Run: python exercise1.py [name]
"""


def greet(name: str) -> str:
    """Return a friendly greeting for name."""
    return f"Hello, {name}!"


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument("name", nargs="?", default="World", help="Name to greet")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
