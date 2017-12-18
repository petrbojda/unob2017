INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_PRN prn)

FIND_PATH(
    PRN_INCLUDE_DIRS
    NAMES prn/api.h
    HINTS $ENV{PRN_DIR}/include
        ${PC_PRN_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    PRN_LIBRARIES
    NAMES gnuradio-prn
    HINTS $ENV{PRN_DIR}/lib
        ${PC_PRN_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(PRN DEFAULT_MSG PRN_LIBRARIES PRN_INCLUDE_DIRS)
MARK_AS_ADVANCED(PRN_LIBRARIES PRN_INCLUDE_DIRS)

