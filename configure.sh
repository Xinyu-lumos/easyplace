#! /bin/zsh
cmake  -S . -B build -DCMAKE_INSTALL_PREFIX=./install -DPython_EXECUTABLE=$(which python)   