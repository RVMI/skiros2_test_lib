cmake_minimum_required(VERSION 2.8.3)
project(skiros2_test_lib)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  rospy
  skiros2_msgs
)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)

## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
catkin_python_setup()

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES hand_eye_calibration
 CATKIN_DEPENDS rospy skiros2_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)


catkin_install_python(PROGRAMS
  test/single_skill_test
  test/skiros_doc_test
  test/world_model_test
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
