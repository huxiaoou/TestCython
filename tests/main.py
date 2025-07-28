if __name__ == "__main__":
    from alg import add, mul
    from alg2 import minus, divide
    from utl import sep

    sep("add")
    print(f"add(2,3) = {add(2,3)}")
    sep("sub")
    print(f"sub(2,3) = {minus(2,3)}")
    sep("mul")
    print(f"mul(2,3) = {mul(2,3)}")
    sep("dvd")
    print(f"dvd(2,3) = {divide(2,3)}")
    sep("dvd")
    print(f"dvd(2,0) = {divide(2,0)}")
