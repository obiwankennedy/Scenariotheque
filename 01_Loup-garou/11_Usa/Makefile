all: preface scenario post

preface:
	mv build/*.toc ./

post:
	mkdir -p build
	mv *.aux build/
	mv *.log build/
	mv *.toc build/

scenario: usa.tex
	xelatex usa.tex
