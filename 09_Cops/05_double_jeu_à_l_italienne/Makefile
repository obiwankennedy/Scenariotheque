
all: mindmap scenario

mindmap:
	dot -Tjpg mindmap.dot -Gdpi=90 -o mindmap.jpg
	dot -Tsvg mindmap.dot -o mindmap.svg

scenario: 01_enquete_meurtre.md 02_enquete_fourgon.md
	markdown-pdf 01_enquete_meurtre.md -o 01_enquete_meurtre.pdf
	markdown-pdf 02_enquete_fourgon.md -o 02_enquete_fourgon.pdf
