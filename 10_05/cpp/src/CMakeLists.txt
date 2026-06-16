cmake_minimum_required(VERSION 3.16)
project(cpp LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

execute_process(
    COMMAND python3 -c "import pybind11; print(pybind11.get_cmake_dir())"
    OUTPUT_VARIABLE pybind11_DIR OUTPUT_STRIP_TRAILING_WHITESPACE
)


find_package(pybind11 REQUIRED)

pybind11_add_module(operations operations.cpp)
pybind11_add_module(power power.cpp)

# cmake -S . -B ../build/