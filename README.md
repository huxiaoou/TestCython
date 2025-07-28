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

After this step, the following two files should be saved in the directory `tests`.

```bash
    alg.cpython-39-x86_64-linux-gnu.so
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
```