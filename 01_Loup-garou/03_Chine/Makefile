all: preface scenario post

preface:
	mv build/*.toc ./

post:
	mkdir -p build
	mv *.aux build/
	mv *.log build/
	mv *.toc build/

scenario: scenar-chine2053.tex
	xelatex scenar-chine2053.tex
