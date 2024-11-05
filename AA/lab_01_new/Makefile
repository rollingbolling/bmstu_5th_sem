CC := gcc
SRC_DIR := ./src
INC_DIR := ./inc
OUT_DIR := ./out

CFLAGS := -Wall -Werror -Wextra -I $(INC_DIR)

OBJ_ALL := $(OUT_DIR)/algorithms.o $(OUT_DIR)/alloc_mtrx.o $(OUT_DIR)/measurement.o
OBJ_MAIN := $(OUT_DIR)/main.o

all: app.exe

app.exe : $(OBJ_ALL) $(OBJ_MAIN)
	$(CC) $^ -o $@

$(OUT_DIR)/%.o: $(SRC_DIR)/%.c $(INC_DIR)/*.h | object_dir
	$(CC) $(CFLAGS) -c $< -o $@

.PHONY: object_dir
object_dir:
	@mkdir -p $(OUT_DIR)

clean:
	rm -rf $(OUT_DIR)\*.o
	rm -rf app.exe
