#include <pybind11/pybind11.h>

int add(int a, int b) {
    return a + b;
}

int mul(int a, int b) {
    return a * b;
}

PYBIND11_MODULE(operations, var) {
    var.def("add", &add);
    var.def("mul", &mul);
}
