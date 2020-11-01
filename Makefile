.PHONY: all clean tex/build/thesis.pdf tex/build/selbsterkl.pdf

all: thesis.pdf tex/build/selbsterkl.pdf

thesis.pdf: tex/build/thesis.pdf
	cp $< $@

tex/build/thesis.pdf: $(shell find tex -name '*.tex') thesis.xmpdata
	cd tex && mkdir -p build && \
	cp ../thesis.xmpdata build/ && \
	python3 make_bibliography.py > bibliography.tex && \
	lualatex -output-directory=build/ thesis.tex && \
	makeglossaries -d build thesis 

tex/build/selbsterkl.pdf: tex/selbsterkl.tex
	cd tex && mkdir -p build && \
	lualatex -output-directory=build/ selbsterkl.tex

clean:
	rm -f tex/build/*
