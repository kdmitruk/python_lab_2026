#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

float avg(std::vector<float> floats) {
    float sum = 0.0;
    for(float f: floats) {
        sum += f;
    }
    return sum / floats.size();
}

PYBIND11_MODULE(avg, var) {
    var.def("avg", &avg);
}