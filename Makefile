.DEFAULT_GOAL := menu

SOURCES := menu.c

BUILD_DIR := build
SOURCE_DIR := MENU
INC_DIR := NNV

SRC := $(SOURCES:%.c=source/%.c)
CC = gcc
CFLAGS = -O0 -g3
PARTS = $(SOURCES:%.c=$(BUILD_DIR)/%.o)

.PHONY: clean
clean:
	rm -f $(BUILD_DIR)/*.o
	rm -f $(BUILD_DIR)/menu

menu : $(PARTS)
	echo parts: $(PARTS)
	echo build: $(SRC)
	$(CC) -o $(BUILD_DIR)/menu $(PARTS) $(CFLAGS)

$(BUILD_DIR)/%.o : $(SOURCE_DIR)/%.c | $(BUILD_DIR)
	$(CC) -c $< -o $@ $(CFLAGS)