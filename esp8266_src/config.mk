# config.mk
THIS_DIR := $(realpath $(dir $(realpath $(lastword $(MAKEFILE_LIST)))))
# ROOT := $(THIS_DIR)/..

LIBS = $(ESP_LIBS)/SPI \
  $(ESP_LIBS)/Wire \
  $(ESP_LIBS)/ESP8266WiFi \
  $(wildcard $(ARDUINO_LIBS)) \
#   $(ROOT)/libraries 
#   $(ROOT)/ext_lib

# UPLOAD_SPEED = 115200