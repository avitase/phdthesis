.PHONY: all clean build/main.pdf

PDF = phddefence_nismeinert.pdf

all: $(PDF)

$(PDF): build/main.pdf
	cp $< $@

build/main.pdf:
	mkdir -p build && \
	lualatex -halt-on-error -jobname=build/main main.tex

clean:
	make clean -f Makefile.snippets
	rm -f slides/build/*
