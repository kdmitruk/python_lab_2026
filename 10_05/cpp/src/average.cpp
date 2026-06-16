#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>


template <typename T>

double average(const std::vector<T> &inputVEC){
    double sum;
    for(int i = 0; i<inputVEC.size(); i++){
        sum+= inputVEC[i];
    }
    return sum/inputVEC.size();
}
PYBIND11_MODULE(average, a) {
    a.def("average", &average<double>);
    a.def("average", &average<int>);


}
