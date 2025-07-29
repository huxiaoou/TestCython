if __name__ == "__main__":
    from alg import add, mul
    from alg2 import minus, divide
    from alg3 import cal_average_salary, CQuant
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
    sep("cal average salary")
    quants = [
        CQuant(name="Jack", gender="M", age=24, salary=1_000),
        CQuant(name="Marry", gender="F", age=27, salary=1_500),
        CQuant(name="Bob", gender="M", age=32, salary=2_200),
    ]
    average = cal_average_salary(quants)
    print(f"Average of salary of all quants = {average:.2f}")
