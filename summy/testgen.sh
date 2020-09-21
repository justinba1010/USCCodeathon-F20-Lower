SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"

mkdir -p input
mkdir -p output

pushd $SCRIPT_DIR
  values=(
    '2,25,4'
    '3,50,8'
    '4,100,16'
    '5,250,25'
    '6,500,100'
    '7,1000,100'
    '8,1500,500'
    '9,2000,1999'
    '10,3000,2000'
    '11,4000,3000'
    '12,5000,3000'
    '13,6000,3000'
    '14,7000,5000'
    '15,8000,7500'
    '16,9000,5500'
    '17,10000,9000'
    '18,20000,15000'
    '19,50000,30000'
    '20,100000,50000'
    '21,250000,200000'
    '22,500000,250000'
  )

  for datarow in "${values[@]}"; do
    while IFS=',' read -r i n k;  do
      echo $i $n $k
      echo $n $k | python3 ./mkin.py > input/input$i.txt;
      python3 ./solutions/solution.py < input/input$i.txt > output/output$i.txt
    done <<< "$datarow"
  done

  for i in {0..1}
  do
    python3 ./solutions/solution.py < input/input$i.txt > output/output$i.txt
  done
popd

rm -rf cases.zip
zip -r cases input output
