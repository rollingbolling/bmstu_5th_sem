cmake_minimum_required(VERSION 3.0.0)
project(lab_01 VERSION 0.1.0 LANGUAGES C CXX)

include(CTest)
enable_testing()

add_executable(lab_01 main.cpp
        src/algorithms.cpp inc/algorithms.h
        src/allocation.cpp inc/allocation.h
        src/print_matrix.cpp inc/print_matrix.h)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
