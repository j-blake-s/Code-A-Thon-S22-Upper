#!/bin/bash
#generates sample input and output

for i in {0..1}
do
  echo $i | python ./mkin.py > samples/input/input$i.txt
  python3 solutions/sol.py < samples/input/input$i.txt > samples/output/output$i.txt
done
