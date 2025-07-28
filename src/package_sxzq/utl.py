def sep(msg: str, length: int = 60):
    print(f"{msg:-^{length}s}")


if __name__ == "__main__":
    sep("hello, world")
