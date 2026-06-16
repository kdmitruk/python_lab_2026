#include <pybind11/pybind11.h>

template<typename T>
T pow2(T a) {
    return a * a;
}

PYBIND11_MODULE(power, var) {
    var.def("pow2", &pow2<double>);
    var.def("pow2", &pow2<int>);
    var.def("pow2_double", &pow2<double>);
}