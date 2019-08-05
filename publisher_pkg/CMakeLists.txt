cmake_minimum_required(VERSION 3.5)
project(publisher_pkg)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(my_msgs REQUIRED)
find_package(rclcpp REQUIRED)

add_executable(publisher src/publisher.cpp)
ament_target_dependencies(publisher
    "rclcpp"
    "my_msgs")

install(TARGETS
    publisher
    DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY
    launch
    DESTINATION share/${PROJECT_NAME}/
)

ament_package()
