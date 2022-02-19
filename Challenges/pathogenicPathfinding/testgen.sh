[[ -e input/ ]] && rm -r input/ 
[[ -e output/ ]] && rm -r output/ 
mkdir -p input
mkdir -p output

#copy over samples
[[ -e samples/input ]] && cp -r samples/input ./
[[ -e samples/output ]] && cp -r samples/output ./

for i in {0..32}
do
  echo $i | python3 ./gen.py > input/input$i.txt
  python3 sol.py < input/input$i.txt > output/output$i.txt

  echo $i
done

rm -rf cases.zip
zip -r cases input output