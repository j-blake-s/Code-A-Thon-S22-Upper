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

rm -rf cases.zip

for i in {2..50}
do
  echo $i | python3 ./mkin.py > input/input$i.txt
  python3 ./solutions/sol.py < input/input$i.txt > output/output$i.txt
#   if [[ $? -ne 0 ]]; then
    # break
#   fi

  echo $i
done

zip -r cases input output
