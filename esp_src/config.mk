# config.mk
THIS_DIR := $(realpath $(dir $(realpath $(lastword $(MAKEFILE_LIST)))))
ROOT := ~/

LIBS = $(ESP_LIBS)/SPI \
  $(ESP_LIBS)/Wire \
  $(ESP_LIBS)/ESP8266WiFi \
  $(wildcard $(ARDUINO_LIBS)) \
# $(HOME)/.platformio/lib
#   $(ROOT)/ext_lib

BOARD = nodemcuv2

# UPLOAD_SPEED = 115200