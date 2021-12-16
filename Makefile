.DEFAULT_GOAL := main

SOURCES := menu.c nnv.c main.c
INC := -lmath -lstdio -lstdint -lstdlib

BUILD_DIR := build
SOURCE_DIR := NNV

# this path is wrong
INC_DIR := -L/usr/lib/

SRC := $(SOURCES:%.c=NNV/%.c)
CC = gcc
CFLAGS = -O0 -g3
PARTS = $(SOURCES:%.c=$(BUILD_DIR)/%.o)


.PHONY: clean
clean:
	rm -f $(BUILD_DIR)/*.o
	rm -f $(BUILD_DIR)/main

main : $(PARTS)
	echo parts: $(PARTS)
	echo build: $(SRC)
	$(CC) -o $(BUILD_DIR)/main $(PARTS) $(CFLAGS) $(INC_DIR) $(INC)

$(BUILD_DIR)/%.o : $(SOURCE_DIR)/%.c | $(BUILD_DIR)
	$(CC) $(INC_DIR) $(INC) -c $< -o $@ $(CFLAGS)