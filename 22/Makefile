.PHONY: all clean run/all

CC := g++
SRCDIR := src
BUILDDIR := bin
INPUTDIR := in

CPP_SOURCES := $(shell find $(SRCDIR) -type f -name '*.cpp')
CPP_OBJECTS := $(notdir $(basename $(CPP_SOURCES)))

PY_SOURCES := $(shell find $(SRCDIR) -type f -name '*.py')
PY_OBJECTS := $(notdir $(basename $(PY_SOURCES)))

ALL_OBJECTS := $(CPP_OBJECTS) $(PY_OBJECTS)

BINS := $(addprefix $(BUILDDIR)/, $(ALL_OBJECTS))

CFLAGS := -g -O3 -mavx -Wall -Wextra -fopenmp -std=c++11 -Isrc
LIB := -fopenmp

all: $(CPP_OBJECTS)

$(CPP_OBJECTS):%: $(SRCDIR)/%.cpp
	mkdir -p $(BUILDDIR)
	$(CC) -o $(BUILDDIR)/$@ $< $(CFLAGS) $(LIB)

run/all: $(addprefix run/, $(ALL_OBJECTS))

run/%: %
	echo -n "\033[0;32m"
	echo "####################### \n#       Day $(shell printf "%02d" $<)        # \n####################### " && echo
	echo && $(BUILDDIR)/$< < $(INPUTDIR)/$(@F).in && echo
	echo "\033[0m"


$(PY_OBJECTS):%: $(SRCDIR)/%.py
	mkdir -p $(BUILDDIR)
	ln -f $< $(BUILDDIR)/$@
	chmod +x $(BUILDDIR)/$@

clean:
	$(RM) -r $(BUILDDIR) $(TARGET)