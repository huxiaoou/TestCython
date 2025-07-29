# Description

This project shows how authors of py-project could use tools like `setuptools`,`Cython` to convert `*.py` files into `*.so` files. By doing so, `*.so` files can be distributed to other users, while preventing them from browsing code details.


# Usage

## Authorize .sh files

```bash
    chmod +x run_build.sh
    chmod +x run_test.sh
```

## Compile and Generate .so file

```bash
    ./run_build.sh
```

After this step, the following 4 `*.so` files should be saved in the directory `tests`.

```bash
    alg.cpython-39-x86_64-linux-gnu.so
    alg2.cpython-39-x86_64-linux-gnu.so
    alg3.cpython-39-x86_64-linux-gnu.so
    utl.cpython-39-x86_64-linux-gnu.so
```

## Test with so file

```bash
    ./run_test.sh
```

### expected result

```bash
----------------------------add-----------------------------
add(2,3) = 5
----------------------------sub-----------------------------
sub(2,3) = -1
----------------------------mul-----------------------------
mul(2,3) = 6
----------------------------dvd-----------------------------
dvd(2,3) = 0.6666666666666666
----------------------------dvd-----------------------------
dvd(2,0) = nan
---------------------cal average salary---------------------
Average of salary of all quants = 1566.67
```

# About **setup_no_pkg.py**

This a simple version of the jobs above. The output would have no package structures and contains vanilla `*.so` files in the following directory only.

```bash
    build/lib.linux-x86_64-3.9
```

for simple `*.py` files, users may want to try this.
