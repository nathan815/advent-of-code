set -e

DAY=$1
echo "DAY: $DAY"
DIRECTORY=day$DAY

if [ ! -d "$DIRECTORY" ]; then
    mkdir $DIRECTORY
    cd $DIRECTORY
    touch {test_,}part{1,2}.py
    touch problem.txt
    touch input.txt
fi
