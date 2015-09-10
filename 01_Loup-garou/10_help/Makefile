all: pre file post

pre:
	mv build/*.toc ./

post:
	mkdir -p build
	mv *.aux build/
	mv *.log build/
	mv *.toc build/

file: help.tex donsLatex.tex
	xelatex help.tex
	xelatex donsLatex.tex
