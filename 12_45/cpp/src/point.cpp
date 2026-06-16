#include <pybind11/pybind11.h>
#include <cmath>

struct Point{
    int x;
    int y;

    Point(int x, int y) {
        this->x = x;
        this->y = y;
    }

        Point() {
        this->x = 0;
        this->y = 0;
    }
};

float distancePoints(Point a, Point b) {
    return hypot((b.x - a.x), (b.y - a.y));
}

PYBIND11_MODULE(point, var) {
    pybind11::class_<Point>(var, "Point")
    .def(pybind11::init<int, int>())
    .def(pybind11::init())
    .def_readwrite("x", &Point::x)
    .def_readwrite("y", &Point::y);
    var.def("distancePoints", &distancePoints);
}
