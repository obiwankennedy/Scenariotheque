all: preface scenario post
first: scenario post

preface:
	mv build/*.toc ./

post:
	mkdir -p build
	mv *.aux build/
	mv *.log build/
	mv *.toc build/

scenario: roi.tex
	xelatex roi.tex
