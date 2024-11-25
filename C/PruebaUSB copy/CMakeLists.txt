cmake_minimum_required(VERSION 3.13)

# Configura el proyecto
include(pico_sdk_import.cmake)

project(PruebaUSB)

pico_sdk_init()

add_executable(PruebaUSB PruebaUSB.c)

target_link_libraries(PruebaUSB pico_stdlib hardware_adc hardware_uart)

pico_add_extra_outputs(PruebaUSB)

