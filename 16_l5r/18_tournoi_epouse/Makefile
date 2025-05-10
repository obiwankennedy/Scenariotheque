all: folder pandoc pdf grip  #gimli 

pandoc: 01_tournoi.md
	pandoc 01_tournoi.md -s -o output/pandoc/01_tournoi.pdf


pdf: 01_tournoi.md
	markdown-pdf 01_tournoi.md 
	mv 01_tournoi.pdf output/markdown-pdf/

grip: 01_tournoi.md
	grip 01_tournoi.md

gimli: 01_tournoi.md
	cd /home/renaud/applications/other/gimli/gimli/bin
	./gimli -f /home/renaud/documents/03_jdr/01_Scenariotheque/16_l5r/18_tournoi_epouse/01_tournoi.md -w '--toc --footer-right "[page]/[toPage]"'
	mv 01_tournoi.pdf /home/renaud/documents/03_jdr/01_Scenariotheque/16_l5r/18_tournoi_epouse/output/gimli/

folder: 
	mkdir -p output/pandoc
	mkdir -p output/grip
	mkdir -p output/markdown-pdf
	#mkdir -p output/gimli


images:
	resizeImage.sh

clean:
	rm -rf output