#include <pybind11/pybind11.h>


template <typename T>
T square(T base){
    return base*base;
}
PYBIND11_MODULE(power, a) {
    a.def("square", &square<double>);
    a.def("square", &square<int>);
    a.def("square_double", &square<double>);

}

