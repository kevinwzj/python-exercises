def greet(name: str) -> str:
    """Return a greeting for the given name after normalizing it."""
    return f"hello {name.strip().title()}"


def main() -> None:
    """CLI entry point: prompt for a name and print a greeting."""
    name = input("What's your name?")
    print(greet(name))


if __name__ == "__main__":
    main()
