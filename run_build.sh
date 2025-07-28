#!/usr/bin/bash -l

rm -r build/*
rm tests/*.so
python setup.py build_ext
cp build/lib.linux-x86_64-3.9/package_huxo/alg.cpython-39-x86_64-linux-gnu.so tests
cp build/lib.linux-x86_64-3.9/package_huxo/alg2.cpython-39-x86_64-linux-gnu.so tests
cp build/lib.linux-x86_64-3.9/package_sxzq/utl.cpython-39-x86_64-linux-gnu.so tests
