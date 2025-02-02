# might only work on windows

#on windows, open this using run, then type Bash
# cd Documents/College\ Notes/ACM/CodeathonFall2020/SymbolSubstitution/

#or using cmd use bash testgen.sh

#first use dos2unix testgen.sh to get rid of windows characters
#in bash use ./testgen.sh

# SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd -P)"
# echo $SCRIPT_DIR

[[ -e input/ ]] && rm -r input/ 
[[ -e output/ ]] && rm -r output/ 
# rm -r -p output/
mkdir -p input
mkdir -p output

# cp $SCRIPT_DIR/input1.txt $SCRIPT_DIR/input/input1.txt
# [[ -e ../../OddOrigami.java ]] && cp ../../OddOrigami.java ./solutions
# [[ -e ../../CommentingGenerator.java ]] && cp ../../CommentingGenerator.java ./

[[ -e samples/input ]] && cp -r samples/input ./
[[ -e samples/output ]] && cp -r samples/output ./

# [[ -e f.txt ]] && cp ../../perimGen23.java ./ 
# pushd $SCRIPT_DIR

# for i in {2..10}
# do
#   # echo "$(cd "$(dirname "$0")" && pwd -P)"
#   echo $i > input/input$i.txt
#   echo $i
# done

for i in {3..30}
do
  # echo "$(cd "$(dirname "$0")" && pwd -P)"
  echo $i | python3 ./mkin.py > input/input$i.txt
  python3 ./solutions/solution.py < input/input$i.txt > output/output$i.txt

  echo $i
done

# for i in {1..2}
# do
#   # echo "$(cd "$(dirname "$0")" && pwd -P)"
#   echo $i | python3 ./mkin.py > samples/input/input$i.txt
#   python3 ./solutions/solution.py < samples/input/input$i.txt > samples/output/output$i.txt

#   echo $i
# done

rm -rf cases.zip
zip -r cases input output
