SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"

mkdir -p input
mkdir -p output

pushd $SCRIPT_DIR
  values=(
    '2,25'
    '3,50'
    '4,100'
    '5,250'
    '6,500'
    '7,1000'
    '8,1500'
    '9,2000'
    '10,3000'
    '11,4000'
    '12,5000'
    '13,6000'
    '14,7000'
    '15,8000'
    '16,9000'
    '17,10000'
  )

  for datarow in "${values[@]}"; do
    while IFS=',' read -r i n; do
      echo $i $n
      echo $n | python3 ./mkin.py > input/input$i.txt;
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
