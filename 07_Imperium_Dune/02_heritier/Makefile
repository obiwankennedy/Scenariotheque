all: scenario post

preface:
	touch build/scenario.toc
	mv build/*.toc ./

post:
	mkdir -p build
	mv *.aux build/
	mv *.log build/
	mv *.toc build/

scenario: scenario.tex
	xelatex scenario.tex
