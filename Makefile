CC=gcc
CFLAGS=-I. -fPIC
OBJ=obj
SRC=sha3
TARGET=libx13bcd_hash.so

SOURCES := $(wildcard $(SRC)/*.c)
OBJS :=  $(patsubst $(SRC)/%.c, $(OBJ)/%.o, $(SOURCES)) $(OBJ)/x13.o


$(TARGET): $(OBJS) 
	$(CC) -o $@ $^ $(CFLAGS) -shared 
	cp $@ /usr/lib

$(OBJ)/%.o: $(SRC)/%.c | $(OBJ)
	$(CC) -c -o $@ $< $(CFLAGS)

$(OBJ):
	mkdir obj

$(OBJ)/x13.o: x13.c
	$(CC) -c -o $@ $< $(CFLAGS)

.PHONY: clean
clean:
	rm -Rf $(OBJ) *.so 
