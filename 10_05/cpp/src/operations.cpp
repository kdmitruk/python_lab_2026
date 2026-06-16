#include <pybind11/pybind11.h>

int add(int a, int b) {
    return a + b;
}

int mul(int a, int b) {
    return a * b;
}



PYBIND11_MODULE(operations, operations) {
    operations.def("add", &add);
    operations.def("mul", &mul);
}