for i in {0..1}
do
  python3 ./solution.py < samples/input/input$i.txt > samples/output/output$i.txt
  echo $i
done