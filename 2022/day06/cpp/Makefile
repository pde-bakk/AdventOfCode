BUILD_DIR := debug
BUILD_TYPE := Debug

all: build

build: $(BUILD_DIR)
	cmake --build $(BUILD_DIR)

$(BUILD_DIR):
	cmake -S . -B $(BUILD_DIR) -DCMAKE_BUILD_TYPE=$(BUILD_TYPE)

clean:
	$(RM) -rf $(BUILD_DIR)

fclean: clean

re:
	$(MAKE) fclean
	$(MAKE) build

.PHONY: all build clean re
