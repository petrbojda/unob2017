# Install script for directory: /home/petr/Projects/Bajer/unob2017/gr-prn/python

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
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

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/prn" TYPE FILE FILES
    "/home/petr/Projects/Bajer/unob2017/gr-prn/python/__init__.py"
    "/home/petr/Projects/Bajer/unob2017/gr-prn/python/ssrg_ff.py"
    "/home/petr/Projects/Bajer/unob2017/gr-prn/python/ssrg_bpsk_fc.py"
    "/home/petr/Projects/Bajer/unob2017/gr-prn/python/ssrg_qpsk_fc.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/prn" TYPE FILE FILES
    "/home/petr/Projects/Bajer/unob2017/gr-prn/build/python/__init__.pyc"
    "/home/petr/Projects/Bajer/unob2017/gr-prn/build/python/ssrg_ff.pyc"
    "/home/petr/Projects/Bajer/unob2017/gr-prn/build/python/ssrg_bpsk_fc.pyc"
    "/home/petr/Projects/Bajer/unob2017/gr-prn/build/python/ssrg_qpsk_fc.pyc"
    "/home/petr/Projects/Bajer/unob2017/gr-prn/build/python/__init__.pyo"
    "/home/petr/Projects/Bajer/unob2017/gr-prn/build/python/ssrg_ff.pyo"
    "/home/petr/Projects/Bajer/unob2017/gr-prn/build/python/ssrg_bpsk_fc.pyo"
    "/home/petr/Projects/Bajer/unob2017/gr-prn/build/python/ssrg_qpsk_fc.pyo"
    )
endif()

