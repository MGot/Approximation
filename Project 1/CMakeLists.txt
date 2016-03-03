cmake_minimum_required(VERSION 3.3)
project(Project_1)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp completegraph.cpp completegraph.h edge.cpp edge.h vertex.cpp vertex.h)
add_executable(Project_1 ${SOURCE_FILES})