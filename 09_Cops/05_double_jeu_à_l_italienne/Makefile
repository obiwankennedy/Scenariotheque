
all: mindmap scenario
	zip double_jeu_`date +'%Y_%m_%d'`.zip mindmap.svg mindmap.jpg 01_enquete_meurtre.pdf 02_enquete_fourgon.pdf *.odt fiches_personnages/*.pdf README.md  

mindmap:
	dot -Tjpg mindmap.dot -Gdpi=90 -o mindmap.jpg
	dot -Tsvg mindmap.dot -o mindmap.svg

scenario: 01_enquete_meurtre.md 02_enquete_fourgon.md
	markdown-pdf 01_enquete_meurtre.md -o 01_enquete_meurtre.pdf
	markdown-pdf 02_enquete_fourgon.md -o 02_enquete_fourgon.pdf

clean:
	rm 01_enquete_meurtre.pdf
	rm 02_enquete_fourgon.pdf
	rm mindmap.jpg 
	rm mindmap.svg
	rm double_jeu*.zip
