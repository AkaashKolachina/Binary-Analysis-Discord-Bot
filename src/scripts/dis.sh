
echo "Attempting to disassemble $1"

# Clear out file if it exists

# TODO Add a folder to put files like this into
# This way it can be accessed by disbot
if test -f "src/results/symbols.txt"; 
then
    rm "src/results/symbols.txt"
fi

objdump --syms $1 > src/results/symbols.txt

if [ -s "src/results/symbols.txt" ]
then
    echo "Success! Table stored at symbols.txt"
else
    echo "Failed!"
fi
