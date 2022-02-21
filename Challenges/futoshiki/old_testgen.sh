#On windows, you can use the linux subsystem, then run testgen.sh

#first use dos2unix testgen.sh to get rid of windows characters

#remove existing input and output
[[ -e input/ ]] && rm -r input/ 
[[ -e output/ ]] && rm -r output/ 
mkdir -p input
mkdir -p output

#copy over samples
[[ -e samples/input ]] && cp -r samples/input ./
[[ -e samples/output ]] && cp -r samples/output ./

for i in {2..10}
do
  python3 ./samples/scraper/scrape_boards.py scrape
  python3 ./samples/scraper/scrape_boards.py input > input/input$i.txt
  python3 ./samples/scraper/scrape_boards.py output > output/output$i.txt

  echo $i
done

rm -rf cases.zip
zip -r cases input output
