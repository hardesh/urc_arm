# Install script for directory: /home/harshal/urc/urc_arm/urc_arm_ws/src/armbot

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/harshal/urc/urc_arm/urc_arm_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/harshal/urc/urc_arm/urc_arm_ws/build/armbot/catkin_generated/installspace/armbot.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/armbot/cmake" TYPE FILE FILES
    "/home/harshal/urc/urc_arm/urc_arm_ws/build/armbot/catkin_generated/installspace/armbotConfig.cmake"
    "/home/harshal/urc/urc_arm/urc_arm_ws/build/armbot/catkin_generated/installspace/armbotConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/armbot" TYPE FILE FILES "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/armbot/config" TYPE FILE FILES "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/config/controllers.yaml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/armbot/launch" TYPE FILE FILES
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/launch/after_example_18_15.launch"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/launch/after_example_18_16.launch"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/launch/all.launch"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/launch/cougarbot.launch"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/launch/example_18_11.launch"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/armbot/moveit_examples/config" TYPE FILE FILES "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/moveit_examples/config/controller.yaml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/armbot/moveit_examples/launch" TYPE FILE FILES "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/moveit_examples/launch/cougarbot_moveit_controller_manager.launch.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/armbot/urdf" TYPE FILE FILES
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/urdf/cougarbot.urdf"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/urdf/example_18_10.urdf"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/urdf/example_18_12.urdf"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/urdf/example_18_13.urdf"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/urdf/example_18_14.urdf"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/urdf/example_18_16.urdf"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/urdf/example_18_1.urdf"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/urdf/example_18_2.urdf"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/urdf/example_18_3.urdf"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/urdf/example_18_4.urdf"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/urdf/example_18_5.urdf"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/urdf/example_18_6.urdf"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/urdf/example_18_7.urdf"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/urdf/example_18_8.urdf"
    "/home/harshal/urc/urc_arm/urc_arm_ws/src/armbot/urdf/example_18_9.urdf"
    )
endif()

